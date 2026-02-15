from bintree import Bintree
from LinkedListQ import LinkedListQ
from helpers import *
import sys

alphabet = "abcdefghijklmnopqrstuvwxyzåäö"

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

def make_children(node, word_tree, visited_words_tree:Bintree, queue_of_words:LinkedListQ, print_ = False):
    accepted_words = []

    _alphabet = str_to_letters(alphabet) #All letters in the alphabet in a list

    visited_words_tree.store(node.word) #Mark parent node as visited

    for l in range(len(node.word)):
        for i in range(len(_alphabet)):
            #change one letter of the current word
            new_word = node.word
            new_word = str_to_letters(new_word)
            new_word[l] = alphabet[i]
            new_word = list_to_str(new_word)

            if (
                new_word 
                and new_word != node.word
                and new_word in word_tree
                and new_word not in visited_words_tree
                and ParentNode(new_word, node) not in queue_of_words
                ):
                accepted_words.append(new_word)

    return accepted_words

def main():
    word_tree = load_words() #all valid word combinations
    visited_words_tree = Bintree() #all visited nodes
    queue_of_words = LinkedListQ() #queue of words to be checked

    starting_word = sys.argv[1]
    target_word = sys.argv[2]

    queue_of_words.enqueue(ParentNode(starting_word)) #add the starting word

    node_found = bfs(queue_of_words, target_word, word_tree, visited_words_tree)
    if node_found:
        path = write_chain(node_found, starting_word)
        print(path)
    else:
        print("No path was found")
    
def write_chain(current_node, starting_word, path = []):
    path.append(current_node.word)
    
    if current_node.word != starting_word:
        write_chain(current_node.parent, starting_word, path)    
    else:
        path.reverse()
    return path

def bfs(queue_of_words:LinkedListQ, target_word:str, word_tree:Bintree, visited_words_tree:Bintree):   
    while not queue_of_words.isEmpty():
        current_node = queue_of_words.dequeue()

        if current_node.word == target_word:
            return current_node
        
            #get all children that have not been searched.
        children = make_children(current_node, word_tree, visited_words_tree, queue_of_words)

        for child in children:
            #add all children to the queue
            queue_of_words.enqueue(ParentNode(child, current_node))
    return None

def bfs_recursive(queue_of_words:LinkedListQ, target_word:str, word_tree:Bintree, visited_words_tree:Bintree):   
    current_node = queue_of_words.dequeue() #remove current visited node from queue

    #check if the current searched node is the target
    if current_node.word == target_word: 
        return current_node 
    
    #get all children that have not been searched.
    children = make_children(current_node, word_tree, visited_words_tree, queue_of_words)

    for child in children:
        #add all children to the queue
        queue_of_words.enqueue(ParentNode(child, current_node))
    
    if len(queue_of_words) > 0:
        return bfs(queue_of_words, target_word, word_tree, visited_words_tree)
    
    return False
    

def load_words():
    word_tree = Bintree()
    with open("word3.txt", "r", encoding="utf-8") as word_file:
        for row in word_file:
            word = row.strip()
            word_tree.store(word)
    return word_tree

main()
