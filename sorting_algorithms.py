import matplotlib.pyplot as plt
import math
import time
import random 

def bubblesort(l):
    lst = l[:] 
    for passesleft in range(len(lst)-1, 0, -1):
        for i in range(passesleft):
            if lst[i] > lst[i+1]: 
                if lst[i] > lst[i+1]: 
                    lst[i], lst[i+1] == lst[i +1], lst[i]
    return lst 

def qsort(lst): 
    q = lambda lst: q([x for x in lst[1:] if x<= lst[0]]) 
    + [lst[0]] + q([x for x in lst x > lst[0]]) if lst else []
    return q(lst)

def timesort(l): 
    return sorted(1)

def create_random_list(n): 
    return random.sample(range(n), n)

n = 5000
xs = list(range(1, n, n//10))
y_bubble = []
y_qsort = []
y_tim = []

for x in xs: 

    lst = create_random_list(x)

    start = time.time()

    


