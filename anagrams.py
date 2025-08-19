# |---------------------------------IMPORTS---------------------------------|

import sys
from colorama import Fore, init

init()

# |---------------------------------PROJECT_GOAL---------------------------------|

'''
The goal of this project is to do the following:
    > load a file as a list of words
    > take input from the user
    > create an empty list to store anagrams in
    > sort the user-word
    > loop through each word in the word list
        ->> sort the word
        ->>  if word sorted == user-word sorted:
            ->>> append word to anagrams list
    > print the anagram list
'''

# |---------------------------------FUNCTIONS---------------------------------|

def load_file():
    fname = '2of4brif.txt'
    
    try:
        with open(fname) as file:
            loaded_txt = file.read().strip().split()
            loaded_txt = [x for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f'\nError opening {fname}. Terminating program.')
        sys.exit(1)

def anagrams():
    words = list(load_file()) 

    while True:
        user_input = input(Fore.LIGHTBLUE_EX + f'\nEnter a word make an anagram or type \'exit\' to quit...\n\n' + Fore.LIGHTYELLOW_EX + f'').lower().strip()

        if user_input == 'exit':
            print(Fore.LIGHTRED_EX + f'\nTerminating program\n')
            break

        sorted_user_input = sorted(user_input)

        anagrams = []

        for word in words:
            sorted_word = sorted(word)
            if sorted_word == sorted_user_input:
                anagrams.append(word)

        print(Fore.LIGHTGREEN_EX +'\nAnagrams:', Fore.LIGHTMAGENTA_EX + f'\n{anagrams}')

# |---------------------------------MAIN_LOOP---------------------------------|
if __name__ == '__main__':
    anagrams()