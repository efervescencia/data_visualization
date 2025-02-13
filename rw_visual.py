import matplotlib.pyplot as plt
from sympy.printing.pretty.pretty_symbology import line_width

from random_walk import RandomWalk
while True:
    #hacemos un camino aleatorio
    rw = RandomWalk(5_000)
    rw.fill_walk()

    #trazamos los puntos del camino
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9), dpi=128)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values)

    #eliminamos los ejes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

