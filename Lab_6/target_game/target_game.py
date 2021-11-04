from typing import List
import random
import os, sys

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    x = 0
    grid = []
    while len(grid) < 3:
        temp = []
        while len(temp) < 3:
            letter = chr(random.randint(ord('A'), ord('Z')))
            temp.append(letter)
        grid.append(temp)
    
    return grid



def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(os.path.join(sys.path[0], "en"), "r") as file:
        string = file.read()
        lst = string.split("\n")
       
    result = []

    def is_valid(word, letters):
        for w in word:
            if w in letters:
                letters.remove(w)
            else:
                return False
        return True
    
    for word in lst:
        if is_valid(word, list(letters)):
            if (word not in result) and (len(word)>3):
                result.append(word)
    

    return result


#print(get_words(['a', 'p', 'e', 'l', 'c', 'z', 'w', 'p', 'i']))


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    words = []
    while 1:
        try:
            words.append(input())
        except EOFError:
            break
   
    print(words)

get_user_words()


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    
    


def results():
    pass
