#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys

##Variables del tablero
filas = 8
columnas = 8
fichaOponente = "$"
ficha = "#"
ultimaX = 0
ultimaY = 0
ultimaTipo = 0
jugadaOponente ={"fila":filas-1,"columna":random.randrange(columnas)}
defensa = []
dificultad = 2

## Funciones
## Mostrar del tablero////////////////////////////////////////////
def mostrarTablero(tablero): 
	"""Esta funcion muestra el tablero"""
	fila = 0
	columna = 0
	for fila in range(0,filas+1):
		columna = 0
		for columna in range(0,columnas+1):
			if len(tablero[fila]) != columna and len(tablero) != fila :
				if fila != filas :
					sys.stdout.write('|')
				else :
					sys.stdout.write(' ')
				sys.stdout.write(str(tablero[fila][columna]))
		sys.stdout.write('\n')

## Creacion del tablero///////////////////////////////////////////
def crearTablero (filas,columnas):
	"""Esta funcion muestra el tablero"""
	tablero = [];
	fila = 0
	columna = 0
	for fila in range(0,filas+1):
		columnasFila = []
		columna = 0
		for columna in range(0,columnas+1):
			if fila != filas :
				if columna != columnas :
					columnasFila.append("_")
				else:
					columnasFila.append(fila+1)
			else:
				if columna != columnas :
					columnasFila.append(columna+1)
		tablero.append(columnasFila)
	return tablero

## Tirar ficha////////////////////////////////////////////////////
def tirarFicha(fichaTirada,posicion,tablero):
	"""Esta funcion tira la ficha en el tablero"""
	global ultimaX
	global ultimaY
	global ultimaTipo
	global fichaOponente
	global ficha
	posicionada = False
	if(posicion > 0 and posicion <9 ) :
		for fila in range(filas-1,-1,-1):
			if tablero[fila][posicion-1] != ficha and tablero[fila][posicion-1] != fichaOponente:
				tablero[fila][posicion-1] = fichaTirada
				ultimaX = fila
				ultimaY = posicion-1
				ultimaTipo = fichaTirada
				posicionada = True
				break
	return posicionada

## Comprobacion columnas//////////////////////////////////////////////
def concurrenciaColumna(tablero,ultimaX,ultimaY,ultimaTipo):
	global filas
	global ficha
	global fichaOponente
	global defensa
	concurrencia = 1
	for fila in range(ultimaX,-1,-1):
		## comprueba en el analisis si es la ficha lanzada
		if fila >= 0 and ultimaX != fila:
			if tablero[fila][ultimaY] == ultimaTipo :
				concurrencia = concurrencia + 1
			else :
				break
		if fila == 0 :
			break;
	for fila in range(ultimaX,filas) :
		## comprueba en el analisis si es la ficha lanzada
		if fila >= 0 and ultimaX != fila:
			if tablero[fila][ultimaY] == ultimaTipo :
				concurrencia = concurrencia + 1
			elif tablero[fila][ultimaY] == "_":
				if concurrencia == 3 and ultimaTipo != fichaOponente:
					if ultimaTipo == ficha :
						fichadefensa = fichaOponente
					else :
						fichadefensa = ficha
					movimiento={"fila":fila,"columna":ultimaY,"fichadefensa":fichadefensa }
					defensa.append(movimiento)
				break
			else:
				break
		if fila == 7 : 
			break;
	return concurrencia

## Comprobacion filas//////////////////////////////////////////////
def concurrenciaFila(tablero,ultimaX,ultimaY,ultimaTipo) :
	global columnas
	global defensa
	global ficha
	global fichaOponente
	concurrencia = 1
	for columna in range(ultimaY,-1,-1):
		## comprueba en el analisis si es la ficha lanzada y los limites
		if columna >= 0 and ultimaY != columna:
			if tablero[ultimaX][columna] == ultimaTipo :
				concurrencia = concurrencia + 1
			elif tablero[ultimaX][columna] == "_":
				if concurrencia == 2 and ultimaTipo != fichaOponente:
					movimiento={"fila":ultimaX,"columna":columna,"fichadefensa":fichaOponente }
					defensa.append(movimiento)
				break
			else:
				break
		if columna == 0 :
			break;
	for columna in range(ultimaY,columnas) :
		## comprueba en el analisis si es la ficha lanzada y los limites
		if columna >= 0 and ultimaY != columna:
			if tablero[ultimaX][columna] == ultimaTipo :
				concurrencia = concurrencia + 1
			elif tablero[ultimaX][columna] == "_":
				if concurrencia == 2 and ultimaTipo != fichaOponente :
					if ultimaTipo == ficha :
						fichadefensa = fichaOponente
					else :
						fichadefensa = ficha
					movimiento={"fila":ultimaX,"columna":columna,"fichadefensa":fichadefensa }
					defensa.append(movimiento)
				break
			else:
				break
		if columna == 7 : 
			break;
	return concurrencia

