#UNIDAD 1

#EJERCICIO 1

"""
jugador1 = input("¿Cuál es la jugada del primer jugador?  ")
jugador1 = jugador1.upper()


jugador2 = input("¿Cuál es la jugada del segundo jugador?  ")
jugador2 = jugador2.upper()

if jugador1 == jugador2:
  print("Hubo empate")

if (jugador1 == "TIJERA" and jugador2 == "PIEDRA") or (jugador1 == "PIEDRA" and jugador2=="PAPEL") or (jugador1=="PAPEL" and jugador2=="TIJERA"):
  print ("Ganó el Jugador 2")

else: print("Ganó el Jugador 1")

"""

#EJERCICIO 2
"""
max = 0

for i in range (5): 
  i = int(input("Ingrese un número: "))
  if i > max:
    max = i

print("El mayor numero es:", max)

"""



#EJERCICIO 3
"""
numero = int(input("Ingrese un número: "))
par = 0
if numero % 2 == 0:
    par= par + numero

pregunta = input("¿Desea ingresar otro?: ")

while pregunta != "no":
  numero = int(input("Ingrese un número: "))
  pregunta = input("¿Desea ingresar otro?: ")
  if numero % 2 == 0:
    par= par + numero

print("Terminado")
print("La suma de los numeros pares son:", par)

"""
#EJERCICIO 4

"""
j1 = int(input("Jugador 1, ingrese su número secreto: "))
intentos = 0

while j1 < 100 and j1 > 1:
  j2 = int(input("Jugador 2, ingrese un número para adivinarlo: "))
  if j2 == j1:
      print("¡Felicidades, adivinaste el número secreto en", intentos, "intentos!")
  elif j2 < j1:
      print("El número ingresado es menor que el número secreto. Inténtalo de nuevo.")
      intentos = intentos + 1
  elif j2 > j1:
      print("El número ingresado es mayor que el número secreto. Inténtalo de nuevo.")
      intentos = intentos + 1

print("Vuelva a Intentarlo. Ingrese un número del 1 al 100")
"""
#EJERCICIO 6

##VERSION DE CLASE!!!!!!!!!


codigo_secreto = []

contador_intentos = 0
ingresocódigo = input("Ingrese un número de 4 dígitos: ")

for i in range (len(ingresocódigo)):
  codigo_secreto.append(ingresocódigo[i])

while contador_intentos < 8: 
  contador_aciertos = 0 #PARA VOLVER A 0 
  listaadivinar = [] #PARA QUE NO SE VAYA REAPPENDEANDO 
  
  input_adivinar = input("Ingrese el número que quiere adivinar el código secreto: ")

  for i in range (len(input_adivinar)):
    listaadivinar.append(input_adivinar[i])


  for i in range(len(codigo_secreto)):
    if (codigo_secreto[i] == listaadivinar[i]):
      contador_aciertos = contador_aciertos + 1

  print("Usted tuvo", contador_aciertos,"aciertos")

  if contador_aciertos == 4 :
    print ("Ganaste!")
    break
    
  print("Le quedan", 7 - contador_intentos, "intentos")
 

  contador_intentos += 1

print("Perdiste!!!!")
  

