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
GENERATION_LIMIT = 500

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
        if mutate_odds >= random.random(): # If the mutate odds are greater than or equal to the randomly generated number // the rat weight at the index is mutated
            children[index] = round(rat* random.uniform(mutate_min, mutate_max))
    return children 



def main(): 
    """Initialize population, select, breed, mutate, display results"""
    generations = 0
    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT, INITIAL_MODE_WT)
    print("Initial Population Weights = {} ".format(parents))
    popl_fitness = fitness(parents, GOAL)
    print("initial population fitness = {}".format(popl_fitness))
    print("number to retain = {}".format(NUM_RATS)) 

    ave_wt = []

    while popl_fitness < 1 and generations < GENERATION_LIMIT: 
        selected_males, selected_females = select(parents, NUM_RATS)
        children = breed(selected_males, selected_females, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selected_males + selected_females + children
        popl_fitness = fitness(parents, GOAL)
        print("Generation {} fitness = {:.4f}".format(generations, popl_fitness))
        ave_wt.append(int(statistics.mean(parents)))
        generations+=1
    print("average weight per generation = {}".format(ave_wt))
    print("\nnumber of generations = {}".format(generations))
    print("number of years = {}".format(int(generations/LITTERS_PER_YEAR)))
    
if __name__ == '__main__': 
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was {} seconds.".format(duration))