## Comprobacion diagonales derechas//////////////////////////////////////////////
def concurrenciaDerDiagonal(tablero,ultimaX,ultimaY,ultimaTipo) :
	global filas
	global columnas
	global defensa
	global ficha
	global fichaOponente
	concurrencia = 1
	fila = ultimaX
	columna = ultimaY
	while fila < filas and columna < columnas:
		if tablero[fila][columna] == ultimaTipo and fila != ultimaX and columna != ultimaY:
			concurrencia = concurrencia + 1
		elif tablero[fila][ultimaY] == "_":
			if concurrencia == 2 and ultimaTipo != fichaOponente :
				if ultimaTipo == ficha :
					fichadefensa = fichaOponente
				else :
					fichadefensa = ficha
				movimiento={"fila":fila,"columna":columna,"fichadefensa":fichadefensa }
				defensa.append(movimiento)
			break
		else:
			break
		fila = fila + 1
		columna = columna + 1
	fila = ultimaX
	columna = ultimaY
	while fila < filas and columna < columnas:
		if tablero[fila][columna] == ultimaTipo and fila != ultimaX and columna != ultimaY:
			concurrencia = concurrencia + 1
		elif tablero[fila][ultimaY] == "_":
			if concurrencia == 2 and ultimaTipo != fichaOponente :
				if ultimaTipo == ficha :
					fichadefensa = fichaOponente
				else :
					fichadefensa = ficha
				movimiento={"fila":fila,"columna":columna,"fichadefensa":fichadefensa }
				defensa.append(movimiento)
			break
		else:
			break
		fila = fila - 1
		columna = columna - 1
	return concurrencia

## Comprobacion diagonales izquierdas//////////////////////////////////////////////
def concurrenciaIzqDiagonal(tablero,ultimaX,ultimaY,ultimaTipo) :
	global filas
	global columnas
	global defensa
	global ficha
	global fichaOponente
	concurrencia = 1
	fila = ultimaX
	columna = ultimaY
	while fila < filas and columna < columnas:
		if tablero[fila][columna] == ultimaTipo and fila != ultimaX and columna != ultimaY:
			concurrencia = concurrencia + 1
		elif tablero[fila][ultimaY] == "_":
			if concurrencia == 2 and ultimaTipo != fichaOponente :
				if ultimaTipo == ficha :
					fichadefensa = fichaOponente
				else :
					fichadefensa = ficha
				movimiento={"fila":fila,"columna":columna,"fichadefensa":fichadefensa }
				defensa.append(movimiento)
			break
		else:
			break
		fila = fila + 1
		columna = columna - 1
	fila = ultimaX
	columna = ultimaY
	while fila < filas and columna < columnas:
		if tablero[fila][columna] == ultimaTipo and fila != ultimaX and columna != ultimaY:
			if tablero[fila][columna] == ultimaTipo :
				concurrencia = concurrencia + 1
			elif tablero[fila][ultimaY] == "_":
				if concurrencia == 2 and ultimaTipo != fichaOponente :
					if ultimaTipo == ficha :
						fichadefensa = fichaOponente
					else :
						fichadefensa = ficha
					movimiento={"fila":fila,"columna":columna,"fichadefensa":fichadefensa }
					defensa.append(movimiento)
				break
			else:
				break
		fila = fila - 1
		columna = columna + 1
	return concurrencia

