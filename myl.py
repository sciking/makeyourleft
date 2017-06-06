#!/usr/bin/ python-
# -*- coding: utf-8 -*-
import os
import random
turno = 0
planzi = 31
ptua = 4
alpar = 65
spar = 1
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
def invio():
	raw_input("Premi invio per continuare")
print """ Benvenuto in Make Your Left, il primo videogioco
nel quale potrai creare il tuo partito di centrosinistra
facendo una scissione dal tuo partito originale,
chiaramente governato da un'oligarchia di
destra che non pensa ai lavoratori, giudata dal malefico
Matteo Lanzi.

Ogni 4 turni si terrà il congresso, nel quale potrai candidarti segretario,
proporre iniziative o dichiarare la scissione.
Ma attenzione, se alle elezioni che si tengono ogni 9 turni
non avrai almeno il 4% dovrai ritirarti dalla vita politica!"""
print ptua
invio()
clear()
def gioco():
	global ptua,planzi,turno,alpar,spar

	alpar = alpar + random.randint(3,3)
	if ptua < 0:
		ptua = 0
	if planzi < 0:
		planzi = 0
	ptot = ptua = planzi
	turno = turno +1
	if spar == 1:
		print "Unione Democratica - Sistema Informatico"
	else:
		print "Federazione Nuova Sinistra - Sistema Informatico"
	planzi = planzi + random.randint(-5,5)
	#ptua = ptua + random.randint(-1,1)
	#qui inizia il giornale
	gior = random.randint(1,10)

	print("La Sinistra Unita - Giornale dei Lavoratori")

	if gior == 1:
		print "Matteo Lanzi: Bisogna cambiare la Sinista"
		planzi = planzi + random.randint(-2,4)
		ptua = ptua + random.randint(-1,2)
	elif gior == 2:
		print "La svolta a sinistra va bene, molti la vorrebbero"
		ptua = ptua + 2
		planzi = planzi - 3
	elif gior == 3:
		print "Cristiani e Democratici entra nell'Unione Democratica \n Pieno supporto a Lanzi"
		planzi = planzi + 4
	elif gior == 4:
		print "Flop linea Lanzi, persi 3 capoluoghi tra cui Agrusco, roccaforte rossa"
		planzi = planzi + 3
	elif gior == 5:
		print "Lanzi? Ci fa vincere i comuni! \n Vinta Gallarago, roccaforte dei Liberali"
		planzi = planzi + 3
	elif gior == 6:
		print "Scissione? Farebbe bene alla Sinistra vera: \n Il parere di Zuribersky, il famoso politologo"
		ptua = ptua + 3
	elif gior == 7:
		print "Sinistra Libera? La lista scissionista fa flop a Casorano"
		ptua = ptua - 2
	elif gior == 8:
		print "Una lista unita Partito Indipendente + UD? \n Fa discutere, ma potrebbe vincere Puzzago"
		alpar = alpar + 2
		ptua = ptua + 1
		planzi = planzi + 1
	elif gior == 9:
		print "L'assemblea nazionale del Partito a Lambrano non chiarisce nulla \n Sempre più incertezza"
		alpar = alpar + 3
		ptua = ptua - 1
		planzi = planzi - 2
	elif gior == 10:
		print "Appalti truccati ad Airate per la stazione? Consiglieri UD assolti!"
		planzi = planzi + random.randint(-4,3)
		ptua = ptua + random.randint(-1,2)
	print("*"*40)
	print "Voti Lanzi: ", planzi
	print "Voti tuoi: ", ptua
	print "Altri partiti: ", alpar
	coeff = (((planzi+ptua+alpar)/100)*4)
	print coeff
	print "SONDAGGI:"
	if coeff < ptua:
		print "Elezione probabile"
	else:
		print "Elezione a rischio"


#congresso
	if turno%4 == 0 and spar == 1:
		print "CONGRESSO DI UNIONE DEMOCRATICA"
		print("""Opzioni:
1) Candidati segretario
2) Dichiara la scissione
3) Intervento pro-segreteria
4) Intervento istituzionale
5) Non recarti al Congresso""")
		l = input(">")
		if l == 1:
			if ptua > planzi and random.randint(1,10) > 4:
				print("Sei stato eletto segretario!")
				vittoria()
			else:
				print("Perdi la segreteria")
				ptua = ptua + random.randint(-4,6)
				planzi = plandi + random.randint(-6,7)
		elif l == 2:
			print("L'Osservatore del Parlamento\nRivoluzione a Sinistra! Dichiarata la scissione\nNasce Nuova Sinistra")
			spar = 0
		elif l == 3:
			print("L'Osservatore del Parlamento\nIl Collettivo Nuova Sinistra supporta Lanzi")
			ptua = ptua + random.randint(-2,5)
			planzi = plandi + random.randint(-3,6)
		elif l == 4:
			print("L'Osservatore del Parlamento\nIl famoso deputato di Nuova Sinistra: 'Viva la Democrazia'")
			ptua = ptua + random.randint(-1,2)
		elif l == 5:
			print("L'Osservatore del Parlamento\nStrappo di Nuova Sinistra? Mancanti al congresso")
	invio()
	clear()
	gioco()

def vittoria():
		print("Pota")
		exit()
gioco()
