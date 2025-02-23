import matplotlib.pyplot as plt

input_values = range(1,1001)
squares = [x**2 for x in input_values]
fig, ax = plt.subplots()
#print(plt.style.available)
plt.style.use('seaborn-v0_8')


ax.scatter(input_values,squares, c=squares, cmap=plt.cm.Blues, s=10)

#ponemos titulo y etiquetas
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

#establecemos el tamaño del punto de los ejes
ax.tick_params(axis='both', which='major', labelsize=14)

#establecemos el rango
ax.axis([0,1100,0,1000000])
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()

