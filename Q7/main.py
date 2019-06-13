import os

A = (0,16,32,64,128,155,12,8,55,56)
B=[3 ,4,1,37,21,18,23,21,27,22,43,21]
#print(A[::6])
#print([A[2] for i in A if A[1]==32])
#print([i for i in A if (A[i]%5==1)])

print(sorted([i+1 for i in B if (i%6==0) and i in B[::6]]))

