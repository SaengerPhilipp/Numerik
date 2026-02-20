import numpy as np
import Gleichungssystem_lösen as lgs

def lr(A):
    for i in range(0,len(A)):
        A[i+1:,i] /= A[i,i]
        A[i+1:,i+1:] -= np.outer(A[i+1:,i],A[i,i+1:])

def lrLösen(A,b):
    y = lgs.lowerLeftUnipotent(A,b)
    return lgs.upperRight(A,y)

def lrKomplett(A,b):
    lr(A)
    return lrLösen(A,b)