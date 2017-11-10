"""Program: poem mixer
This program takes string input and then prints out a mixed order version of the string
Program Parts
program flow gathers the word list, modifies the case and order, and prints
    get string input, input like a poem, verse or saying
    split the string into a list of individual words
    determine the length of the list
    Loop the length of the list by index number and for each list index:
        if a word is short (3 letters or less) make the word in the list lowercase
        if a word is long (7 letters or more) make the word in the list uppercase
    call the word_mixer function with the modified list
    print the return value from the word_mixer function
word_mixer Function has 1 argument: an original list of string words, containing greater than 5 words and the function returns a new list.
    sort the original list
    create a new list
    Loop while the list is longer than 5 words:
        in each loop pop a word from the sorted original list and append to the new list
        pop the word 5th from the end of the list and append to the new list
        pop the first word in the list and append to the new list
        pop the last word in the list and append to the new list
    return the new list on exiting the loop
"""
def word_mixer(word_list):
    new_words = []
    word_list.sort()
    while len(word_list) > 5:
        new_words.append(word_list.pop(4))
        new_words.append(word_list.pop(0))
        new_words.append(word_list.pop())
    return print (new_words)


poem = input("enter a saying or poem:")
words_in_poem = poem.split(' ')
len_of_words_in_poem = len(words_in_poem)
for index in range(0, len_of_words_in_poem):
    if len(words_in_poem[index]) <= 3:
        words_in_poem[index].lower()
    if len(words_in_poem[index]) >= 7:
        words_in_poem[index].upper()
word_mixer(words_in_poem)