## Simulacion de la tirada del contrincante//////////////////////////////////////////////
def tiradaCPU(tablero,defensa) :
	global columnas
	global jugadaOponente
	global fichaOponente
	PJugadas = []
	tirada = False
	posicionada = False
	if len(defensa) > 0 :
		for movimiento in defensa :
			if tablero [movimiento["fila"]-1][movimiento["columna"]] != "_" :
				tablero [movimiento["fila"]][movimiento["columna"]] = movimiento["fichadefensa"]
				defensa.remove(movimiento)
				tirada = True
				break
	
	ConColumna = concurrenciaColumna(tablero,jugadaOponente["fila"],jugadaOponente["columna"],fichaOponente)
	ConFila = concurrenciaFila(tablero,jugadaOponente["fila"],jugadaOponente["columna"],fichaOponente)
	ConDerDiagonal = concurrenciaDerDiagonal(tablero,jugadaOponente["fila"],jugadaOponente["columna"],fichaOponente)
	ConIzqDiagonal = concurrenciaIzqDiagonal(tablero,jugadaOponente["fila"],jugadaOponente["columna"],fichaOponente)
	print "columna: "+str(jugadaOponente["columna"])
	print "fila: "+str(jugadaOponente["fila"])
	if jugadaOponente["columna"] < columnas-1:
		if tablero[jugadaOponente["fila"]][jugadaOponente["columna"]+1] == "_" :
			# Derecha
			print "Derecha"
			PJugadas.append({"fila":jugadaOponente["fila"],"columna":jugadaOponente["columna"]+1,"tipo":0})
	if jugadaOponente["columna"] > 0:
		if tablero[jugadaOponente["fila"]][jugadaOponente["columna"]-1] == "_" :
			# Izquierda
			PJugadas.append({"fila":jugadaOponente["fila"],"columna":jugadaOponente["columna"]-1,"tipo":2})
			print "Izquierda"
	if jugadaOponente["fila"] < filas-1 and jugadaOponente["columna"] < columnas-1:
		if tablero[jugadaOponente["fila"]+1][jugadaOponente["columna"]+1] == "_" and tablero[jugadaOponente["fila"]][jugadaOponente["columna"]+1] != "_":
			#Derecha superior
			PJugadas.append({"fila":jugadaOponente["fila"]+1,"columna":jugadaOponente["columna"]+1,"tipo":1})
			print "Derecha superior"
	if jugadaOponente["fila"] < filas-1 and jugadaOponente["columna"] > 0:
		if tablero[jugadaOponente["fila"]+1][jugadaOponente["columna"]-1] == "_" and tablero[jugadaOponente["fila"]][jugadaOponente["columna"]-1] != "_":
			#Izquierda Superior
			PJugadas.append({"fila":jugadaOponente["fila"]+1,"columna":jugadaOponente["columna"]-1,"tipo":3})
			print "Izquierda Superior"
	if jugadaOponente["fila"] <= filas-1:
		# Vertical
		if tablero[jugadaOponente["fila"]+1][jugadaOponente["columna"]] == "_" :
			PJugadas.append({"fila":jugadaOponente["fila"]+1,"columna":jugadaOponente["columna"],"tipo":4})
			print "Vertical"
	if jugadaOponente["fila"] > 0 and jugadaOponente["columna"] <columnas -1:
		#Derecha inferior
		if jugadaOponente["fila"] == 0 :
			if tablero[jugadaOponente["fila"]-1][jugadaOponente["columna"]+1] == "_":
				PJugadas.append({"fila":jugadaOponente["fila"]-1,"columna":jugadaOponente["columna"]+1,"tipo":5})
				print "Derecha inferior"
		else :
			if tablero[jugadaOponente["fila"]-1][jugadaOponente["columna"]+1] == "_" and tablero[jugadaOponente["fila"]-2][jugadaOponente["columna"]+1] != "_":
				PJugadas.append({"fila":jugadaOponente["fila"]-1,"columna":jugadaOponente["columna"]+1,"tipo":5})
				print "Derecha inferior"
	if jugadaOponente["fila"] > 0 and jugadaOponente["columna"] >0:
		#Izquierda inferior
		if jugadaOponente["fila"] == 0 :
			if tablero[jugadaOponente["fila"]-1][jugadaOponente["columna"]-1] == "_":
				PJugadas.append({"fila":jugadaOponente["fila"]-1,"columna":jugadaOponente["columna"]+1,"tipo":5})
				print "Izquierda inferior"
		else :
			if tablero[jugadaOponente["fila"]-1][jugadaOponente["columna"]-1] == "_" and tablero[jugadaOponente["fila"]-2][jugadaOponente["columna"]-1] != "_":
				PJugadas.append({"fila":jugadaOponente["fila"]-1,"columna":jugadaOponente["columna"]-1,"tipo":5})
				print "Izquierda inferior"

	print "posibles: "+str(len(PJugadas))
	ordenJugada = []
	ordenJugada.append("NULL")
	ordenJugada.append("NULL")
	ordenJugada.append("NULL")
	ordenJugada.append("NULL")
	ordenJugada.append("NULL")
	ordenJugada.append("NULL")
	ordenJugada.append("NULL")
	ordenJugada.insert(ConColumna,4)
	ordenJugada.insert(ConFila,0)
	ordenJugada.insert(ConFila,2)
	ordenJugada.insert(ConDerDiagonal,1)
	ordenJugada.insert(ConDerDiagonal,5)
	ordenJugada.insert(ConIzqDiagonal,6)
	ordenJugada.insert(ConIzqDiagonal,3)

	for jugada in ordenJugada:
		if jugada != "NULL" :
			for posible in PJugadas :
				if posible["tipo"] == jugada :
					jugadaOponente ={"fila":posible["fila"],"columna":posible["columna"]}
					posicionada = tirarFicha(fichaOponente,posible["columna"]+1,tablero)
					break
			if posicionada == True :
				break


