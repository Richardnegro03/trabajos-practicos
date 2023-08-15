# Practico n°7
# 1 - Escriba una función redondear() que permita redondear un número decimal de acuerdo al criterio:
#Si el número es mayor a 3.50, devolver el entero siguiente (en este caso, 4),
#si no devolver el entero inmediatamente anterior (3).
# n=3.50
# print(round(n))
# import math
# n=3.50
# n=math.floor(n)
# print(n)



# 3 - Usando el módulo datetime, escribe un programa que muestre la fecha y hora actuales del sistema.
# from datetime import datetime
# print (datetime.today())




#5 - Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado para la adivinación o para buscar consejo:
# 8 respuestas

import random
while True:
    
    pregunta=input("Ingrese pregunta: ")
    respuesta=random.randint(1,8)
    if pregunta==(""):
        print("Se termino el juego")
        break
    if respuesta==1:
        print("Es seguro que si")
    elif respuesta==2:
        print("Las chances son buenas")
    elif respuesta==3:
        print("Puedes contar con ello")
    elif respuesta==4:
        print("Preguntame de nuevo mas tarde")
    elif respuesta==5:
        print("Concentrate y pregunta de nuevo")
    elif respuesta==6:
        print("No veo con claridad, pregunta de nuevo")
    elif respuesta==7:
        print("Mi respuesta es no")
    elif respuesta==8:
        print("Mis fuentes me dicen que no")


# 6 -Encuentre el tiempo de ejecución de los programas de los ejercicios anteriores (pista: use el módulo time)
import time
inicio=time.time()
time.sleep(1)
fin=time.time()
print(fin-inicio)