import operator

string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7, 5]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

""" 
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
    count = {}
    for achar in string1:
        count[achar] = count.get(achar,0) +1
    return count

#print count_unique(string1)

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 & set2

#print common_items(list1, list2)

"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shaded between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
#this is unsatisfying
    dict_all = {}
    common_list = []
    for word in list1:
        dict_all[word] = dict_all.setdefault(word, 1)
    for word in list2:
        dict_all[word] = dict_all.get(word, 0) + 1

    for key, value in dict_all.iteritems():
        if value > 1:
            common_list.append(key)
    return common_list
        
#print common_items2(list1, list2)

"""Given a list of numbers, return list of number pairs that sum to zero"""

def sum_zero(list1):
    zero_pairs = []
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            print(list1[i],list1[j])
            if list1[i] + list1[j] == 0:
                zero_pairs.append((list1[i],list1[j]))
    return zero_pairs
print sum_zero(list2)

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    dict_of_list = {}
    for word in words:
        dict_of_list[word] = dict_of_list.get(word, 0) + 1
    no_dupes = []
    for key,value in dict_of_list.iteritems():
        if value < 2:
            no_dupes.append(key)
    return no_dupes

#print find_duplicates(words)


"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    word_length = {}

    for word in words:
        word_length[word] = len(word)
    
    sorted_length = sorted(word_length.items(), key=operator.itemgetter(1))
    return sorted_length

#print word_length(words)


def pirate_translate():
    pirate_string = ""
    pirate_dictionary = {"sir":"matey",
"hotel":"fleabaginn",
"student":"swabbie",
"boy":"matey",
"madam":"proudbeauty",
"professor":"foulblaggart",
"restaurant":"galley",
"your":"yer",
"excuse":"arr",
"students":"swabbies",
"are":"be",
"lawyer":"foulblaggart",
"the":"th'",
"restroom":"head",
"my":"me",
"hello":"avast",
"is":"be",
"man":"matey"}

    print "type in a sentence"
    user_text = raw_input()
    user_text = user_text.split()
    for word in user_text:
        if word in pirate_dictionary:
            word = pirate_dictionary[word]
        pirate_string = pirate_string + " " + word
    return pirate_string

#print(pirate_translate())

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey 

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""
