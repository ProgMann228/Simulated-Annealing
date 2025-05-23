import math
import random

def euclidean_distance(p1, p2):
    dist= math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    return dist

"""
#тупо меняю местами два рандомных
def salesman_generationFunc(s_coord):
    new_coord=s_coord.copy()
    i, j = random.sample(range(len(s_coord)), 2)
    new_coord[i], new_coord[j] = new_coord[j], new_coord[i]
    return new_coord

#меняю местами два рандомных с инверсией
def salesman_generationFunc(s_coord):
    new_coord=s_coord.copy()
    i, j = sorted(random.sample(range(len(s_coord)), 2))
    new_route = route[:i] + route[i:j][::-1] + route[j:]
    return new_coord

#перемещаю один в др место
def salesman_generationFunc(s_coord):
    new_coord=s_coord.copy()
    p = new_coord.pop(random.randint(0, len(new_coord) - 1))
    new_coord.insert(random.randint(0, len(new_coord)), p)
    return new_coord

#случайно перемешиваю части
def salesman_generationFunc(s_coord):
    new_coord=s_coord.copy()
    i, j = sorted(random.sample(range(len(new_coord)), 2))
    sub = new_coord[i:j]
    random.shuffle(sub)
    new_coord[i:j] = sub
    return new_coord

"""
#случайно два с инверсией + еще один переставляю
def salesman_generationFunc(s_coord):
    new_coord=s_coord.copy()
    if random.random() < 0.7:  # 70% chance для инверсии
        i, j = sorted(random.sample(range(len(new_coord)), 2))
        new_coord[i:j] = reversed(new_coord[i:j])
    if random.random() < 0.5:  # 50% chance для перестановки
        p = new_coord.pop(random.randint(0, len(new_coord) - 1))
        new_coord.insert(random.randint(0, len(new_coord)), p)
    if random.random() < 0.3:  # 30% chance для сдвига
        city = new_coord.pop(random.randint(0, len(new_coord) - 1))
        new_coord.insert(random.randint(0, len(new_coord)), city)
    return new_coord


def salesman_energyFunc(new_coord):
    summ=0.0
    prev_point=new_coord[0]
    i=1
    while i<(len(new_coord)):
        cur_point=new_coord[i]
        summ+=euclidean_distance(cur_point,prev_point)
        i+=1
    summ+=euclidean_distance(new_coord[0],new_coord[-1])
    return summ

def sorted_start(coord):
    start=coord[0]
    unvisited = coord[1:]
    path=coord.copy()
    path.append(start)

    while len(unvisited)>0:
        mini = float('inf')
        for p in unvisited:
            dist=euclidean_distance(p,start)
            if(dist<mini):
                mini=dist
                next=p
        start = next
        unvisited.remove(next)
    return path




