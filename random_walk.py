from random import choice
class RandomWalk:
    """Una clase para generar caminos aleatorios"""

    def __init__(self, num_points=5000):
        """Inicializamos los atributos de un camino"""
        self.num_points = num_points

        #todos los caminos empiezan en 0,0
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """calcula los puntos del camino"""

        #sigue dando pasos hasta alcanzar la longitud deseada
        while len(self.x_values) < self.num_points:

            #decide la direccion y cuanto avanzar
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #rechazamos movimientos que no vana  ningun sitio
            if x_step == 0 and y_step == 0:
                continue

            #calculoamos la nueva posicion
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)





