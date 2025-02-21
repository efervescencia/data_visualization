from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Crea un D6
die = Die()

#hace algunas tiradas y guarda los resultados en una lista
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#analizamos los resultados
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

#visualizamos los resultados
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
        xaxis=x_axis_config, yaxis= y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')