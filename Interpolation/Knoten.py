import random
import math

def f_fromRandomX(numbers, func):
    return [func(x) for x in numbers]

def randomX_beta(a,b,num):
    numbers = set()
    while len(numbers) < num:
        sample = random.betavariate(0.5,0.5)
        numbers.add(a+sample*(b-a))
    return list(numbers)

def randomX_uniform(a,b,num):
    numbers = set()
    while len(numbers) < num:
        numbers.add(random.uniform(a,b))
    return list(numbers)

def chebyshevX(a, b, num):
    numbers = []
    for i in range(0, num):
        number = math.cos((i/num) * math.pi)
        scaled = 0.5 * (a + b) + 0.5 * (b - a) * number
        numbers.append(scaled)
    return numbers

def äquidistantesX(a,b,num):
    return [a + i* ((b-a)/num) for i in range(1,num+1)]