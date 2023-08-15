#Modulos
# nombresyedades={"Ricardo":4}
# def AptoParaComprarAlcohol(nombre):
#     edad=nombresyedades[nombre]
#     if edad>=18:
#         return True
#     return False
# edadingresada=int(input("ingrese edad:"))
# if AptoParaComprarAlcohol("Ricardo"):
#     print("si podes")
# else:
#     print("no permitido")
#Escibir funcion q muestre todos los numeros primos entre 1 y n qu es ingresado por parametro:
# def esPrimo(numero):
#     if numero<2:
#         return False
#     for k in range(2,numero-1):
#         if numero%k==0:
#             return False
#     return True
# #n=input("ingresar numero: ")
# def mostrarPrimosHasta(n):
# #def esPrimo(n):
#     for i in range(1,101):
                
#         if esPrimo(i):
#             print(i,end=" ")

# esPrimo(30)
# def di_hola():
#     print("hola! Ricardo")
# di_hola()
#clase nico
# def saludar ():
#     print("hola")
# saludar()
# def saludar(nombre,apellido):
#     print(f"hola (nombre) (apellido)")
# saludar("nico","pipo")
# solicitar al usuario que ingres su direccion email.
#1
# def mailvalido(mail):
#     if "@" in mail:
#         return True
#     else:
#         return False
    
# def mailvalidoFind(mail):
#     if mail.find("@")!=-1:
#         print("valida")
#     else:
#         print("no valida")
# mail=input("ingrese correo:")
# mailvalidoFind(mail)
#factorial
# def fact(numero):
#     Factorial=numero
#     for i in range(1,numero):
#         Factorial=Factorial*i
#     print(f"el factorial de {numero} es {Factorial}")
# fact(5)

# def numero_primo(numero):
        
#     for i in range(2,numero):
#         if numero%i==0:
#             return False
#         return True
# n=int(input("ingresar numero:"))
# for numero in range(1,n):
#         if numero_primo(numero):
#           print(numero)   

# def condimentar(condimento):
#     if condimento=="salir":
#         print("listo")
#         return False
# condimento=str(input("ingresar condimento: "))
# sandwichs="pancho"
# print(sandwichs,condimento,)


# def pedir_ingredientes ():
#   ingredientes = [] # lista vacía
#   print ("Ingrese los ingredientes de su sandwich. Escriba 'fin' para terminar.")
#   while True: # bucle infinito
#     ingrediente = input ("Ingrese un ingrediente: ") # leer el ingrediente
#     if ingrediente == "fin": # si el usuario escribe 'fin'
#       break # salir del bucle
#     else: # si el usuario escribe otro valor
#       ingrediente.append (ingredientes) # agregar el ingrediente a la lista
#   return ingredientes # devolver la lista de ingredientes

# def imprimir_ingredientes (ingredientes):
#   print ("Los ingredientes de tu sandwich son:")
#   for ingrediente in ingredientes: # para cada ingrediente en la lista
#     print (ingrediente) # imprimir el ingrediente

def redondear(n):
    if n>3.50:
          return(n)
    print(round(n))


    
         
               
          


    


# n=3.50
# print(round(n))
# import math
# n=3.50
# n=math.floor(n)
# print(n)

# import math 
# n > 3.50
# n=math.floor(n)
# print((n))
# n=math.ceil(n)
# print(n)





















# def fib(n):
#     if n<2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
# #n=int(input("ingresar numero:"))
# #print(fib(8))
# for x in range(2):
#     print(fib(x))


