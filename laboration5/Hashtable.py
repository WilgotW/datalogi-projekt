#Slot class for hash table
class HashNode:
    def __init__(self, key = "", data = None):
        self.key = key #node identifier 
        self.data = data

class Hashtable:
    def __init__(self, size):
        self.size  = size
        self.count = 0     
        self.table = [None] * size #create a list of empty slots
        self.skip = 3 #probing skip number in collision cases

    def store(self, key, data = None):
        store_slot(self, key, data)

    def search(self, key):
        hash_value = self.hashFunction(key, self.size)
        
        current_index = hash_value
        while self.table[current_index] is not None:
            if self.table[current_index].key == key:
                return self.table[current_index].data
            
            print("was taken, skipped 3")
            current_index = (current_index + self.skip) % self.size
            if current_index == hash_value: 
                #looped around the hash
                break

        raise KeyError

    def __contains__(self, key): 
        try:
            self.search(key)
            return True
        except KeyError:
            return False
        

    # def __getitem__(self, nyckel):
    #     # Frivillig uppgift
    #     print()

    def hashFunction(self, key, hash_size):
        #if item is a stirng: convert string to a number 
        if isinstance(key, str):
            string_total = 0
            for char in key:
                string_total = (string_total * 31) + ord(char) #ord() turns a letter into its ASCII number
            key = string_total

        #x(mid square method)
        squared = key * key
        hash_value = squared % hash_size
        
        return hash_value

def store_slot(hashtable:Hashtable, key, data):
    hash_value = hashtable.hashFunction(key, hashtable.size)

    current_index = hash_value

    for i in range(hashtable.size):
        node = hashtable.table[current_index]

        if node is None: 
            hashtable.table[current_index] = HashNode(key, data)
            hashtable.count += 1
            return
        elif node.key == key: 
            #slot is taken, but by the same key we want to store
            node.data = data #overwrite old data
            return #dont increase size
        
        #slot is taken by a different key, handle collision and find a new slot
        current_index = handleCollision(hashtable, current_index)

    raise Exception("Hash table is full")

def handleCollision(hashtable:Hashtable, index): 
    #open addressing (skiping slots). Modulo makes sure wrap around works in the table
    return (index + hashtable.skip) % hashtable.size

