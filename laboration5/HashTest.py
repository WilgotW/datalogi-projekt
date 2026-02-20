import unittest
from Hashtable import Hashtable

class TestHashtable(unittest.TestCase):

    # OUT: returnerar 1 tom hashtabell (storlek 10), 2 nycklar och 2 värden 
    def setup(self):
        d1 = Hashtable(10)
        # Nycklarna är heltal för att fungera med item * item i hash-funktionen
        k1 = 10  # 10 * 10 = 100. Hash-värde blir 0
        v1 = 1946
        k2 = 30  # 30 * 30 = 900. Hash-värde blir också 0 (Krock!)
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
            d1.search(key1)

    # --- NYA TESTER NEDANFÖR ---

    # TEST: Testa om hash-funktionen returnerar rätt värde
    def test_hashfunction(self):
        d1, key1, key2, value1, value2 = self.setup()
        # För k1 (10): 10*10 = 100. Mittersta siffran är 0. 0 % 10 = 0.
        self.assertEqual(d1.hashFunction(key1, d1.size), 0)

    # TEST: Testa att krockhanteringen (open addressing/skip) fungerar
    def test_collision(self):
        d1, key1, key2, value1, value2 = self.setup()
        
        # Både 10 och 30 hashas till index 0. Detta tvingar fram en krock.
        d1.store(key1, value1)
        d1.store(key2, value2) 
        
        # Sökningen ska kunna hoppa (skip) över krocken och hitta båda
        self.assertEqual(d1.search(key1), value1)
        self.assertEqual(d1.search(key2), value2)

    # TEST: Testa att count uppdateras när vi lägger till nya element
    def test_count(self):
        d1, key1, key2, value1, value2 = self.setup()
        self.assertEqual(d1.count, 0)
        
        d1.store(key1, value1)
        self.assertEqual(d1.count, 1)
        
        d1.store(key2, value2)
        self.assertEqual(d1.count, 2)

    # TEST: Testa att gamla värden skrivs över om samma nyckel används
    def test_overwrite(self):
        d1, key1, key2, value1, value2 = self.setup()
        
        d1.store(key1, "Gammalt Värde")
        d1.store(key1, "Nytt Värde") # Ska skriva över det gamla
        
        self.assertEqual(d1.search(key1), "Nytt Värde")
        self.assertEqual(d1.count, 1) # Count ska EJ öka när vi uppdaterar ett befintligt värde!

if __name__ == '__main__':
    unittest.main()