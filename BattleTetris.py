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
    agents = [ TetrisAgent("1", GA()), TetrisAgent("2", GA()) ]
    num_turns = 1
    loser = None
    
    while(num_turns > 0):
        p = get_random_piece()
        
        for a in agents:
            a.set_current_piece(p)
            a.random_move()
            
        # send results to other player
        agents[0].vs(agents[1].score())
        agents[1].vs(agents[0].score())
        
        for a in agents:
            if a.board.is_game_over():
                loser = a
                break
        
        num_turns -= 1
    
    print(agents[0].board)
    print(agents[1].board)
    

if __name__ == "__main__":
    # Don't run this yet, it's pseudocode
    # main()
    play_random()
