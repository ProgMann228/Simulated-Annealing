import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def path_visual(coord):
    # Разделим координаты по осям для построения
    x = [point[0] for point in coord]
    y = [point[1] for point in coord]

    # Добавим первую точку в конец, чтобы замкнуть маршрут
    x.append(coord[0][0])
    y.append(coord[0][1])

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.title("Маршрут коммивояжёра")
    plt.xlabel("X координата")
    plt.ylabel("Y координата")

    # Подпишем города
    for i, (xi, yi) in enumerate(coord):
        plt.text(xi + 1, yi + 1, str(i), fontsize=9)

    plt.grid(True)
    plt.show()


def animate_paths(route_history):
    fig, ax = plt.subplots(figsize=(8, 6))
    line, = ax.plot([], [], 'bo-', lw=2)
    text_labels = []

    def init():
        all_x = [p[0] for route in route_history for p in route]
        all_y = [p[1] for route in route_history for p in route]
        padding = 10

        ax.set_xlim(min(all_x) - padding, max(all_x) + padding)
        ax.set_ylim(min(all_y) - padding, max(all_y) + padding)
        return line,

    def update(frame):
        coord = route_history[frame]
        x = [p[0] for p in coord] + [coord[0][0]]
        y = [p[1] for p in coord] + [coord[0][1]]
        line.set_data(x, y)

        # очищаем и перерисовываем подписи
        for t in text_labels:
            t.remove()
        text_labels.clear()

        for i, (xi, yi) in enumerate(coord):
            text = ax.text(xi + 1, yi + 1, str(i), fontsize=8)
            text_labels.append(text)

        return line, *text_labels

    ani = FuncAnimation(fig, update, frames=len(route_history),
                        init_func=init, blit=True, interval=10, repeat=False)
    plt.title("Эволюция маршрута (отжиг)")
    plt.show()


def func_visualize(func, best_point, bounds=(-5.12, 5.12), resolution=200):
    """
    Визуализация 2D функции (2 входных переменных) сверху (контурный график),
    с отмеченной найденной точкой оптимума.

    Parameters:
    - func: функция, принимающая numpy array из 2 элементов и возвращающая число
    - best_point: numpy array из 2 элементов — найденная оптимальная точка
    - bounds: кортеж (мин, макс) диапазона для переменных
    - resolution: количество точек по каждой оси для построения сетки
    """
    x = np.linspace(bounds[0], bounds[1], resolution)
    y = np.linspace(bounds[0], bounds[1], resolution)
    X, Y = np.meshgrid(x, y)

    Z = np.zeros_like(X)
    for i in range(resolution):
        for j in range(resolution):
            Z[i, j] = func(np.array([X[i, j], Y[i, j]]))

    plt.figure(figsize=(8, 6))
    contour = plt.contourf(X, Y, Z, levels=100, cmap='viridis')
    plt.colorbar(contour)
    plt.scatter(best_point[0], best_point[1], color='red', s=80, label='Оптимум')
    plt.title('Вид сверху: контур функции с оптимумом')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()
