def average_rgb(pixels):
    r = [x[0] for x in pixels]
    g = [x[1] for x in pixels]
    b = [x[2] for x in pixels]
    n = len(r)
    return (sum(r)/n, sum(g)/n, sum(b)/n)

print(average_rgb([(0,0,0), (256, 128, 0), (32,64,33)]))

# Unit Test to see if the function works for border case of 0's 
def unit_test_avg(): 
    print('Test average...')
    print(average_rgb([(0,0,0)]) == average_rgb([(0,0,0), (0,0,0)]))

# Unit test to make sure a tuple of ints is returned 

def unit_test_type(): 
    print("Test type..")
    for i in range(3):
        print(type(average_rgb([(1,2,3), (4,5,6)])[i]) == int) # Tells is if every member of the resulting tuple is an int 


unit_test_avg()
unit_test_type()