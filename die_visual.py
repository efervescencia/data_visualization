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