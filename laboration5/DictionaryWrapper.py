
class DictionaryWrapper():
    def __init__(self):
        self.dictionary = {}

    def store(self, key, data=None):
        self.dictionary[key] = data

    def search(self, key):
        return self.dictionary[key]
    
    def __contains__(self, key):
        return key in self.dictionary
    
    def __getitem__(self, key):
        return self.search(key)
    