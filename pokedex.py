import csv
import pokemon
import random

class Pokedex:

    __slots__ = ['__pokemon_list']

    def __init__(self):
        
        self.__pokemon_list = []
    
    def load(self,filename):

        with open(filename) as file:
            csvreader = csv.reader(file,delimiter=',')
            next(csvreader)
            for line in csvreader:
                name = line[0]
                name = pokemon.Pokemon(line[0],line[1],line[2],line[3])
                self.__pokemon_list += [name]
        return self.__pokemon_list
    
    def get_pokemon_list(self):
        return self.__pokemon_list
    
    def create_two_parties(self):
        
        party1 = set()
        party2 = set()
        random.shuffle(self.__pokemon_list)
        

        for _ in range(6):
            a_pokemon = self.__pokemon_list.pop()
            party1.add(a_pokemon)
        for _ in range(6):
            a_pokemon = self.__pokemon_list.pop()
            party2.add(a_pokemon)
        return party1,party2




# p = Pokedex()
# p.load('data/pokemon.csv')
# print(p.get_pokemon_list())
# print(p.create_two_parties())
      