##-----------------------------------------------------
#crear tablero inicial
tablero = crearTablero(filas,columnas)
mostrarTablero(tablero)
opcion = 0
while opcion not in ('1','2'):
	opcion = raw_input("Elige ficha 1-# y 2-$:")
	if opcion == '2' :
		ficha = "$"
		fichaOponente = "#"
	elif opcion == '1':
		ficha = "#"
		fichaOponente = "$"

i =0
while i <= filas*columnas :
	opcion = 0
	while opcion not in ('1','2','3','4','5','6','7','8'):
		opcion = raw_input("Elija la casilla del 1 al "+str(columnas)+" para tirar ficha:")
	opcion = int(opcion)
	tirarFicha(ficha,opcion,tablero)
	conColumna = concurrenciaColumna(tablero,ultimaX,ultimaY,ultimaTipo)
	conFila = concurrenciaFila(tablero,ultimaX,ultimaY,ultimaTipo)
	conDerDiagonal = concurrenciaDerDiagonal(tablero,ultimaX,ultimaY,ultimaTipo)
	conIzqDiagonal = concurrenciaIzqDiagonal(tablero,ultimaX,ultimaY,ultimaTipo)
	if conColumna < conFila :
		conColumna = conFila
	if conColumna < conIzqDiagonal :
		conColumna = conIzqDiagonal
	if conColumna < conDerDiagonal :
		conColumna = conDerDiagonal
	mostrarTablero(tablero)
	if conColumna == 3 :
		print "uff casi"
	if conColumna > 3:
		print "felicidades me has vencido!!!"
		break
	for movimiento in defensa :
		print "fila:"+str(movimiento["fila"])
		print "columna:"+str(movimiento["columna"])
		print "fichadefensa: "+str(movimiento["fichadefensa"])
	tiradaCPU(tablero,defensa)
	conColumna = concurrenciaColumna(tablero,jugadaOponente["fila"],jugadaOponente["columna"],fichaOponente)
	#print "conColumna:"+str(conColumna)
	conFila = concurrenciaFila(tablero,jugadaOponente["fila"],jugadaOponente["columna"],fichaOponente)
	#print "conFila:"+str(conFila)
	conDerDiagonal = concurrenciaDerDiagonal(tablero,jugadaOponente["fila"],jugadaOponente["columna"],fichaOponente)
	#print "conDerDiagonal:"+str(conDerDiagonal)
	conIzqDiagonal = concurrenciaIzqDiagonal(tablero,jugadaOponente["fila"],jugadaOponente["columna"],fichaOponente)
	#print "conIzqDiagonal:"+str(conIzqDiagonal)
	if conColumna < conFila :
		conColumna = conFila
	if conColumna < conIzqDiagonal :
		conColumna = conIzqDiagonal
	if conColumna < conDerDiagonal :
		conColumna = conDerDiagonal
	mostrarTablero(tablero)
	if conColumna >3 :
		print "Has perdido"
		break
	i = i +1

	#tiradas con error 8 9 2 3