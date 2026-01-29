from bintree import Bintree

def make_tree_from_input():
    tree = Bintree()
    data = input().strip()
    while data != "#":
        tree.store(data)
        data = input().strip()
    return tree

def search_input(tree):
    findme = input().strip()
    while findme != "#":
        if findme in tree:
            print(findme, "found")
        else:
            print(findme, "not found")
        findme = input().strip()

def main():
    tree = make_tree_from_input()
    search_input(tree)

main()