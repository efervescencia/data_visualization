import matplotlib.pyplot as plt

from random_walk import RandomWalk

#hacemos un camino aleatorio
rw = RandomWalk()
rw.fill_walk()

#trazamos los puntos del camino
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
