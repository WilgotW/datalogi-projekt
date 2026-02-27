import unittest
from DictionaryWrapper import DictionaryWrapper
from Hashtable import Hashtable

class TestStringMethods(unittest.TestCase):

    # OUT: returns 1 empty dictionary, 2 keys and 2 values 
    def setup(self):
        d1 = DictionaryWrapper()
        k1 = "Carl XVI Gustaf"
        v1 = 1946
        k2 = "Region Blekinge"
        v2 = ["Karlshamn", "Karlskrona", "Olofström", "Ronneby", "Sölvesborg"]
        return d1, k1, k2, v1, v2
    
    # TEST: store a key in a dictionary and search for it
    def test_store1(self):
        d1, key1, key2, value1, value2 = self.setup()
        d1.store(key1, value1)
        self.assertEqual(d1.search(key1), value1)

    # TEST: store two keys in a dictionary and search for them
    def test_store2(self):
        d1, key1, key2, value1, value2 = self.setup()
        d1.store(key1, value1)
        d1.store(key2, value2)
        self.assertEqual(d1.search(key1), value1)
        self.assertEqual(d1.search(key2), value2)

    # TEST: search for key in empty dictionary                               
    def test_key_error(self):
        d1, key1, key2, value1, value2 = self.setup()
        with self.assertRaises(KeyError):
            d1.search( key1 )

if __name__ == '__main__':
    unittest.main()