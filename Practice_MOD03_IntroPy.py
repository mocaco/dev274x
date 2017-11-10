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