import numpy as np
x = np.array([(np.linspace(1,10,10)), (np.linspace(11,20,10)), (np.linspace(21,30,10)), (np.linspace(31,40,10)), 
              (np.linspace(41,50,10)), (np.linspace(51,60,10)), (np.linspace(61,70,10)), (np.linspace(71,80,10)),
              (np.linspace(81,90,10)), (np.linspace(91,100,10))], dtype= int)
A = np.square(x)
print('The 10x10 Matrix is \n', A, '\n')

B = A%3

div = A[np.where (B==0)]
print('The values divisible by 3 in the 10x10 matrix are: \n', div)
