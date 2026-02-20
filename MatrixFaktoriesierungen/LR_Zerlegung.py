import numpy as np
import Gleichungssystem_lösen as lgs

def lr(A):
    p = []
    for i in range(0,len(A)):
        maxRow=i
        for j in range(i,len(A)):
            if A[j,i] > A[maxRow,i]:
                maxRow = j
        p += [maxRow]
        if maxRow != i:
            A[[i,maxRow]] = A[[maxRow,i]]
        A[i+1:,i] /= A[i,i]
        A[i+1:,i+1:] -= np.outer(A[i+1:,i],A[i,i+1:])
    return p

def lrLösen(A,b):
    y = lgs.lowerLeftUnipotent(A,b)
    return lgs.upperRight(A,y)

def lrKomplett(A,b):
    p=lr(A)
    for i in range(0,len(b)):
        if i != p[i]:
            b[i], b[p[i]] = b[p[i]], b[i]
    return lrLösen(A,b)