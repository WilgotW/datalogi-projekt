from mergesort import merge_sort 
import timeit

class Song:
    def __init__(self, artist_id, artist_name, song_title, length, year):
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.song_title = song_title
        self.length = float(length)
        self.year = year

    def __lt__(self, other):
        return self.length < other.length

def read_song_data(file_path):
    song_list = []
    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            items = row.strip().split('\t')
            if len(items) == 5:
                song = Song(items[0], items[1], items[2], items[3], items[4])
                song_list.append(song)
    return song_list

#utan sortering. hittar den k:te längsta låten 
def method_1(song_list, k):
    ignored_keys = [] #ignorera redan tagna låtar. 
    longest_song = None
    
    for _ in range(k):
        max_len = -1
        longest_song = None
        
        for song in song_list:
            unique_key = song.artist_id + song.song_title 
            
            if unique_key not in ignored_keys and song.length > max_len:
                max_len = song.length
                longest_song = song
                
        ignored_keys.append(longest_song.artist_id + longest_song.song_title)
        
    return longest_song

#sorterar alla låtar i ordning av längd or returnerar k:te längsta låten
def method_2(song_list, k):
    list_copy = song_list.copy()
    
    merge_sort(list_copy)

    return list_copy[-k] #-k då listan går från kortast till längst 

def main():
    print("Läser in låtfilen")
    song_list = read_song_data("sang_artist_data.txt")

    test_list = song_list 
    
    k_values = []
    times_m1 = []
    times_m2 = []
    
    k = 1
    print("k      Method 1.    Method 2")
    while k <= 30:
        t1 = timeit.timeit(stmt = lambda: method_1(test_list, k), number = 1)
        t2 = timeit.timeit(stmt = lambda: method_2(test_list, k), number = 1)
        
        print(f"{k}\t{t1:.4f}s\t\t{t2:.4f}s")
         
        k_values.append(k)
        times_m1.append(t1)
        times_m2.append(t2)
        
        k += 1
        
if __name__ == '__main__':
    main()