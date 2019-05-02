# GA.py
import random

class GAIndividual:
    def __init__(self, attr):
        """ Initialize from array of values """
        self.occupied_weight = attr[0]
        self.num_holes_weight = attr[1]
        self.pile_height_weight = attr[2]
        self.well_heights_weight = attr[3]
        self.completed_rows_weight = attr[4]
        self.fitness = 0
        
    def __repr__(self):
        return "(occupied: {:.2f}, holes: {:.2f}, height: {:.2f}, well heights: {:.2f}, completed rows: {:.2f}, fitness: {})".format(self.occupied_weight, 
            self.num_holes_weight, self.pile_height_weight,
            self.well_heights_weight, self.completed_rows_weight, self.fitness)
            
    def to_array(self):
        return [self.occupied_weight, self.num_holes_weight, self.pile_height_weight,
            self.well_heights_weight, self.completed_rows_weight]
    
def random_individual():
    return GAIndividual([random.uniform(-1,1), random.uniform(-1,1), 
        random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)])

if __name__ == "__main__":
    print(random_individual())
