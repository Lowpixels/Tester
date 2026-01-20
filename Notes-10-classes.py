# Classes and Objects
# Author: Marcus
# 11 December 2025

import random


class Pokemon:
    def __init__(self):
        # Initialize the properties of Pokemon
        self.name = ""
        self.species = ""
        self.type = "normal"
        self.age = 0
        self.level = 1
        print("A pokemon is born!")
        # One out of 4096 should be shiny
        # self.shiny = random.randint(4096)
        if random.randint(0, 4096):
            self.shiny = False
        else:
            self.shiny = True
            print("✨{self.name} is shiny!✨")

    def talk(self):
        """Hear what the pokemon has to say.
        The pokemon says its species name."""
        print(f'{self.name} says, "{self.species}".')

    def stats(self):
        """Display the stats of the Pokemon"""
        print(f"---{self.species}----------")
        print(f"   Name: {self.name}")
        print(f"   Type: {self.type}")
        print(f"   Age:  {self.age}")
        print(f"   Level: {self.level}")
        print("---------------------------")

    def find_something(self, how_many_things=1) -> list[str]:
        """Send pokemon to find something

        Returns:
            a str representing what it found"""
        things = [
            "pinap berry",
            "razz berry",
            "nanab berry",
            "golden razz berry",
            "leftovers",
            "moon stone",
        ]
        found_things = []

        for _ in range(how_many_things):
            found_things.append(random.choice(things))

        return found_things


class Squirtle(Pokemon):
    def __init__(self):
        # Call the superclass constructor explicitly
        super().__init__()
        self.name = "Squirtle"
        self.species = "Squirtle"
        self.type = "water"
        self.has_sunglasses = True

    def water_gun(self):
        """Use the water gun attack."""
        print(f"{self.name} used water gun.")
        # TODO: check to see if it's effective


if __name__ == "__main__":
    # Create a pokemon object
    pokemon_one = Pokemon()
    # View its properties
    print("Pokemon Name:", pokemon_one.name)
    # Change some properties
    pokemon_one.name = "Gary"
    print("Pokemon Name:", pokemon_one.name)
    # Create another pokemon object
    pokemon_two = Pokemon()
    print("Pokemon two's name:", pokemon_two.name)
    # Compare the two pokemon
    if pokemon_one == pokemon_two:
        print("These are the same pokemon?")
    else:
        print("They're individual, distinct pokemon")
    # Check if both objects are pokemon
    if type(pokemon_one) is Pokemon:
        print(f"{pokemon_one.name} is a Pokemon.")
    if type(pokemon_two) is Pokemon:
        print(f"{pokemon_two.name} is a Pokemon.")

    # Have Gary talk
    pokemon_one.talk()
    pokemon_two.talk()
    pokemon_one.stats()
    pokemon_two.stats()

    squirtle_one = Squirtle()
    squirtle_one.talk()
    squirtle_one.water_gun()
