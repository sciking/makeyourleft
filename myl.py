#!/usr/bin/ python-
# -*- coding: utf-8 -*-
import os
import random
turno = 0
planzi = 31
ptua = 4
spar = 1
ptot = planzi + ptua
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
def invio():
	raw_input("Premi invio per continuare")
print """ Benvenuto in Make Your Left, il primo videogioco
nel quale potrai creare il tuo partito di centrosinistra
facendo una scissione dal tuo partito originale,
chiaramente governato da un'oligarchia di
destra che non pensa ai lavoratori.

Ogni 4 turni si terrà il congresso, nel quale potrai candidarti segretario,
proporre iniziative o dichiarare la scissione.
Ma attenzione, se alle elezioni che si tengono ogni 9 turni
non avrai almeno il 4% dovrai ritirarti dalla vita politica!"""


def gioco():
	global ptua,planzi.ptot,turno
	ptot = ptua = planzi
	turno = turno +1
	if spar == 1:
		print "Unione Democratica - Sistema Informatico"
	else:
		print "Federazione Nuova Sinistra - Sistema Informatico"
