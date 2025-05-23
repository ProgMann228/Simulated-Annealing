from functions import euclidean_distance
import heapq
import math
from visualization import path_visual

"""
def tsp_astar(coord):
    N = len(coord)
    start = 0   #юзаем индексы вместо координат
    visited = []    #для индексрв посещенных городов
    visited.append(start)
    path=[]
    path.append(start)
    heap = [(0, 0, start, visited, path)]  # (f, g, current_city, visited, path)

    while heap:
        f, g, cur, visited, path =  heapq.heappop(heap)

        if len(visited)==N:
            rez_E=g+euclidean_distance(coord[cur],coord[start])
            return path + [start], rez_E  # возвращ путь с индексами
            
        for next_p in range(N):
            if next_p not in visited:
                new_visited=visited.copy()
                new_visited.append(next_p)
                new_g = g + euclidean_distance(coord[cur], coord[next_p])
                
                #эвристическая оценка дальнейшего пути
                if len(new_visited) < N:
                    unvisited = [k for k in range(N) if k not in new_visited]
                    mini = min(euclidean_distance(coord[next_p], coord[k]) for k in unvisited)
                    new_h = mini

                else:
                    new_h =0

                new_f = new_g + new_h
                heapq.heappush(heap, (new_f, new_g, next_p, visited, path + [next_p]))

    return None, float('inf')


"""

def dist_matrix(coord):
    N = len(coord)
    matrix = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dx = coord[i][0] - coord[j][0]
            dy = coord[i][1] - coord[j][1]
            matrix[i][j] = matrix[j][i] = math.sqrt(dx**2 + dy**2)

    return matrix

#функция эвристики где мы учитываем проход по каждой вершине
def nearest_neighbor(unvisited, cur, matrix):
    if not unvisited:
        return 0
    cost = 0
    rem = list(unvisited)
    c = cur  # Текущий город
    while rem:
        next_p = min(rem, key=lambda x: matrix[c][x])
        cost += matrix[c][next_p]
        c = next_p
        rem.remove(next_p)
    return cost

def tsp_astar(coord):
    N = len(coord)
    start = 0
    visited = frozenset([start])
    path = [start]
    matrix=dist_matrix(coord)
    heap = [(0, 0, start, visited, [start])]  # (f, g, current_city, visited, path)

    while heap:
        #print("Текущий размер пирамиды:", len(heap))
        k=0
        f, g, cur, visited, path = heapq.heappop(heap)

        if len(visited) == N:
            # вернуться в начальный город
            rez_E = g + matrix[cur][start]
            full_path=path + [start]
            path_visual([coord[i] for i in full_path])
            return full_path, rez_E

        unvisited = [i for i in range(N) if i not in visited]

        for next_p in unvisited:
            new_g = g + matrix[cur][next_p]
            new_visited = visited | {next_p}
            new_h = nearest_neighbor(unvisited, next_p, matrix)
            new_f = new_g + new_h
            heapq.heappush(heap, (new_f, new_g, next_p, new_visited, path + [next_p]))

    return None, float('inf')

