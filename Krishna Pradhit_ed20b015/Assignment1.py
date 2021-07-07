import numpy as np

# Solution for the 1st question

Y = np.random.rand(100,5)                    #   Y represents the matrix, whose each row is a vector with random elements between 0 and 1
y=  np.random.randint(2,size=(100,5))        #   y represents the matrix, whose each row is a vector with random 0s and 1s only

Sum = 0
i=0
while(i<100):
    Sum = y[i]*np.log2(Y[i]) + (1-y[i])*np.log2(1-Y[i])   # The loop helps in giving the sum
    i=i+1

O = (-1/100)*Sum                            # O is Sum*-1/n 

print(O)                                    # gives the final result






 
