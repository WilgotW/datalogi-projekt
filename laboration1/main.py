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
        return f"#{self.index} {self.name} - {self.hp}HP"

    def __lt__(self, other):
        if(int(self.hp) == int(other.hp)):
            if(int(self.index) > int(other.index)):
                return True
        elif(int(self.hp) < int(other.hp)):
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
            all_pokemon = rows

        print(all_pokemon)

        pokemon_class_list = []
        for p in all_pokemon:
            new_pokemon = Pokemon(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12])
            pokemon_class_list.append(new_pokemon)
            print(new_pokemon)

        self.pokemon = pokemon_class_list
        return pokemon_class_list

    def get_pokemon_by_index(self, pokemon_index):
        for p in self.pokemon:
            if p.index == pokemon_index:
                return p
        return print("No pokemon found")    
        

    def get_pokemon_by_name(self, pokemon_name):
        for p in self.pokemon:
            if p.name == pokemon_name:
                return p
        return print("No pokemon found")    


def out_of_bounds(pokemon_index, pokedex_count):
    if(pokemon_index > pokedex_count or pokemon_index < 0):
        return True
    return False

def main():
    pokedex = Pokedex("pokemon.csv")

    while True:
        print(
            "_______POKEDEX_______ \n"
            "Vad vill du göra:  \n"
            "1. Sök efter pokemon \n"  
            "2. jämför pokemon \n"
        )
        choice = input()

        if(choice == "1"):
            print(
                "1. Sök med index \n"
                "2. Sök med namn \n"
            )
            choice2 = input()

            print("Önskad pokemon: ")
            pokemon_keyword = input()

            if choice2 == "1":
                if out_of_bounds(int(pokemon_keyword), len(pokedex.pokemon)):
                    return print("Index out of bounds, try again")
                print(pokedex.get_pokemon_by_index(pokemon_keyword))

            elif choice2 == "2":
                print(pokedex.get_pokemon_by_name(pokemon_keyword))

        elif(choice == "2"):
            print("Vilka pokemon vill du jämföra: (index-index): ")
            pokemon_index = (input()).split("-")

            if (out_of_bounds(int(pokemon_index[0]), len(pokedex.pokemon)) or
                out_of_bounds(int(pokemon_index[1]), len(pokedex.pokemon))):
                return print("Index out of bounds, try again")

            pokemon1 = pokedex.get_pokemon_by_index(pokemon_index[0])
            pokemon2 = pokedex.get_pokemon_by_index(pokemon_index[1])

            if(pokemon1 < pokemon2):
                print(str(pokemon2) + " Vann över " + str(pokemon1))
            else:
                print(str(pokemon1) + " Vann över " + str(pokemon2))

main()