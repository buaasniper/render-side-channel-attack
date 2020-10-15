import numpy as np

NN1 = np.random.randint(16,21,size = 55)
CC1 = np.random.randint(16,21,size = 50)

NN2 = np.random.randint(11,16,size = 45)
CC2 = np.random.randint(10,16,size = 50)

NN = np.concatenate((NN1, NN2), axis=0)
CC = np.concatenate((CC1, CC2), axis=0)
np.random.shuffle(NN)
np.random.shuffle(CC)
print(NN)
print(CC)
