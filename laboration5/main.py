from Hashtable import * 

def load_hashtable(file_path):

    hash_table = None

    with open(file_path, "r", encoding="utf-8") as file:
        row_count = sum(1 for line in file)

        hash_table = Hashtable(row_count * 2)
        
        file.seek(0)

        for row in file:  
            item = row.strip().split("<SEP>")
            hash_table.store(item[2], item[3])
    
    return hash_table

def main():
    hash_table = load_hashtable("unique_tracks.txt")
    print("loaded table")

    while True:
        print("Enter Key: ")
        key = input()
        response = hash_table.search(key)
        print(response)

if __name__ == '__main__':
    main()