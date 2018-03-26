import psycopg2
import sys, os, configparser, csv
from pyspark import SparkConf, SparkContext
from datetime import datetime

log_path = "/home/hadoop/logs/"  # don't change this
aws_region = "us-east-1"  # don't change this
s3_bucket = "cs327e-fall2017-final-project"  # don't change this
the_numbers_files = "s3a://" + s3_bucket + "/the-numbers/*"  # dataset for milestone 3

# global variable sc = Spark Context
sc = SparkContext()

# global variables for RDS connection
rds_config = configparser.ConfigParser()
rds_config.read(os.path.expanduser("~/config"))
rds_database = rds_config.get("default", "database")
rds_user = rds_config.get("default", "user")
rds_password = rds_config.get("default", "password")
rds_host = rds_config.get("default", "host")
rds_port = rds_config.get("default", "port")


def init():
    # set AWS access key and secret account key
    cred_config = configparser.ConfigParser()
    cred_config.read(os.path.expanduser("~/.aws/credentials"))
    access_id = cred_config.get("default", "aws_access_key_id")
    access_key = cred_config.get("default", "aws_secret_access_key")

    # spark and hadoop configuration
    sc.setSystemProperty("com.amazonaws.services.s3.enableV4", "true")
    hadoop_conf = sc._jsc.hadoopConfiguration()
    hadoop_conf.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    hadoop_conf.set("com.amazonaws.services.s3.enableV4", "true")
    hadoop_conf.set("fs.s3a.access.key", access_id)
    hadoop_conf.set("fs.s3a.secret.key", access_key)
    os.environ['PYSPARK_SUBMIT_ARGS'] = "--packages=org.apache.hadoop:hadoop-aws:2.7.3 pyspark-shell"


################## general utility function ##################################

def print_rdd(rdd, logfile):
    f = open(log_path + logfile, "w")
    results = rdd.collect()
    counter = 0
    for result in results:
        counter = counter + 1
        f.write(str(result) + "\n")
        if counter > 30:
            break
    f.close()


################## process the-numbers dataset #################################

def parse_line(line):
    # add logic for parsing and cleaning the fields as specified in step 4 of assignment sheet
    currentLine = line.split("\t")
    release_year = datetime.strptime(currentLine[0], "%m/%d/%Y").strftime("%Y")
    movie_title = currentLine[1].upper().encode('utf-8')
    genre = currentLine[2].strip()
    if (genre == "Thriller/Suspense"):
        genre = "Thriller"
    elif (genre == "Black Comedy"):
        genre = "Comedy"
    elif (genre == "Romantic Comedy"):
        genre = "Romance"
    budgetOrig = currentLine[3].strip()
    budgetCleaned = budgetOrig.replace("$", "").replace(",", "").replace("\\", "").replace(" ", "").replace('"', "")
    if len(budgetCleaned) == 0:
        budget = -1
    else:
        budget = int(budgetCleaned)
    box_officeOrig = currentLine[4].strip()
    box_officeCleaned = box_officeOrig.replace("$", "").replace(",", "").replace("\\", "").replace(" ", "").replace('"',
                                                                                                                    "")
    if len(box_officeCleaned) == 0:
        box_office = -1
    else:
        box_office = int(box_officeCleaned)

    return (release_year, movie_title, genre, budget, box_office)


init()
base_rdd = sc.textFile(the_numbers_files)
mapped_rdd = base_rdd.map(parse_line)
print_rdd(mapped_rdd, "mapped_rdd")


def save_to_db(list_of_tuples):
    conn = psycopg2.connect(database=rds_database, user=rds_user, password=rds_password, host=rds_host, port=rds_port)
    conn.autocommit = True
    cur = conn.cursor()

    # add logic to look up the title_id in the database as specified in step 5 of assignment sheet
    # add logic to write out the financial record to the database as specified in step 5 of assignment sheet
    for tupl in list_of_tuples:
        release_year, movie_title, genre, budget, box_office = tupl

        insertStatement = "INSERT INTO title_financials VALUES (%s, %s, %s)"

        initQueryStatement = "select count(title_id) from title_basics with Index(ColumnIndex) where %s = start_year and %s = upper(primary_title)"

        cur.execute(initQueryStatement, (release_year, movie_title))
        numTitleID = len(cur.fetchall())

        if numTitleID > 1 and box_office > 0:
            tvQueryStatement = "select title_id from title_basics with Index(ColumnIndex) where %s = start_year and %s = upper(primary_title) and title_type = 'movie'"
            cur.execute(tvQueryStatement, (release_year, movie_title))
            titleID = cur.fetchall()
            if len(titleID) == 1:
                titleID = cur.fetchone()
                cur.execute(insertStatement, (titleID, budget, box_office))
            else:
                continue
        elif numTitleID > 1 and box_office <= 0:
            genreQueryStatement = "select title_id from title_basics tb inner join title_genres tg on tb.title_id = tg.title_id with Index(ColumnIndex) where %s = tb.start_year and %s = upper(tb.primary_title) and %s = tg.genre"
            cur.execute(genreQueryStatement, (release_year, movie_title, genre))
            titleID = cur.fetchall()
            if len(titleID) == 1:
                titleID = cur.fetchone()
                cur.execute(insertStatement, (titleID, budget, box_office))
            else:
                pass
        elif numTitleID == 1:
            titleID = cur.fetchone()
            if titleID is None:
                pass
            else:
                cur.execute(insertStatement, (titleID, budget, box_office))

    cur.close()
    conn.close()


mapped_rdd.foreachPartition(save_to_db)

# free up resources
sc.stop()
