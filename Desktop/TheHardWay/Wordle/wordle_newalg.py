#Algorithm for best next guess:
# If guess is not target, which guess eliminates the
# most possible wrong words from the list of possible words.


import shelve
import random
import pandas as pd

shelfFile = shelve.open('five_words')
five_words1 = shelfFile['five_words2']

def wordle_blitz(guess1, guess2, guess3, trials, five_words1):
    database = shelfFile['blank_db']
    print(database.head())
    count = 0
    right = 0
    wrong = 0
    round_dict = {1:0,2:0,3:0,4:0,5:0,6:0}
    missed_words = []
    while count < trials:
        if count%100 ==0:
            print(count)
        guess_list = []
        count += 1
        possible_target_words = five_words1
        five_words = five_words1
        random.shuffle(five_words)
        target_word = random.choice(five_words)
        guesses = 0

        # Here is the new algorithm.
        # pick the guess that for every possible target word eliminates the most possible guesses on average.

        # find the average len of possible target words list for each word in five_words:
        #pgw =possible guess word
        for pgw in five_words1:
            for ptw in possible_target_words:
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


        while guesses < 6:
            if guesses == 0:
                guess = guess1
            elif guesses == 1:
                guess = guess2
            elif guesses == 2:
                guess = guess3
            else:
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
    for word in missed_words:
        pattern1 = []
        pattern2 = []
        pattern3 = []
        for i in range(0,5):
            if word[i] == guess1[i]:
                pattern1.append('g')
            elif guess1[i] in word:
                pattern1.append('y')
            else:
                pattern1.append('b')
        for i in range(0,5):
            if word[i] == guess2[i]:
                pattern1.append('g')
            elif guess2[i] in word:
                pattern1.append('y')
            else:
                pattern1.append('b')
        for i in range(0,5):
            if word[i] == guess3[i]:
                pattern1.append('g')
            elif guess3[i] in word:
                pattern1.append('y')
            else:
                pattern1.append('b')
        database.at[word, 'Pattern'] = [pattern1, pattern2, pattern3]

    print(count)
    print('Correct tries: ' + str(right))
    print('Incorrect tries: ' + str(wrong))
    print('Percent correct: {:.2%}'.format(right/trials))
    print('Correct answers per round:')
    print('Round 4: ' + str(round_dict[4]))
    print('Round 5: ' + str(round_dict[5]))
    print('Round 6: ' + str(round_dict[6]))



    return database
wordle_blitz('brick','stomp','nudge',10000, five_words1)
