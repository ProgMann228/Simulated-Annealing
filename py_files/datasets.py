import gzip
import numpy as np

def saleman_dataset(dataset):
    coords = []

    with open(dataset, 'r', encoding='utf-8') as file:
        start = False
        for line in file:
            if line.strip() == "NODE_COORD_SECTION":
                start = True
                continue
            if start:
                if line.strip() == "EOF":
                    break
                parts = line.strip().split()
                if len(parts) >= 3:
                    idx = int(parts[0]) - 1
                    x = float(parts[1])
                    y = float(parts[2])
                    coords.append((idx, x, y))

    # Сортируем по idx, чтобы порядок соответствовал исходному
    coords.sort(key=lambda x: x[0])
    return [(x, y) for _, x, y in coords]

"""
def load_optimal_tour(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    start = False
    tour = []
    for line in lines:
        if line.strip() == "TOUR_SECTION":
            start = True
            continue
        if line.strip() == "-1" or line.strip() == "EOF":
            break
        if start:
            tour.append(int(line.strip()) - 1)
    return tour
"""
