from mergesort import *
from binary_search import *

class song:
    def __init__(self, track_id, song_id, artist, song_title):
        self.track_id = track_id
        self.song_id = song_id
        self.artist = artist
        self.song_title = song_title

    def __lt__(self, other):
        if self.artist != other.artist:
            return self.artist < other.artist
        else:
            return self.song_title < other.song_title

def read_file(file_path):
    index_list = []
    dictorionary = {}
    with open(file_path, "r") as file:
        for row in file:
            items = row.strip().split("<SEP>")

            song_object = song(items[0], items[1], items[2], items[3])
            index_list.append(song_object)
            dictorionary[items[2]] = song_object

    return index_list, dictorionary
        

def sort_test(sorted_list):
    s = 0
    for i in range(len(sorted_list) - 1):
        s += sorted_list[i+1] < sorted_list[i]
    if s == 0:
        print("list is sorted")
    else:
        print("list is not sorted")



def binary_search_test():
    #Läs in listan
    indata = input().strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()

def main():
    index_list, dictorionary = read_file("unique_tracks.txt")

    reduced_list = index_list[:30] #take the first 30 elements. 
    sorted_list = merge_sort(reduced_list) #sort the list
    sort_test(sorted_list) #test if list is sorted

    binary_search_test()

    
if __name__ == '__main__':
   main()