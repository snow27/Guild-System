from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name in self.pokemon:
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon.pokemon_details())
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str):
        for data in self.pokemon:
            if pokemon_name in data:
                self.pokemon.remove(data)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for name in self.pokemon:
            result += f"- {name}\n"
        return result


