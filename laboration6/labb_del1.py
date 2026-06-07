from mergesort import *
from binary_search import *
import timeit
import random

from bintree import Bintree
from LinkedListQ import LinkedListQ
from IndexListQ import IndexListQ
from hashtable import Hashtable

class Song:
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
    dictionary = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            items = row.strip().split("<SEP>")
            song_object = Song(items[0], items[1], items[2], items[3])
            index_list.append(song_object)
            dictionary[items[2]] = song_object
    return index_list, dictionary 
        
def linear_search(song_list, target_artist):
    for song in song_list:
        if song.artist == target_artist:
            return True
    return False

def average_random_linear_search(song_list, iterations=1000):
    random_songs = random.sample(song_list, iterations)
    for target in random_songs:
        linear_search(song_list, target.artist)

def test_queue(q, lst):
    for item in lst:
        q.enqueue(item) 
    
    while not q.isEmpty():
        q.dequeue()

def test_bintree(tree, lst):
    for item in lst:
        tree.store(item.artist)
        
def test_hashtable(ht, lst):
    for item in lst:
        ht.store(item.artist, item) 


def main():
    index_list, dictionary = read_file("unique_tracks.txt")

    test_sizes = [250000, 500000, 1000000]

    for n in test_sizes:
        test_list = index_list[:n]
        
        fake_artist = "fake_artist"
        fake_song = Song("", "", fake_artist, "")
        
        #1.Linjärsök osorterad, kommer söka hela listan, O(n)
        t_lin_osort = timeit.timeit(stmt=lambda: linear_search(test_list, fake_song), number=1)
        print(f"I - Linjärsök osorterad: {t_lin_osort:.5f} sekunder")
        
        #3. Linjärsökning efter 1000 slumpvalda element, O(n)
        t_lin_rand = timeit.timeit(stmt=lambda: average_random_linear_search(test_list, 1000), number=1)
        print(f"III - Linjärsök (snitt 1000): {(t_lin_rand / 1000):.5f} sek/sökning (Total: {t_lin_rand:.2f}s)")

        #4. sortera med merge sort, O(n log n)
        t_sort = timeit.timeit(stmt=lambda: merge_sort(test_list.copy()), number=1)
        print(f"IV - Mergesort: {t_sort:.5f} sekunder")

        # skapa sorterade listan, O(n log n)
        sorted_list = merge_sort(test_list.copy())

        #2. Linjärsökning i sorterad lista, O(n)
        t_lin_sort = timeit.timeit(stmt=lambda: linear_search(sorted_list, fake_song), number=1)
        print(f"II - Linjärsök sorterad: {t_lin_sort:.5f} sekunder")

        #5. Binärsökning i sorterad lista, O(log n)
        t_bin_sort = timeit.timeit(stmt=lambda: binary_search(sorted_list, fake_song), number=1)
        print(f"V - Binärsök sorterad: {t_bin_sort:.5f} sekunder")
        
        #6. IndexListQ, lägg in element med kö, O(n^2)
        idx_q = IndexListQ()
        t_idxq = timeit.timeit(stmt=lambda: test_queue(idx_q, test_list), number=1)
        print(f"VI - IndexListQ: {t_idxq:.5f} sekunder")

        #7. LinkedListQ, O(n)
        ll_q = LinkedListQ()
        t_llq = timeit.timeit(stmt=lambda: test_queue(ll_q, test_list), number=1)
        print(f"VII - LinkedListQ: {t_llq:.5f} sekunder")

        #8. Binärträd, O(n log n)
        tree = Bintree()
        t_tree = timeit.timeit(stmt=lambda: test_bintree(tree, test_list), number=1)
        print(f"VIII - Binärträd: {t_tree:.5f} sekunder")

        #9. Hashtabell n*2, O(n)
        ht2 = Hashtable(n * 2)
        t_ht2 = timeit.timeit(stmt=lambda: test_hashtable(ht2, test_list), number=1)
        print(f"IX - Hashtabell (n*2): {t_ht2:.5f} sekunder")

        #10. Hashtabell n*1.5, O(n)
        ht15 = Hashtable(int(n * 1.5))
        t_ht15 = timeit.timeit(stmt=lambda: test_hashtable(ht15, test_list), number=1)
        print(f"X - Hashtabell (n*1.5): {t_ht15:.5f} sekunder")

        print("\n")
   
if __name__ == '__main__':
   main()