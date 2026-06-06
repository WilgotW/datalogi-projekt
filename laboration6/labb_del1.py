from mergesort import *
from binary_search import *
import timeit
import random

from bintree import Bintree
from LinkedListQ import LinkedListQ
from IndexListQ import IndexListQ
from hashtable import Hashtable

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
    dictionary = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            items = row.strip().split("<SEP>")
            song_object = song(items[0], items[1], items[2], items[3])
            index_list.append(song_object)
            dictionary[items[2]] = song_object
    return index_list, dictionary 
        
def linear_search(lst, target_artist):
    for song in lst:
        if song.artist == target_artist:
            return True
    return False

def average_random_linear_search(lst, iterations=1000):
    random_songs = random.sample(lst, iterations)
    for target in random_songs:
        linear_search(lst, target.artist)

def test_queue(q, lst):
    """Lägger in alla element i kön och plockar därefter ut dem"""
    for item in lst:
        q.enqueue(item) 
    
    # Ändrat från is_empty() till isEmpty()
    while not q.isEmpty():
        q.dequeue()

def test_bintree(tree, lst):
    """Lägger in alla element i binärträdet"""
    for item in lst:
        tree.store(item.artist)
        
def test_hashtable(ht, lst):
    """Lägger in alla element i hashtabellen"""
    for item in lst:
        ht.store(item.artist, item) # Byt till ht.put() beroende på din labb 5-implementation

# -------------------------------------------------------------

def main():
    print("Läser in filen...")
    index_list, dictionary = read_file("unique_tracks.txt")
    print("Inläsning klar!\n")

    test_sizes = [250000, 500000, 1000000]

    for n in test_sizes:
        print(f"--- TESTAR MED n = {n} LÅTAR ---")
        test_list = index_list[:n]
        
        # Sträng för linjärsökningarna (eftersom linear_search jämför med song.artist)
        fake_artist = "ARTIST_SOM_INTE_FINNS_123"
        
        # Ett dummy-song-objekt för binärsökningen (så att __lt__ kan jämföra song mot song)
        fake_song = song("", "", fake_artist, "")
        
        # I - Linjärsökning i osorterad lista (finns ej)
        t_lin_osort = timeit.timeit(stmt=lambda: linear_search(test_list, fake_artist), number=1)
        print(f"I - Linjärsök osorterad: {t_lin_osort:.5f} sekunder")
        
        # III - Linjärsökning efter 1000 slumpvalda element
        t_lin_rand = timeit.timeit(stmt=lambda: average_random_linear_search(test_list, 1000), number=1)
        print(f"III - Linjärsök (snitt 1000): {(t_lin_rand / 1000):.5f} sek/sökning (Total: {t_lin_rand:.2f}s)")

        # IV - Sortera listan med mergesort
        list_to_sort = test_list.copy()
        t_sort = timeit.timeit(stmt=lambda: merge_sort(list_to_sort), number=1)
        print(f"IV - Mergesort: {t_sort:.5f} sekunder")

        # II - Linjärsökning i sorterad lista (finns ej)
        t_lin_sort = timeit.timeit(stmt=lambda: linear_search(list_to_sort, fake_artist), number=1)
        print(f"II - Linjärsök sorterad: {t_lin_sort:.5f} sekunder")

        # V - Binärsökning i sorterad lista (HÄR SKICKAR VI IN fake_song ISTÄLLET)
        t_bin_sort = timeit.timeit(stmt=lambda: binary_search(list_to_sort, fake_song), number=1)
        print(f"V - Binärsök sorterad: {t_bin_sort:.5f} sekunder")
        
        # VI - IndexListQ (OBS: Kan ta jättelång tid på n=1 000 000!)
        idx_q = IndexListQ()
        t_idxq = timeit.timeit(stmt=lambda: test_queue(idx_q, test_list), number=1)
        print(f"VI - IndexListQ: {t_idxq:.5f} sekunder")

        # VII - LinkedListQ
        ll_q = LinkedListQ()
        t_llq = timeit.timeit(stmt=lambda: test_queue(ll_q, test_list), number=1)
        print(f"VII - LinkedListQ: {t_llq:.5f} sekunder")

        # VIII - Binärträd
        tree = Bintree()
        t_tree = timeit.timeit(stmt=lambda: test_bintree(tree, test_list), number=1)
        print(f"VIII - Binärträd: {t_tree:.5f} sekunder")

        # IX - Hashtabell n * 2
        ht2 = Hashtable(n * 2)
        t_ht2 = timeit.timeit(stmt=lambda: test_hashtable(ht2, test_list), number=1)
        print(f"IX - Hashtabell (n*2): {t_ht2:.5f} sekunder")

        # X - Hashtabell n * 1.5
        ht15 = Hashtable(int(n * 1.5))
        t_ht15 = timeit.timeit(stmt=lambda: test_hashtable(ht15, test_list), number=1)
        print(f"X - Hashtabell (n*1.5): {t_ht15:.5f} sekunder")

        print("\n")
   
if __name__ == '__main__':
   main()