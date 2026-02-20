#Slot class for hash table

class HashNode:
    def __init__(self, key = "", data = None):
      self.key = key
      self.data = data

class Hashtable:
    def __init__(self, size):
        self.size  = size
        self.count = 0     
        self.__table = [] 

    def store(self, key, data = None):
        #Fyll i kod här!
        print()

    def search(self, key):
        print()    #Fyll i kod här!
            #...
        # else:
        #     raise KeyError

    def __contains__(self, nyckel): 
        #Fyll i kod här!
        print()

    def __getitem__(self, nyckel):
        # Frivillig uppgift
        print()

    def hashfunction(self, key):
        print()


def hashFunction(item):
    #mid_square_value
    squared = item * item
    
