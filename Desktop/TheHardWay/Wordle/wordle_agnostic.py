#The purpose of this version of wordle_blitz is to see what the wrong word distribution looks like when we don't chose the first n guesses.



import shelve
import random
import pandas as pd
import numpy as np
from wordle_wrong import analysis

shelfFile = shelve.open('five_words')
five_words1 = shelfFile['five_words2']

def wordle_blitz(trials, five_words1):
    count = 0
    right = 0
    wrong = 0
    round_dict = {1:0,2:0,3:0,4:0,5:0,6:0}
    missed_words = []
    tries = []
    while count < trials:
        if count%100 ==0:
            print(count)
        guess_list = []
        count += 1
        five_words = five_words1
        random.shuffle(five_words)
        target_word = random.choice(five_words)
        tries.append(target_word)
        guesses = 0
        while guesses < 6:
            guess = random.choice(five_words)
            guess_list.append(guess)
            if guess == target_word:
                right +=1
                round_dict[guesses + 1] += 1
                break

            guesses +=1
            for i in range(0,5):
                if guess[i] == target_word[i]:
                    five_words = [word for word in five_words if  word[i] == guess[i]]
                elif guess[i] in target_word:
                    #Includes letters in words, but in the wrong spaces
                    five_words = [word for word in five_words if guess[i] in word]
                    #Exclude the words with the right letters in the wrong places
                    five_words = [word for word in five_words if  word[i] != guess[i]]

                else:
                    five_words = [word for word in five_words if guess[i] not in word]
        if guesses == 6:
            wrong +=1
            missed_words.append(target_word)
            if wrong%25 == 0:
                print(target_word)
                print(guess_list)
    database = analysis(missed_words, tries)


    print(count)
    print('Correct tries: ' + str(right))
    print('Incorrect tries: ' + str(wrong))
    print('Percent correct: {:.2%}'.format(right/trials))
    print('Correct answers per round:')
    print('Round 4: ' + str(round_dict[4]))
    print('Round 5: ' + str(round_dict[5]))
    print('Round 6: ' + str(round_dict[6]))



    return database
