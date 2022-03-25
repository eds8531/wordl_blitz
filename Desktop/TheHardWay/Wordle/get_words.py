"""import shelve

word_file = open('words.txt', 'r')
word_file = word_file.read()

shelfFile = shelve.open('five_words')

word_file = word_file.split(' ')

five_words = []

for i in word_file:
    if len(i) == 5:
        five_words.append(i)

print(five_words[:5])
print(five_words[-5:])
print(len(five_words))

shelfFile['five_words'] = five_words
shelfFile.close()
"""

import shelve
shelfFile = shelve.open('five_words')
