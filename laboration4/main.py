from bintree import Bintree
from helpers import *

alphabet = "abcdefghijklmnopqrstuvwxyzåäö"

def make_children(word, word_tree):
    word_combinations = []
    _alphabet = str_to_letters(alphabet)
    for l in range(len(word)):
        for i in range(len(_alphabet)):
            new_word = word
            new_word = str_to_letters(new_word)
            new_word[l] = alphabet[i]
            new_word = list_to_str(new_word)

            if (
                new_word 
                not in word_combinations 
                and new_word != word
                and new_word in word_tree
                ):
                word_combinations.append(new_word)
    return word_combinations

def load_words():
    word_tree = Bintree()
    with open("word3.txt", "r", encoding="utf-8") as word_file:
        for row in word_file:
            word = row.strip()
            word_tree.store(word)
    return word_tree
    

def main():
    word_tree = load_words()
    word_combinations = make_children("söt", word_tree)

    for word in word_combinations:
        print(word)

    


main()
