import math
import random
import numpy as np
from Rosenbrock_functions import Rosenbrock_function,Rastrigin_function, generate_neighbor
from visualization import func_visualize


point = np.random.uniform(-5, 5, size=2)

def simulated_annealing(point):

    dim = 3
    T = 1000000           # начальная температура (можно попробовать и 500, и 100)
    T_min = 0.0001     # минимальная, при которой завершается отжиг
    alpha = 0.999

    cur_E = Rosenbrock_function(point)
    print("start Energy: ",cur_E)

    T=cur_E * 0.1
    no_improve = 0  #количество  неулучшений
    best_func=cur_E
    best_point=point

    b=0.0003
    i=0
    while T > T_min:
        improve = 0
        moves = 0

        for _ in range(100):  # 100 попыток при одной температуре
            new_point=generate_neighbor(point)
            new_E=Rosenbrock_function(new_point)
            moves+=1
            delta_E = new_E - cur_E

            if delta_E < 0:
                #print("Improvenemt from ", cur_E, " to", new_E)
                point=new_point
                cur_E = new_E
                improve +=1
                # сохраняем копию текущего маршрута
                best_func=new_E
                best_point=point

            else:
                probability = math.exp((-delta_E)/T)

                if random.random() < probability:
                    #print("Degradation from ", cur_E, " to", new_E)
                    point=new_point
                    cur_E=new_E
                    improve += 1

        # Охлаждение
        """
        if moves > 0:
            success = improve / moves
        else:
            success=0

        if success < 0.2:
            alpha = min(alpha + 0.0005, 0.999)
        elif success > 0.5:
            alpha = max(alpha - 0.0005, 0.98)
"""
        T *= alpha
        """
        T = T / math.log(2 + i)
        i+=1
        if improve == 0:
            no_improve += 1
        else:
            no_improve = 0
"""
    #нагреваем  если за 10 кругов нет улучшений
        if no_improve >= 10:
            T =  max(T * 1.5, 50000)
            no_improve = 0
            print(f"Reheating! T={T}")

    #print("Best: ",best_func)

    return best_func,best_point

"""
best_E,best_coord = simulated_annealing(coord)
for _ in range(10):
    cur_E,cur_coord = simulated_annealing(best_coord)
    if cur_E < best_E:
        best_E = cur_E
        best_coord=cur_coord
print(f"Лучший результат после 10 запусков: {best_E:.2f}")
"""
func,point=simulated_annealing(point)
print(func,point)

func_visualize(Rosenbrock_function,point)