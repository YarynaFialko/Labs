"""Target Game Module"""
from typing import List
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    grid = []
    while len(grid) < 3:
        temp = []
        while len(temp) < 3:
            letter = chr(random.randint(ord('A'), ord('Z')))
            temp.append(letter)
        grid.append(temp)

    return grid



def get_words(file: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(file, "r", encoding="utf-8") as file:
        string = file.read()
        lst = string.split("\n")

    result = []

    def is_valid(word, letters):
        for wor in word:
            if wor in letters:
                letters.remove(wor)
            else:
                return False
        return True

    for word in lst:
        if is_valid(word, list(letters)):
            if (word not in result) and (len(word)>3):
                if word.count(letters[4]) > 0:
                    result.append(word)
    return result


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    words = []
    try:
        words = input().split()
    except EOFError:
        pass

    return words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]: # pylint: disable=line-too-long
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    result = []
    def is_valid(word, letters):
        for wor in word:
            if wor in letters:
                letters.remove(wor)
            else:
                return False
        return True

    for word in user_words:
        if is_valid(word, list(letters)):
            if (word not in result) and (word not in words_from_dict):
                if word.count(letters[4]) > 0:
                    result.append(word)

    return result


def results():
    """
    Returns results of the game
    """
    grid = generate_grid()
    letters = grid[0] + grid[1] + grid[2]
    letters = [letter.lower() for letter in letters]
    words_from_dict = get_words('f', letters)
    user_words = get_user_words()
    non_dict = get_pure_user_words(user_words, letters, words_from_dict)

    score = len(non_dict)
    for wor in user_words:
        if wor in words_from_dict:
            score += 1

    skipped_answers = []
    for wor in words_from_dict:
        if wor not in user_words:
            skipped_answers.append(wor)

    with open('results.txt', "w", newline='', encoding="utf-8") as file:
        file.write(score)
        file.write(words_from_dict)
        file.write(skipped_answers)
        file.write(non_dict)

    print(score)
    print(words_from_dict)
    print(skipped_answers)
    print(non_dict)
        