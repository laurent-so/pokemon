import random

class Pokemon:
    def __init__(self, nom, type_pokemon):
        self.nom, self.type_pokemon = nom, type_pokemon
        self.points_de_vie, self.niveau = 100, 1
        self.puissance_attaque, self.defense = 0, 0

    def afficher_infos(self):
        print("Nom:", self.nom)
        print("Points de vie:", self.points_de_vie)
        print("Type:", self.type_pokemon)
        print("Niveau:", self.niveau)
        print("Puissance d'attaque:", self.puissance_attaque)
        print("Défense:", self.defense)

class PokemonNormal(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "normal")
        self.points_de_vie, self.puissance_attaque, self.defense = 90, 20, 10

class PokemonFeu(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "feu")
        self.points_de_vie, self.puissance_attaque, self.defense = 70, 25, 5

class PokemonEau(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "eau")
        self.points_de_vie, self.puissance_attaque, self.defense = 90, 15, 15

class PokemonTerre(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "terre")
        self.points_de_vie, self.puissance_attaque, self.defense = 70, 5, 20

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1, self.pokemon2 = pokemon1, pokemon2

    def verifier_pokemon_en_vie(self):
        if self.pokemon1.points_de_vie <= 0:
            return self.pokemon2
        elif self.pokemon2.points_de_vie <= 0:
            return self.pokemon1
        else:
            return None

    def choisir_aleatoire_attaque(self):
        return random.randint(0, 1)

    def calculer_degats(self, attaquant, defenseur):
        multiplicateurs = {
            "normal": 1,
            "feu": {"eau": 0.5, "terre": 2},
            "eau": {"feu": 2, "terre": 0.5},
            "terre": {"eau": 2, "feu": 0.5}
        }
        multiplicateur = multiplicateurs[attaquant.type_pokemon].get(defenseur.type_pokemon, 1)
        return attaquant.puissance_attaque * multiplicateur

pikachu = PokemonEau("Pikachu")
bulbasaur = PokemonTerre("Bulbasaur")

pikachu.afficher_infos()
bulbasaur.afficher_infos()

combat = Combat(pikachu, bulbasaur)

while not combat.verifier_pokemon_en_vie():
    attaquant = combat.choisir_aleatoire_attaque()
    if attaquant == 0:
        degats = combat.calculer_degats(pikachu, bulbasaur)
        bulbasaur.points_de_vie -= degats
    else:
        degats = combat.calculer_degats(bulbasaur, pikachu)
        pikachu.points_de_vie -= degats

print("\nAttaquant:", combat.pokemon1.nom)
print("Défenseur:", combat.pokemon2.nom)
print("Dégâts infligés:", degats)

combat.pokemon1, combat.pokemon2 = combat.pokemon2, combat.pokemon1

print("\nLe gagnant est:", combat.verifier_pokemon_en_vie().nom)