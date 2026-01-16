import csv

class Pokemon:
    def __init__(self, index, name, type1, type2, total, hp, attack, defence, special_attack, special_defence, speed, generation, legendary):
        self.index = index
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.special_attack = special_attack
        self.special_defefence = special_defence
        self.speed = speed
        self.generation = generation
        self.legendary = legendary
    def __str__(self):
        return self.name + ": " + self.type1
    def __lt__(self, other):
        if(self.hp < other.hp):
            return True
        if(self.index < other.index):
            return True
        return False
    
class Pokedex:
    def __init__(self, pokemon_csv):
        self.pokemon = []
        self.load_pokedex(pokemon_csv)

    def __str__(self):
        all_pokemon = ""
        for p in self.pokemon: 
            all_pokemon += (p.name + ", ")
        return all_pokemon

    def load_pokedex(self, pokemon_csv):
        all_pokemon = [] #alla pokemon från csv filen lagras här
        with open(pokemon_csv) as file:
            csvreader = csv.reader(file)
            rows = []
            for row in csvreader:
                rows.append(row)
            # Ett par tester
            if rows[0][1] != "Name": print("Test misslyckades. Förväntade mig 'Name' men fick", rows[0][1], " i raden:\n\t", rows[0])
            if rows[1][1] != "Bulbasaur": print("Test misslyckades. Förväntade mig 'Bulbasaur' men fick", rows[1][1], " i raden:\n\t", rows[1])
            all_pokemon = rows;

        pokemon_class_list = []
        for p in all_pokemon:
            new_pokemon = Pokemon(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12])
            pokemon_class_list.append(new_pokemon)
        self.pokemon = pokemon_class_list
        return pokemon_class_list
    
    def get_pokemon_by_index(self, pokemon_index):
        for p in self.pokemon:
            if p.index == pokemon_index:
                return p
            
    def get_pokemon_by_name(self, pokemon_name):
        for p in self.pokemon:
            if p.name == pokemon_name:
                return p
            
def main():
    pokedex = Pokedex("pokemon.csv")
    print(pokedex)

    while True:
        print("_______POKEDEX_______")
        print("Vad vill du göra: ")
        print("1. Sök efter pokemon")
        choice = input()
        if(choice == "1"): 
            print("1. Sök med index")
            print("2. Sök med namn")
            choice2 = input()

            print("input: ")
            keyword = input()
            
            if choice2 == "1":
                print(pokedex.get_pokemon_by_index(keyword))
            elif choice2 == "2":
                print(pokedex.get_pokemon_by_name(keyword))

main() 

