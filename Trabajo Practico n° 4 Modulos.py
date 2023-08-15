#Trabajo Practico n° 4 Modulos.py
# 1-Escriba una función que muestre todos los números primos entre 1 y un número n que es ingresado por parámetro.
# def numero_primo(numero):
        
#     for i in range(2,numero):
#         if numero%i==0:
#             return False
#         return True
# n=int(input("ingresar numero:"))
# for numero in range(1,n):
#         if numero_primo(numero):
#           print(numero)   

#2 - Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta que el usuario ingrese ‘salir’.
#Cada vez que se ingrese un condimento, muestre un mensaje avisando que ya se agregó el condimento al sándwich,
#Escriba versiones diferentes del programa de acuerdo a estos criterios:
#Use un test condicional en el ciclo while para detener la ejecución.
#Use un test condicional dentro del ciclo para decidir si continuar la ejecución.

def pedir_ingredientes ():
  ingredientes = [] # lista vacía
  print ("Ingrese los ingredientes de su sandwich, Escriba 'fin' para terminar.")
  while True: # bucle infinito
    ingrediente = input ("Ingrese un ingrediente: ") # leer el ingrediente
    if ingrediente == "fin": # si el usuario escribe 'fin'
      break # salir del bucle
    else: # si el usuario escribe otro valor
      ingredientes.append (ingrediente) # agregar el ingrediente a la lista
  return ingrediente # devolver la lista de ingredientes
print()






#4 - Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros de la serie de Fibonacci
#En esta serie, los primeros dos números son 0 y 1, y cada sucesivo número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8

# def fib(n):
#     if n<2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
# #n=int(input("ingresar numero:"))
# #print(fib(8))
# for x in range(2):
#     print(fib(x))
    