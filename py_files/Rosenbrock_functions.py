import math
import random

import numpy as np


def Rosenbrock_function(vec):
    summ=0
    for i in range(len(vec)-1):
        f = (1-vec[i])**2 + 100*(vec[i+1]-vec[i]**2)**2
        summ+=f
    return summ

def generate_neighbor(vec,bounds=(-5.12, 5.12)):
    vec_new = np.copy(vec)
    if random.random() < 0.7:
        i = np.random.randint(len(vec))  # случайный индекс
        # случайно выбираем значение из интервала
        vec_new[i] += np.random.uniform(-0.5, 0.5)
        vec_new[i] = np.clip(vec_new[i], bounds[0], bounds[1])

    else:
        for i in range(len(vec)):
            vec_new[i] += np.random.uniform(-0.2, 0.2)
            vec_new[i] = np.clip(vec_new[i], bounds[0], bounds[1])

    return vec_new


def Rastrigin_function(vec):
    summ=0
    n=len(vec)
    A=10
    for i in range(n):
        f = (vec[i])**2 -A*np.cos(2*np.pi*vec[i])
        summ+=f
    return A*n + summ

