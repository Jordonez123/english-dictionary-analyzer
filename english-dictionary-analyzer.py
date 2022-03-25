#we are going to be iterating through the file dict_test.py and going to be maki#ng a dictionary[word] = index of the word



def count_lines (filename):
    '''this is a method to count the number of lines in
    a given file'''


    file  = open(filename,"r")
    line_count = 0
    for line in file:
        if line != '\n':
            line_count+=1
    file.close()
    return line_count

def process_file(filename):
    '''this function helps us clean up a 
    .txt file into a nice format
    
    this will return an array of words that are
    in the file'''

    word_arr = []

    file  = open(filename,"r")
    for i in range(line_count):
        line = file.readline()
        #print('line: ', line)
        word = line.split('\n')[0]
        if word[0] in alphabet:
            word_arr.append(word)
    file.close()
    return word_arr

def make_word_dict(word_arr):
    '''this function takes in an array of words
    and return a dictionary with word as the key
    and the position of the word as values'''

    dict1 = {}
    for i in range(len(word_arr)):
        dict1[word_arr[i]] = i
    return dict1




def word_analysis(word_dict):
    t_num = len(dict1)
    percentage_sum = 0
    freq_dict = {}
    for letter in alphabet:
        letter_count = 0
        for key in dict1:
            if key[0] == letter:
                letter_count+=1
        letter_percentage = (letter_count/t_num) * 100
        percentage_sum+=letter_percentage
        #print("{} : {}% ".format(letter, letter_percentage))
        freq_dict[letter]  = letter_percentage
    print('sorted frequencies: ' , sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))
    print('total percentage: {}%'.format(percentage_sum))

filename = input('please enter a filename: ')
line_count = count_lines(filename)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

word_arr = process_file(filename)
dict1 = make_word_dict(word_arr)

'''now, we are going to be doing some analysis on the dictionary that we have
gathered. 

1. For every letter in the alphabet, compute the percentage of words in the doc#ument that begin with that corresponding letter

'''
word_analysis(dict1)
