from bintree import Bintree
from helpers import *

alphabet = "abcdefghijklmnopqrstuvwxyzåäö"

def make_children(word, word_tree, visited_words_tree:Bintree, print_ = False):
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

# Ett av barnen till söt är söm och motsvarande är ett av barnen till söm är söt.

# Om du inte tar hänsyn till redan besökta ord så kan du få oändliga kedjor och aldrig komma fram till någon lösning.

# söt -> söm -> söt -> söm -> söt -> söm -> söt ...
# söt -> söm -> döm -> dum -> döm -> söm -> söt ...
# Spara därför undan redan besökta ord i ytterligare ett binärträd och modifiera makechildren så att enbart barn som inte förekommit tidigare genereras.

# Skapa minst ett fördefinierat testfall där du testar att det redan-besökta-trädet fungerar. Om du exempelvis lägger in ordet söm så borde söt få 9 unika barn istället för 10.

def main():
    word_tree = load_words()
    visited_words_tree = Bintree()

    make_children("söt", word_tree, visited_words_tree, True)
    print("---")
    make_children("söm", word_tree, visited_words_tree, True)
    print("---")

    print()

    


main()
