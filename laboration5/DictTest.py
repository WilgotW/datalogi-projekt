import unittest
from DictionaryWrapper import DictionaryWrapper

class TestStringMethods(unittest.TestCase):

    def setup(self):
        d1 = DictionaryWrapper()
        k1 = "Carl XVI Gustaf"
        v1 = 1946
        k2 = "Region Blekinge"
        v2 = ["Karlshamn", "Karlskrona", "Olofström", "Ronneby", "Sölvesborg"]
        return d1, k1, k2, v1, v2
    
    def test_store1(self):
        d1, key1, key2, value1, value2 = self.setup()
        d1.store(key1, value1)
        self.assertEqual(d1.search(key1), value1)

    def test_store2(self):
        d1, key1, key2, value1, value2 = self.setup()
        d1.store(key1, value1)
        d1.store(key2, value2)
        self.assertEqual(d1.search(key1), value1)
        self.assertEqual(d1.search(key2), value2)

    def test_key_error(self):
        d1, key1, key2, value1, value2 = self.setup()
        with self.assertRaises(KeyError):
            d1.search( key1 )

if __name__ == '__main__':
    unittest.main()