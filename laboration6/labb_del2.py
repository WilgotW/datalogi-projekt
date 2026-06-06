from mergesort import merge_sort # Antar att du använder Mergesort från del 1
import timeit
# import matplotlib.pyplot as plt # Används för grafen på slutet

class SongWithLength:
    def __init__(self, artist_id, artist_name, song_title, length, year):
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.song_title = song_title
        self.length = float(length) # Gör om strängen till flyttal
        self.year = year

    # Sortera baserat på längd
    def __lt__(self, other):
        return self.length < other.length

def read_song_data(file_path):
    song_list = []
    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            items = row.strip().split('\t')
            # Säkerställ att raden faktiskt har 5 kolumner
            if len(items) == 5:
                # Kolumner: artistid (0), artistnamn (1), sångtitel (2), låtlängd (3), år (4)
                song = SongWithLength(items[0], items[1], items[2], items[3], items[4])
                song_list.append(song)
    return song_list

def method_1(song_list, k):
    """ Upprepade linjärsökningar """
    ignored_keys = set() # Uppslagslista för låtar vi redan har plockat ut
    best_song = None
    
    for _ in range(k):
        max_len = -1
        best_song = None
        
        for song in song_list:
            # Uppgiften tipsade om att konkatenera två strängar för en unik nyckel
            unique_key = song.artist_id + song.song_title 
            
            if unique_key not in ignored_keys and song.length > max_len:
                max_len = song.length
                best_song = song
                
        # Lägg till den längsta vi hittade i detta varv i ignorerings-set:et
        ignored_keys.add(best_song.artist_id + best_song.song_title)
        
    return best_song

def method_2(song_list, k):
    """ Sortera och plocka ut """
    # Måste sortera en Kopia av listan, annars sorteras den för all framtid,
    # vilket gör att nästa testkörning av method_2 blir fusk (redan sorterad).
    list_copy = song_list.copy()
    
    # Kör din mergesort (vi antar att den sorterar i stigande ordning, kortast först)
    merge_sort(list_copy)
    
    # Den k längsta ligger då i slutet av listan.
    # Exempel: 1:a längsta = index -1. k:te längsta = index -k.
    return list_copy[-k]

def main():
    print("Läser in stora låtfilen (ta en klunk kaffe)...")
    song_list = read_song_data("sang_artist_data.txt")
    print(f"Inläsning klar! {len(song_list)} låtar hittades.\n")
    
    # OBS: För felsökning är det smart att byta ut song_list mot song_list[:50000] 
    # tills du vet att allt fungerar, kör sedan med hela miljonen!
    test_list = song_list 
    
    k_values = []
    times_m1 = []
    times_m2 = []
    
    k = 1
    print("k\tMethod 1\tMethod 2")
    # Vi kör upp till k = 40 för att vara säkra på att få med brytpunkten (~20)
    while k <= 40:
        # timeit vill ha en funktion utan parametrar, så vi använder lambda
        t1 = timeit.timeit(stmt = lambda: method_1(test_list, k), number = 1)
        t2 = timeit.timeit(stmt = lambda: method_2(test_list, k), number = 1)
        
        print(f"{k}\t{t1:.4f}s\t\t{t2:.4f}s")
        
        # Spara data för grafen
        k_values.append(k)
        times_m1.append(t1)
        times_m2.append(t2)
        
        k += 4
if __name__ == '__main__':
    main()