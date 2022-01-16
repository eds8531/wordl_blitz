import shelve
import random

shelfFile = shelve.open('five_words')

five_words = shelfFile['five_words']

random.shuffle(five_words)

print('Length five_words = ' + str(len(five_words)))

target_word = random.choice(five_words)

dead_letters = []

live_letters = []

wrong_letters = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}

placed_letters = {}

guess = 'slate'

if guess == target_word:
    print('Success! The target word was ' + guess)

for i in range(0,5):
    if guess[i] == target_word[i]:
        placed_letters[guess[i]] = i
    elif guess[i] in target_word:
        live_letters.append(guess[i])
        wrong_letters[guess[i]].append(i)
    else:
        dead_letters.append(guess[i])


print(target_word)
print(dead_letters)
print(live_letters)
print(wrong_letters)
print(placed_letters)

guess = 'round'

for i in range(0,5):
    if guess[i] == target_word[i]:
        placed_letters[guess[i]] = i
    if guess[i] in target_word:
        live_letters.append(guess[i])
        wrong_letters[guess[i]].append(i)
    else:
        dead_letters.append(guess[i])

print(dead_letters)
print(live_letters)
print(wrong_letters)
print(placed_letters)

print(len(five_words))

for key in placed_letters:
    five_words = [word for word in five_words if not word[placed_letters[key]] != key]


print(len(five_words))
print(five_words[:25])



for letter in live_letters:
    five_words = [word for word in five_words if letter in word]

for letter in dead_letters:
    five_words = [word for word in five_words if letter not in word]




print(len(five_words))
print(five_words[:25])
