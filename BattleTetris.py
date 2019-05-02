# BattleTetris.py
from TetrisAgent import *
from GA import *
import random
import sys

POPULATION_SIZE = 10
GENERATIONS = 1 # I have no idea what a good number is here

pieces = ["O", "I", "T", "L", "J", "S", "Z"]

def evolve():
        """ GA: Single Population Competitive Coevolution """
        gen = 0
        # num_parents = int(POPULATION_SIZE / 10)
        num_parents = 4
        num_children = int(POPULATION_SIZE * 0.6 )
        output = open("output.txt", "w")
        
        # Initialize Population
        population = [random_individual() for i in range(POPULATION_SIZE)]
        output.write("Starting population: {}\n".format(population))
        
        while gen < GENERATIONS:
            output.write("Generation {}:".format(gen))
            sys.stdout.flush()
            # Evaluate
            random.shuffle(population)
            tournament(population)
            # print("Rankings:")
            # for p in population:
            #     print(p.fitness)
            
            # Select Parents: top 10%
            rank = sorted(population, key=lambda p: p.fitness) # sort by fitness
            rank.reverse()
            output.write("Rankings: {}\n".format(rank))
            parents = rank[0:num_parents]
            
            # Produce children:
            children = []
            for c in range(num_children):
                # Crossover 60% of population
                # Mutate 1%
                
                # temp:
                children.append(random_individual())
                continue

            # Survivor Selection
            population = parents + children
            gen += 1
            
        # return most fit individual
        population = sorted(population, key=lambda p: p.fitness)
        output.write("\nMost fit individual: {}".format(population[POPULATION_SIZE-1]))
        output.close()
        
        return population[POPULATION_SIZE-1]
        
def tournament(base_population, round=0, winners=None):
    """ Single elimination tournament, updates population fitness values """
    # winners is a list of indices into base_population
    if winners is None:
        # round 0: everyone's a winner!
        winners = [i for i in range(len(base_population))]
    elif len(winners) == 1:
        # tournament complete
        base_population[winners[0]].fitness = round
        return
    
    print("Tournament {}".format(round))
    print("Last Round's Winners: {}".format(winners))
    # fitness = how many rounds won, updated on loss
    new_winners = []
    r = 1
    for i in range(0, len(winners), 2):
        if i < (len(winners)-1):
            a1 = TetrisAgent(str(i), base_population[winners[i]])
            a2 = TetrisAgent(str(i+1), base_population[winners[i+1]])
            # print("Battle {}: {} vs. {}".format(r, a1, a2))
            print("Battle {}:".format(r))
            sys.stdout.flush()
            winner = play_game(a1, a2)
            if winner == a1:
                new_winners.append(winners[i]) # go on to next round
                print("\tWinner: {}\n".format(winners[i]))
                base_population[winners[i+1]].fitness = round
            else:
                new_winners.append(winners[i+1]) # go on to next round
                print("\tWinner: {}\n".format(winners[i+1]))
                base_population[winners[i]].fitness = round
        else:
            new_winners.append(winners[i]) # free pass for odd numbers
        r+= 1
    
    tournament(base_population, round+1, new_winners)
    return
    
def next_piece():
    global pieces
    return pieces[random.randint(0,6)]
    
def play_game(a1, a2):
    """ Agent 1 and Agent 2 play one game, returns the winner """
    
    while True:
        p = next_piece()
        
        a1.set_current_piece(TetrisPiece(p))
        a1.best_move()
        
        a2.set_current_piece(TetrisPiece(p))
        a2.best_move()
        
        # send results to other player
        a1.update(a2.score())
        a2.update(a1.score())
        
        # In the event of a tie, it favors a2, but since any given individual 
        # is unlikely to be a2 every time, I'm leaving it.
        if a1.is_game_over():
            return a2
        elif a2.is_game_over():
            return a1
    return

def play_random():
    # play one game
    a1 = TetrisAgent("1", GAIndividual())
    a2 = TetrisAgent("2", GAIndividual())
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
    evolve()
    
    # play_random()
    
    # a1 = TetrisAgent("1", random_individual())
    # a2 = TetrisAgent("2", random_individual())
    # print("{}".format(a1))
    # print("{}".format(a2))
    # winner = play_game(a1, a2)
    # print("{} wins!".format(winner.name)) 
