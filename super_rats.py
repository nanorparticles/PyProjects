import time # it's interesting to time genetic algorithms.... 
import random # stochastic 
import statistics # means 

# CONSTANTS: (Weight in Grams)

GOAL = 50000
NUM_RATS = 20
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.01 
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2 
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10 
GENERATIONAL_LIMIT = 500

# ensure even number of rats for breeding pairs 
if NUM_RATS % 2 != 0: 
    NUM_RATS += 1


# This is the programs shopping representative, picks out the rats. 
def populate(num_rats, min_wt, max_wt, mode_wt):
    "Initialize a population with a Triangular distribution of weights"
    return [int(random.triangular(min_wt, max_wt, mode_wt)) for i in range(num_rats)]

def fitness(population, goal):
    "Measure population fitness based on attribute mean vs target mean"
    ave = statistics.mean(population)
    return ave / goal 

def select(population, to_retain):
    """Cull a population to retain only a specified number of members"""
    sorted_population = sorted(population)
    to_retain_by_sex = to_retain //2
    members_per_sex = len(sorted_population)//2
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    return selected_males, selected_females

