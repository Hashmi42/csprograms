#  File: Books.py

#  Description:

#  Student Name: Logan Hashmi

#  Student UT EID: Sah4334

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created:

#  Date Last Modified:


# Create word dictionary from the comprehensive word list
word_dict = {}


def create_word_dict():
    book = open('words.txt', 'r')
    for line in book:
        line = line.strip()
        line = line.lower()
        word_list = line.split()
        for word in word_list:
            if word in word_dict:
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1
    book.close()


# Removes punctuation marks from a string but apostrophes
def parseString(st):
    new_str = ''
    st = st.replace("'new_str ", "")
    st = st.replace("' ", "")
    for i in range(len(st)):
        if st[i].isalpha() or st[i].isspace():
            new_str += st[i]
        elif (st[i] == "'"):
            if st[i:] == "'new_str" or st[i:] == "'":
                new_str += ""
            else:
                new_str += st[i]
        else:
            new_str += " "
    return new_str


# get the input file and a word dictionary for pair values
# Returns a dictionary of words and their frequencies
def getWordFreq(file):
    # open book
    bookFile = open(file, "r")
    firstBook = {}
    for lines in bookFile:
        lines = lines.strip()
        lines = parseString(lines)
        lines = lines.split()

        for word in lines:
            if word != " ":
                if word in firstBook:
                    firstBook[word] += 1
                else:
                    firstBook[word] = 1

    bookFile.close()
    keys = list(firstBook.keys())
    capitalWords = []
    for key in keys:
        if key[0].isupper():
            lower_key = key.lower
            if lower_key in firstBook:
                firstBook[lower_key] += firstBook[key]
            elif lower_key in firstBook:
                firstBook[lower_key] = firstBook[key]

    for key in capitalWords:
        del firsBook
    return firstBook


# Compares the distinct words in two dictionaries
def wordComparison(author1, freq1, author2, freq2):
    # initialize counting variables and create set differences
    totalCount1 = 0
    wordCount1 = 0
    for word in freq1:
        totalCount1 += freq1[word]
        wordCount1 += 1
    totalCount2 = 0
    wordCount2 = 0
    for word in freq2:
        totalCount2 += freq2[word]
        wordCount2 += 1
    set1 = set(freq1)
    set2 = set(freq2)
    diff1 = set1 - set2
    diff2 = set2 - set1
    count1 = 0
    for x in diff1:
        count1 += freq1[x]
    count2 = 0
    for x in diff2:
        count2 += freq2[x]

    # Print results
    print()
    print(author1)
    print('Total distinct words =', wordCount1)
    print('Total words (including duplicates) =', totalCount1)
    print('Ratio (% of total distinct words to total words) = wordCount1 / totalCount1 * 100, end=' '')
    print(author2)
    print('Total distinct words =', wordCount2)
    print('Total words (including duplicates) =', totalCount2)
    print('Ratio (% of total distinct words to total words =', wordCount2 / totalCount2 * 100, end='\n\n')
    print('%s used %d words that %s did not use.' % (author1, len(diff1), author2))
    print('Relative frequency of words used by %s not in common with %s =' % (author1, author2), count1 / totalCount1 * 100, end='\n\n')
    print('%s used %d words that %s did not use.' % (author2, len(diff2), author1))
    print('Relative frequency of words used by %s not in common with %s ='
          % (author2, author1), count2 / totalCount2 * 100, end='\n\n')


def main():
    # Enter names of the two books in electronic form
    book1 = input("Enter name of first book: ")
    book2 = input("Enter name of second book: ")
    print()

    # Enter names of the two authors
    author1 = input("Enter last name of first author: ")
    author2 = input("Enter last name of second author: ")
    print()

    # Get the frequency of words used by the two authors
    wordFreq1 = getWordFreq(book1)
    wordFreq2 = getWordFreq(book2)

    # Compare the relative frequency of uncommon words used
    # by the two authors
    wordComparison(author1, wordFreq1, author2, wordFreq2)


main()
