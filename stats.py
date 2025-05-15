def count_words(string):
    #Note: we use split method b/c for loops iterate over characters when given strings.. we need words to iterate over
    words = string.split()   # using split method with no arguements so that all type of white spaces are considered (space, \t tab, \n newline)
    # in this case, split method returns a list of all the words (where space, tab, or newline are all considered delimiters)
    # if split had a separator argument like .split(sep = ' ').. it will treat single whitespaces only and tabs, and newlines are considered one word (i.e. word\tword ... word\nword)

    count = 0

    for word in words:  #iterating over list that contains all the words of string
        count += 1     #we can easily now calculate the count of all the words b/c we know each element in that list is a word

    return count 

def count_chars(string):
    rev_string = string.lower()   #converting all characters to lowercase so we don't consider 'T' and 't' different (case insentive)

    char_count_dict = {}

    for char in rev_string:   # iterating over the characters of the string
        if char not in char_count_dict:   #if character is not an entry/key in the dictonary
            char_count_dict[char] = 1  # set it / intialize the entry/key-value pair .. value is 1 for first occurence count
        else:     #for the current character, there is an entry/key in the dictonary 
            char_count_dict[char] += 1   # since there is, increment the count by incrementing the value of that key in the dictonary
    
    return char_count_dict   # final dictonary that represents the count of all unique characters in that book (string)


def sort_dict(char_dict):

    list_dicts = []

    # dictonaries in the list are formatted as such =>  {"char": "b", "num": 4868} 
    # this format is helpful for sorting a list of dictonaries using .sort()
    for key in char_dict:

        a = {"char": key, "num": char_dict[key]}

        list_dicts.append(a)

    #once we have the list of dictonaries in the corrected format..
    #we use the sort method to sort the list and use the key argument which takes one function (of any type) that returns a value
    #in this case we used a lambda function (aka anonymous function: function with no name)
    #the lambda function is made up of a 'parameter': 'expression' .. has the same structure of a normal function but in one line 
    #the lambda function is applied to each element (dictionary) in the list
    #in our case, when applied to each element, the lambda function will return the value of key 'num' for that current dictonary
    #this value is what's going to represent that dictonary and so this continues for all dictionaries in the list
    #once the lambda function has been applied to all dictonaries in the list, all the values that represent those dictonaries are going to be sorted now
    #once those values are correctly sorted (in this case from greatest to least i.e. key argument reverse=True), the dictonaries can now take that sorted arrangement
    #so the dictonary would have been sorted based on the VALUE of the "num" KEY
    #the sorted list of dictonaries
    list_dicts.sort(key=lambda dictionary: dictionary["num"], reverse=True)

    #final reformatting in this way -> ['key: value', 'key: value', ... ]
    final_list = []

    for dictonary in list_dicts:
        a = f'{dictonary["char"]}: {dictonary["num"]}'

        final_list.append(a)

    return final_list




            