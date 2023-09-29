# Cargar librería
from Dados import dados

# Cargar dados
dice = dados()
# Seleccionar un número de dado
dados.escoger(3)
# Generar un lanzamiento aleatorio con probabilidad igual para cada cara
lanzamiento = dados.lanzar()
# Imprimir lanzamiento
print(lanzamiento)

# Nota
# Para ver más dados.help
# No se necesita ninguna paquetería adicional, todos los módulos son python base para Python 3.7+