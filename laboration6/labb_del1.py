class song:
    def __init__(self, track_id, song_id, artist, song_title):
        self.track_id = track_id
        self.song_id = song_id
        self.artist = artist
        self.song_title = song_title

    def __lt__(self, other):
        if self.artist < other.artist or self.song_title < other.song_title:
            return True
        return False
    

def read_file(file_path):
    index_list = []
    
    with open(file_path, "r") as file:
        for row in file:
            item = file.strip().split("<SEP>")
            data.
        


def main():
    