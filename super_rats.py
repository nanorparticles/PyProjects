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


