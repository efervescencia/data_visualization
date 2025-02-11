import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    #hacemos un camino aleatorio
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #trazamos los puntos del camino
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    #eliminamos los ejes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

