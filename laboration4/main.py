from bintree import Bintree
from LinkedListQ import LinkedListQ
from helpers import *

alphabet = "abcdefghijklmnopqrstuvwxyzåäö"

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
        
def make_children(word, word_tree, visited_words_tree:Bintree, queue_of_words:LinkedListQ, print_ = False):
    word_combinations = []
    _alphabet = str_to_letters(alphabet)

    visited_words_tree.store(word)

    for l in range(len(word)):
        for i in range(len(_alphabet)):
            new_word = word
            new_word = str_to_letters(new_word)
            new_word[l] = alphabet[i]
            new_word = list_to_str(new_word)
            
            if (
                new_word 
                and new_word != word
                and new_word in word_tree
                and new_word not in visited_words_tree
                and new_word not in queue_of_words
                ):
                word_combinations.append(new_word)
    
    if print_:
        for word in word_combinations:
            print(word)

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
    visited_words_tree = Bintree()

    queue_of_words = LinkedListQ()
    target_word = "söt"

    starting_word = "sur"
    queue_of_words.enqueue(starting_word)

    word_found = bfs(queue_of_words, target_word, word_tree, visited_words_tree)
    print(word_found)

#1. Lägg till första ordet i kön. 
#2. Kolla ordet: är det de sökta ordet? Om ja returnera
#3. Hitta barnen med make_children och lägg till alla barn i kön
#4. gå till första barnet -> rätt ord? returna. fel ord? lägg till alla deras barn i kön
#5. fortsätt tills rätta ordet hittas 
def bfs(queue_of_words:LinkedListQ, target_word, word_tree, visited_words_tree):
    current_word = queue_of_words.dequeue()

    print(queue_of_words)
    input()

    if current_word == target_word: 
        return True

    children = make_children(current_word, word_tree, visited_words_tree, queue_of_words)
    for child in children:
        queue_of_words.enqueue(child)
    
    if len(queue_of_words) > 0:
        return bfs(queue_of_words, target_word, word_tree, visited_words_tree)
    
    return False
    



    
def test(word_tree, visited_words_tree):
    make_children("söt", word_tree, visited_words_tree, True)
    print("---")
    make_children("söm", word_tree, visited_words_tree, True)
    print("---")

    print()

main()
