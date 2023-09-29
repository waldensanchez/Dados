from random import randrange

# Para Python 3.7+
# No es necesario instalar paqueterías adicionales, utiliza módulos de python base

class dados():
    def __init__(self):
        self.todos = {dice:values for dice,values in zip([1,2,3,4],[[1,2,3,4,5,6],[1,2,3,3],[1,2,3,6,6,6],[1,2,3,4,5,6,7,7]])}
        self.help = "Para conocer los dados se pone dados.todos, para escoger dados.escoger(numero_de_dado), y para lanzar una vez escogido dados.lanzar()"
    
    def escoger(self,numero_dado: int):
        self.dado = self.todos[numero_dado]
        print(f'Dado {numero_dado} seleccionado! Ya lo puede lanzar.')
        return self.dado

    def lanzar(self):   
        tiro = randrange( start = 0, stop = len(self.dado) )
        return self.dado[tiro]