#Ability to get a odd number by rolling a dice
import numpy as np
def uniform(n, m):
    return np.random.randint(1, n+1, size = m)
no = 0   #variable for storing number of event occurence
for i in range(100000): #repetitions
    die = uniform(6,1)  #experiment
    if die == 1 or die == 3 or die==5: #Event
        no = no + 1
e=(no/100000) #probability estimate by Monte Carlo
print('The probability as given by the Monte Carlo simulation is ',e)