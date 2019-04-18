# GA.py
import random

class GA:
    def __init__(self, occupied=0, holes=0, pile=0, wells=0, completed=0): 
        self.occupied_weight = occupied
        self.num_holes_weight = holes
        self.pile_height_weight = pile
        self.well_heights_weight = wells
        self.completed_rows_weight = completed
        
    def normalize(self):
        """ Normalizes the weights """
        x = self.occupied_weight + self.num_holes_weight \
            + self.pile_height_weight + self.well_heights_weight \
            + self.completed_rows_weight
        self.occupied_weight /= x
        self.num_holes_weight /= x
        self.pile_height_weight /= x
        self.well_heights_weight /= x
        self.completed_rows_weight /= x
        return
    
def random_individual(self):
    individual = GA(random.random(), random.random(), random.random(), \
                    random.random(), random.random())
    individual.normalize()
    return individual
