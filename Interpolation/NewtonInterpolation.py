import math
import matplotlib.pyplot as plt
import numpy as np
#import timeit
import Knoten

#func= lambda y: 1+(4/3)*y+(2/3)*math.pow(y,2)

x = Knoten.chebyshevX(-20,20,50)
f = Knoten.f_fromRandomX(x, lambda y: math.exp(y))

#test
#x=[0,1,3]
#f=[1,3,11]

def xf(x,f, a=-1, b=-1, hashmap=None):
    if hashmap and (a,b) in hashmap:
        return hashmap[(a,b)]
    if len(x) == 1:
        return f[0]
    if (a != -1) and (b != -1) and hashmap != None:
        return_value = (xf(x[0:-1],f[0:-1],a,b-1,hashmap)-xf(x[1:],f[1:],a+1,b,hashmap))/(x[0]-x[-1])
        hashmap[(a,b)] = return_value
    else:
        return_value = (xf(x[0:-1],f[0:-1])-xf(x[1:],f[1:]))/(x[0]-x[-1])
    return return_value

def alpha(x,f):
    a = []
    hashmap = {}
    for i in range(2, len(x)+1):
        a += [xf(x[0:i],f[0:i],0,i,hashmap)]
    return a

def omegaNplusOne(x):
    return lambda y: math.prod((y-z) for z in x)

def interpolationsPolynom(x,f):
    a = alpha(x,f)
    return lambda y: f[0]+sum(a[i-1]*omegaNplusOne(x[0:i])(y) for i in range(1,len(x)))

#duration = timeit.timeit(lambda: interpolationsPolynom(x,f), number=1000)
#print(duration)

trueFunction = lambda y: math.exp(y)
p = interpolationsPolynom(x,f)

x_values = np.linspace(-20, 20, 400)

# 3. Y-Werte berechnen (Vektorisierung per Listen-Abstraktion)
y_prod = [trueFunction(x) for x in x_values]
y_sum = [p(x) for x in x_values]

# 4. Plotten
plt.figure(figsize=(10, 6))

plt.plot(x_values, y_prod, label="sin$", color="blue", linewidth=2)
plt.plot(x_values, y_sum, label="p", color="red", linestyle="--")

# Nullstellen von y markieren
plt.ylim(-3,3)
plt.axhline(0, color='black', linewidth=0.5)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()