# -*- coding: Latin-1 -*-
import os
import random
import math

argent = 200 #somme initiale

while argent >= 0 :
	print("Somme actuelle : ", argent, "$")
	
	#verification du parametre de mise
	miseOk = False
	while miseOk is False :
		try :
			mise = int(input("Combien souhaitez vous miser à la roulette ?"))
			assert mise < 0 , "La mise doit etre supérieur à zéro"
			assert mise > argent, "La mise ne peut pas dépasser l'argent possédé"
		else : 
			miseOk = True
		except ValueError: 
			print("Veuillez entrer un entier")
	
	#verification du parametre de la cible du paris
	cibleOk = False
	while cibleOk is False :
		try :
			numeroCible = int(input("Sur quel numero souhaitez vous miser?"))
			assert numeroCible < 0 , "La cible de la mise ne peut pas être inférieure à zéro"
			assert numeroCible > 49, "La cible de la mise ne peut pas être supérieure à 49"
		else : 
			cibleOk = True
		except ValueError: 
			print("Veuillez entrer un entier")
	
	#resultat de la roulette
	numeroRoulette = random.randrange(49)
	
	couleurMise = (numeroCible % 2) == 0
	couleurResultat = (numeroRoulette % 2) == 0
	
	gain = 0
	#calcul des gains
	if couleurMise == couleurResultat : 
		gain = math.ceil(mise)
		argent += gain
		print("Même couleur, vous gagnez", gain, "$")

	if numeroCible == numeroRoulette : 
		gain = mise * 3
		argent += gain
		print("Bon numéro, vous gagnez", mise, "$")

	# Pour eviter de reverser la mise initiale si l'on trouve le bon numero (car on a aussi forcement la bonne couleur)
	# le rajout de la mise est fait ici
	if gain > 0 :	
		argent += mise

	

os.command("pause")