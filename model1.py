import numpy as np
import matplotlib.pyplot as plt

maxAge = 36500

birthRate = 1000
certainDeathAge = 80*365
simulationLength = 2*certainDeathAge

stateVector = np.random.randint(0,2000,size=maxAge)

fig, ax = plt.subplots(1)
for count in range(simulationLength):
    #ax.scatter(count,stateVector,)
    pass

fig.savefig('figures/model1.pdf')


