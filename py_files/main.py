import math
import random
from functions import sorted_start, salesman_generationFunc, salesman_energyFunc
from visualization import path_visual,animate_paths
from datasets import saleman_dataset
from A_star import tsp_astar

"""
coord=[]
for i in range (10):
   x = random.randint(1, 100)
   y = random.randint(1, 100)
   coord.append((x, y))

"""

dataset = 'berlin52.tsp'
#dataset = 'a280.tsp'
#dataset = 'ch150.tsp'

coord = saleman_dataset(dataset)

#coord = coord[:20]

def simulated_annealing(coord):
    #coord = sorted_start(coord)
    random.shuffle(coord)

    N= len(coord)
    path_history = []

    # сохраняем копию текущего маршрута
    path_history.append(coord.copy())

    #s_coord=[(3, 4), (1, 6), (23, 4)] #координаты значений(городов/атомов)
    #T = 100000           # начальная температура (можно попробовать и 500, и 100)
    T_min = 0.001     # минимальная, при которой завершается отжиг
    alpha = 0.995

    #coord=sorted_start(coord)
    path_visual(coord)

    cur_E = salesman_energyFunc(coord)
    print("start Energy: ",cur_E)

    T=cur_E * 0.1
    no_improve = 0  #количество  неулучшений
    best=cur_E
    b=0.0003
    i=0
    while T > T_min:
        improve = 0
        moves = 0

        for _ in range(500):  # 100 попыток при одной температуре
            new_coord=salesman_generationFunc(coord)
            new_E=salesman_energyFunc(new_coord)
            moves+=1
            delta_E = new_E - cur_E

            if delta_E < 0:
                #print("Improvenemt from ", cur_E, " to", new_E)
                coord=new_coord
                cur_E = new_E
                improve +=1
                # сохраняем копию текущего маршрута
                path_history.append(coord.copy())
                best=new_E

            else:
                probability = math.exp((-delta_E)/T)

                if random.random() < probability:
                    #print("Degradation from ", cur_E, " to", new_E)
                    coord=new_coord
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

        T *= alpha
        """
        T = T / math.log(2 + i)
        i+=1
        if improve == 0:
            no_improve += 1
        else:
            no_improve = 0

        # Reheating, если за 10 кругов нет улучшений
        if no_improve >= 10:
            T =  max(T * 1.5, 50000)
            no_improve = 0
            print(f"Reheating! T={T}")

    print("Best: ",best)

    path_visual(coord)
    animate_paths(path_history)
    return best,coord

"""
best_E,best_coord = simulated_annealing(coord)
for _ in range(10):
    cur_E,cur_coord = simulated_annealing(best_coord)
    if cur_E < best_E:
        best_E = cur_E
        best_coord=cur_coord
print(f"Лучший результат после 10 запусков: {best_E:.2f}")
"""
best,path1=simulated_annealing(coord)

path2,cost=tsp_astar(coord)
print(cost)