/* Query 1: Computes productive actors */
select primary_name as actor_name, start_year as year, count(*) as title_count 
from title_basics tb 
inner join stars s on tb.title_id = s.title_id
inner join person_basics pb on pb.person_id = s.person_id
where start_year between 2007 and 2017 and title_type = 'movie'
group by primary_name, start_year 
having count(*) >= 10 
order by start_year, count(*);

/* Query 2: Counts the number of people in each profession */
select profession, count(primary_name)
from person_professions ppf
inner join person_basics pb
on ppf.person_id = pb.person_id
where pb.birth_year >=1987
group by ppf.profession
order by count(pb.primary_name) desc;

<<<<<<< HEAD
\* Query 3: shows highly voted productions with more than 20 seasons */
=======
/* Query 3: shows highly voted productions with more than 20 seasons */
>>>>>>> 777e4c6cb0188647dc937194606182ad9b3d8fc3
select primary_title as title,genre as genre,season_num as seasons, sum(num_votes) as total_votes
from title_genres tg inner join title_basics pb on tg.title_id = pb.title_id
full outer join title_ratings tr on tg.title_id = tr.title_id
full outer join title_episodes te on tg.title_id = te.title_id
group by primary_title, genre, num_votes, season_num
having num_votes>1000 and season_num >20
order by genre;

/* Query 4: Tom Cruise movies and the number of directors that worked with */
select primary_name as actor_name, primary_title as movie_names, count(d.title_id) as number_of_directors
from stars S
inner join person_basics pb on S.person_id = pb.person_id
full outer join title_basics tb on S.title_id = tb.title_id
inner join directors d on S.title_id = d.title_id
where pb.primary_name = 'Tom Cruise'
group by primary_name, birth_year, primary_title, d.title_id
order by primary_title;

/* Query 5: Principals and their number of projects */
/* create small_principals due to full principals causing AWS server to run out of available space in this query */
create materialized view small_principals as select * from principals limit 5000;
CREATE  MATERIALIZED VIEW v_principals_num_titles AS 
select pb.primary_name, count(sp.title_id) as num_titles
from small_principals sp
inner join person_basics pb on pb.person_id = sp.person_id
group by primary_name
order by primary_name;

/* Query 6: writers with the highest rated productions */
select primary_name as writers_name,primary_title as productions_name, tr.num_votes as total_votes, sum(average_rating)
from writers w
inner join person_basics pb on w.person_id = pb.person_id
inner join title_basics tb on w.title_id = tb.title_id
inner join title_ratings tr on tb.title_id = tr.title_id
group by primary_name, primary_title, num_votes
having (num_votes) > 1000000
order by num_votes desc;