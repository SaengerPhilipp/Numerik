import numpy as np

def lowerLeft(A,b):
    x=[b[0]/A[0,0]]
    for i in range(1,len(A)):
        x += [(b[i]-np.inner(A[i,0:i],x))/A[i,i]]
    return x

def lowerLeftUnipotent(A,b):
    x = [b[0]]
    for i in range(1, len(A)):
        x += [(b[i] - np.inner(A[i, 0:i], x))]
    return x

def upperRight(A,b):
    x = [b[-1]/A[-1,-1]]
    for i in range(len(A)-2,-1,-1):
        x = np.insert(x,0,(b[i] - np.inner(A[i,i+1:len(A)],x))/A[i,i])
    return x