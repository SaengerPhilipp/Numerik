import math
import matplotlib.pyplot as plt
import numpy as np
import timeit
import Knoten

#Test:
#x = [-2*math.pi, -math.pi, -(1/2)*math.pi, 0, (1/2)*math.pi, math.pi, 2*math.pi]
#f = [0,0,-1,0,1,0,0]

x = Knoten.äquidistantesX(-20,20,100)
f = Knoten.f_fromRandomX(x, lambda y: math.exp(y))

def weigths(x):
    lamda = []
    for j in range(0,len(x)):
        lamdaj = 1
        for k in range(0,len(x)):
            if k != j:
                lamdaj *= 1/(x[j]-x[k])
        lamda += [lamdaj]
    return lamda

def omegaNplusOne(x):
    return lambda y: math.prod((y-z) for z in x)

def interpolationsPolynom(x,f):
    lamdajs = weigths(x)
    return lambda y: omegaNplusOne(x)(y)*sum((f[j]/(y-x[j]))*lamdajs[j] for j in range(0,len(x)))

duration = timeit.timeit(lambda: interpolationsPolynom(x,f), number=1000)
print(duration)

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
