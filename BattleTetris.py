# BattleTetris.py
from TetrisAgent import *
from GA import *

POPULATION_SIZE = 100
GENERATIONS = 5 # I have no idea what a good number is here

def main():
        # GA: Single Population Competitive Coevolution
        # Initialize Initial Population
        population = [GA.random_individual() for i in range(POPULATION_SIZE)]
        # Choose Evaluators (at random?)
        starter = GA(occupied=0.2, holes=0.2, pile=0.2, wells=0.2, completed=0.2)
        eval_agent = TetrisAgent("0", starter)
        # Evaluate all individuals
        # While remaining generations:
            # Select Parents (based on fitness)
            # Produce children:
                # Crossover
                # Mutate
            # select evaluators
            # evaluate children (# rows cleared, points won, or games won)
            # Survivor Selection
        # return most fit individual
        
def play_random():
    # play one game
    a1 = TetrisAgent("1", GA())
    a2 = TetrisAgent("2", GA())
    num_turns = 1
    winner = None
    
    while(num_turns > 0):
        pieces = ["O", "I", "T", "L", "J", "S", "Z"]
        p = pieces[random.randint(0,6)]
        
        a1.set_current_piece(TetrisPiece(p))
        a1.random_move()
        
        a2.set_current_piece(TetrisPiece(p))
        a2.random_move()
        
        # send results to other player
        a1.update(a2.score())
        a2.update(a1.score())
        
        if a1.is_game_over():
            winner = a2.name
            print("{} wins!".format(winner))
            break
        elif a2.is_game_over():
            winner = a1.name
            print("{} wins!".format(winner))
            break
        
        num_turns -= 1
    
    print("a1's board:")
    print(a1.game_board)
    
    print("a2's board:")
    print(a2.game_board)
    print("Final scores: {}: {}, {}:{}".format(a1.name, a1.total_score, a2.name, a2.total_score))
    

if __name__ == "__main__":
    # Don't run this yet, it's pseudocode
    # main()
    play_random()
