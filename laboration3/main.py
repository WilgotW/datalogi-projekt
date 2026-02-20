from bintree import Bintree

def load_swedish_words():
    swedish = Bintree() #all unique words
    with open("word3.txt", "r", encoding="utf-8") as swedish_file:
        for row in swedish_file:
            word = row.strip()
            if word in swedish:
                print(word, end=" ") #skip duplicates
            else:
                swedish.store(word) #add to tree
    print("\n")
    return swedish

def load_english_words(swedish):
    english = Bintree()
    with open("engelska.txt", "r", encoding="utf-8") as english_file:
        for row in english_file:
            words = row.split()
            for word in words: 
                if word in english:
                    pass
                else: 
                    english.store(word)
                    if word in swedish: 
                        print(word, end=" ")
    print("\n")
    return english

def main():
    # tree = make_tree_from_input()
    # search_input(tree)

    swedish = load_swedish_words()
    english = load_english_words(swedish)

main()