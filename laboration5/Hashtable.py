
#Slot class for hash table
class HashNode:
    def __init__(self, key = "", data = None):
        self.key = key
        self.data = data

class Hashtable:
    def __init__(self, size):
        self.size  = size
        self.count = 0     
        self.table = [None] * size #create a list of empty slots
        self.skip = 3

    def store(self, key, data = None):
        store_slot(self.hashtable, key, data)


    def search(self, key):
        hash_value = self.hashFunction(key, self.size)
        
        current_index = hash_value
        while self.table[current_index] is not None:
            if self.table[current_index].key == key:
                return self.table[current_index].data
            
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

    def hashFunction(self, item, hash_size):
        #mid square method
        squared = str(item * item)
        
        hash_value = None
        
        if len(squared) > 2:
            mid_index = len(squared) // 2
            squared = squared[mid_index-1:mid_index+1]

        hash_value = int(squared) % hash_size
        
        return hash_value

def store_slot(hashtable:Hashtable, key, data):
    hash_value = hashtable.hashFunction(key, hashtable.size)

    if hashtable.table[hash_value] is not None:
        hash_value = handleCollision(hashtable, hash_value)
    
    hashtable.table[hash_value] = HashNode(key, data)


def handleCollision(hashtable:Hashtable, index):
    #open addressing 
    new_index = (index + hashtable.skip) % hashtable.size

    if hashtable.table[index] is not None: 
        return handleCollision(hashtable, new_index)

    return new_index

