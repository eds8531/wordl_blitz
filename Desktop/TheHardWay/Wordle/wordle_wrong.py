import shelve
import random
import numpy as np
import pandas as pd


def analysis(wrong_words, tries):

    shelfFile = shelve.open('/Users/ericschlosser/Desktop/TheHardWay/Wordle/five_words')
    five_words = shelfFile['five_words']

    two_letters = []
    for word in five_words:
        pair = [word, False]
        for letter in word:
            if word.count(letter) > 1:
                pair[1] = True
        two_letters.append(pair[1])

    wrong_word_data = {"Word": five_words,
                        'Tries': [0]*4738,
                      'Number Wrong': [0]*4738,
                      'Percent Missed': [0]*4738,
                      'Round 1': [0]*4738,
                      'Round 2': [0]*4738,
                      'Round 3': [0]*4738,
                      'Round 4': [0]*4738,
                      'Round 5': [0]*4738,
                      'Round 6': [0]*4738,
                      'Guesses': [[]]*4738,
                       'Pattern': [[]]*4738,
                       'Two Letters': two_letters
                      }

    df_ww = pd.DataFrame(wrong_word_data)

    df_ww = df_ww.set_index('Word')

    for word in wrong_words:
        df_ww.loc[word, 'Number Wrong'] += 1

    for word in tries:
        df_ww.loc[word, 'Tries'] += 1

    df_ww.loc[:,'Percent Missed'] = (df_ww.loc[:,'Number Wrong']/df_ww.loc[:,'Tries'])*100

    df_ww.style.format({'Percent Missed': '{:,.2f}.format'})

    return df_ww
