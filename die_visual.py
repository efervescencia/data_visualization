from die import Die

#Crea un D6
die = Die()

#hace algunas tiradas y guarda los resultados en una lista
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)