# -*- coding: Latin-1 -*-

import pickle
import random
import os
import donnees

def trouverMot() : 
	taille = len(donnees.listeMot)
	return str(donnees.listeMot[random.randrange(taille)])
	
def devinerLettre(lettre, mot, lettreJouees) :
	bienJoue = False

	if mot.count(lettre) > 0 :
		print("Felicitation, la lettre {} est bien presente dans le mot mystere".format(lettre))
		bienJoue = True
	else : 
		print("Pas de chance, la lettre {} n'est pas presente dans le mot mystere".format(lettre))

	#affichage du mot avec les lettres deja trouvees
	fin = True
	aAfficher = str()
	for i in mot :
		if i in lettreJouees : 
			aAfficher += i
		else : 
			aAfficher += "-"
			fin = False
	
	print(mot)
	print(fin)
	print("Mot mystere : {} \nLettres jouees : {}".format(aAfficher, lettreJouees))
	
	return bienJoue, fin

def chargerScore(nom) :
	try :
		with open('donnees', 'rb') as fichier:
			mon_unpickler = pickle.Unpickler(fichier)
			donnees.score = mon_unpickler.load()
	except : 
		with open('donnees', 'wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(donnees.score)
	
	if not nom in donnees.score :
		donnees.score[nom] = 0
	
	return donnees.score[nom]
	
def sauverScore(nom, scoreCourant) :
	donnees.score[nom] = scoreCourant

	with open('donnees', 'wb') as fichier:
		mon_pickler = pickle.Pickler(fichier)
		mon_pickler.dump(donnees.score)

# test de la fonction trouverMot()
if __name__ == "__main__":
        print (trouverMot() )
        os.system("pause")
