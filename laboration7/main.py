import json, re, random

def extract_attack_msg(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    pattern = r"<td><small>(.*?)\."
    return re.findall(pattern, file_content)

class Pokemon:
    def __init__(self, name, id, type, hp, attack, defense, sp_attack, sp_defense, speed, msg, sp_msg):
        self.name = name	
        self.id	= id		
        self.type = type	
        self.hp = hp		
        self.attack = attack	
        self.defense = defense	
        self.sp_attack = sp_attack	
        self.sp_defense = sp_defense	
        self.speed = speed
        self.level = 1
        self.msg = msg
        self.sp_msg = sp_msg

    def __str__(self):
        return str(self.name).capitalize()

    def __lt__(self, other):
        if(int(self.hp) == int(other.hp)):
            if(int(self.id) > int(other.id)):
                return True
        elif(int(self.hp) < int(other.hp)):
            return True
    
        return False

class Pokedex:
    def __init__(self):
        self.pokemon = self.load_pokedex()

    def __str__(self):
        all_pokemon = []
        for p in self.pokemon.values():
            all_pokemon.append(p.name)
        return ", ".join(all_pokemon)
    
    def load_pokedex():
        with open("pokedex.json", "r") as fil:
            pokelist = json.load(fil)

        attack_messages = extract_attack_msg("List_of_moves_mod.html")

        pokedict = {}
        for k in pokelist:
            sp_msg = random.choice(attack_messages)
            msg = random.choice(attack_messages)
            
            english_name = k["name"]["english"]
            pokedict[english_name.lower()] = Pokemon(
                name=english_name, 
                id=k["id"], 
                type=k["type"], 
                hp=k["base"]["HP"], 
                attack=k["base"]["Attack"], 
                defense=k["base"]["Defense"], 
                sp_attack=k["base"]["Sp_Attack"], 
                sp_defense=k["base"]["Sp_Defense"], 
                speed=k["base"]["Speed"], 
                msg=msg, 
                sp_msg=sp_msg
            )

        return pokedict

    def __getitem__(self, key):
        if isinstance(key, str):
            if key.isdigit():
                key = int(key)
            else:
                found_pokemon = self.pokemon.get(key.lower())
                if found_pokemon:
                    return found_pokemon
        
        if isinstance(key, int):
            for p in self.pokemon.values():
                if int(p.id) == key:
                    return p

    def move(self, p1, p2, special = False):
        A = p1.level
        B = p1.sp_attack if special else p1.attack
        C = B
        D = p1.sp_defense if special else p1.defense
        X = 1
        Y = self.type_modifier(p1, p2)
        Z = random.randint(217, 255)
        dmg = (((((((2*A/5+2)*B*C)/D)/50)+2)*X*Y)*Z)/255
        return dmg

    def type_modifier(self, p1: Pokemon, p2: Pokemon):
        attacker_type = p1.type[0]
        defender_types = p2.type

        first_multiplier = self.type_match(attacker_type, defender_types[0])
        second_multiplier = self.type_match(attacker_type, defender_types[1]) if len(defender_types) > 1 and defender_types[1] else 1.0
        
        Y = first_multiplier * second_multiplier

        return Y

def type_match(attacker_type, defender_type):          
    data = {}

    with open('statchart.txt', 'r') as file:
        lines = file.readlines()

    header_line = lines[0].strip()
    types = header_line.split()
    
    for i in range(len(types)):
        types[i] = types[i].lower()

    data_lines = lines[1:]

    for row_index in range(len(data_lines)):
        line = data_lines[row_index].strip()
        
        if not line:
            continue
            
        current_attacker = types[row_index]
        data[current_attacker] = {}
        
        multipliers = line.split()
        
        for col_index in range(len(multipliers)):
            current_defender = types[col_index]
            value = multipliers[col_index]
            
            data[current_attacker][current_defender] = float(value)

    return data[attacker_type.lower()][defender_type.lower()]

def out_of_bounds(pokemon_index, pokedex_count):
    if(pokemon_index > pokedex_count or pokemon_index < 0):
        return True
    return False

def main():
    pokedex = Pokedex()

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

#main()