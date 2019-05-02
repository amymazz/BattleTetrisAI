# GA.py
import random

class GAIndividual:
    def __init__(self, occupied=0, holes=0, pile=0, wells=0, completed=0): 
        self.occupied_weight = occupied
        self.num_holes_weight = holes
        self.pile_height_weight = pile
        self.well_heights_weight = wells
        self.completed_rows_weight = completed
        self.fitness = 0
        
    def __repr__(self):
        return "(occupied: {:.2f}, holes: {:.2f}, height: {:.2f}, well heights: {:.2f}, completed rows: {:.2f}, fitness: {})".format(self.occupied_weight, 
            self.num_holes_weight, self.pile_height_weight,
            self.well_heights_weight, self.completed_rows_weight, self.fitness)
    
def random_individual():
    return GAIndividual(random.uniform(-1,1), random.uniform(-1,1), 
        random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1))

if __name__ == "__main__":
    print(random_individual())
