import pokedex
import pokemon
import csv



def battle (party1,party2):

    round_number = 1
    

    while len(party1) != 0 or len(party2)!= 0:

        print('Round:',round_number)
        
        print('Party 1:','<',party1,'>')
        print('Party 2:','<',party2,'>')

        pokemon1 = party1.pop()
        pokemon2 = party2.pop()
        print(pokemon1)
        print(pokemon2)
        
            
        if pokemon1 == pokemon2:
            print('Battle Concluded in a Draw')
            print('Returning Pokemon to Party')
            party1.add(pokemon1)
            party2.add(pokemon2)
            round_number+=1
            input('Hit enter to battle again')
        
        if pokemon1 > pokemon2:
            print(pokemon1,'has won the round over',pokemon2)
            party1.add(pokemon1)
            pokemon2.lose_round(pokemon1.get_damage_points())
            party2.add(pokemon2)
            round_number+=1
            if pokemon2.is_fainted() == True:
                print(pokemon2,'has fainted')
                party2.remove(pokemon2)
            input('Hit enter to battle again')
            
            
        
        if pokemon1 < pokemon2:
            print(pokemon2,'has won the round over',pokemon1)
            party2.add(pokemon2)
            pokemon1.lose_round(pokemon2.get_damage_points())
            party1.add(pokemon1)
            round_number+=1
            if pokemon1.is_fainted() == True:
                print(pokemon1,'has fainted')
                party1.remove(pokemon1)
            input('Hit enter to battle again')
            
    
        
        

        if len(party1) < 1:
            print('party 2','has beaten party 1 after',round_number,'rounds')
            break
        if len(party2) < 1 :
            print('party 1','has beaten party 2 after',round_number,'rounds')
            break
        

def main():

    pokies = pokedex.Pokedex()
    (pokies.load('data/pokemon.csv'))
    party1 = pokies.create_two_parties()[0]
    party2 = pokies.create_two_parties()[1]

    battle(party1,party2)




if __name__=='__main__':
    main()






            





