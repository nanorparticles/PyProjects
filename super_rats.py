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
    females = sorted_population[:members_per_sex] # first half of the sorted array 
    males = sorted_population[members_per_sex:] # last half of the sorted array
    selected_females = females[-to_retain_by_sex:] # take the top number 
    selected_males = males[-to_retain_by_sex:] # take the top number - parents of next gen 
    return selected_males, selected_females # return the tuple of selected males and females 

#Assume that the weight of each child is lesser or equal to father and more or equal to mother  
def breed(males, females, litter_size): 
    """Crossover genes among weights of a population"""

    random.shuffle(males) # Shuffle the pairings of males and females  
    random.shuffle(females)
    children = []
    for male, female in zip(males, females): # create pairs of males and females 
        for child in range(litter_size): # up to litter size number of children
            child = random.randint(female, male) # each weighing in between female and male 
            children.append(child) # append child to the children array
    return children # return the children 

# A small percentage of the children will experience a mutation 
# Usually this means runts but this can also mean heavier ones that survive 

def mutate(children, mutate_odds, mutate_min, mutate_max):
    """Randomly alter rat weights using input odds and fractional changes"""
    for index, rat in enumerate(children): 
        if mutate_odds >= random.random(): 
            children[index] = round(rat* random.uniform(mutate_min, mutate_max))
    return children 


