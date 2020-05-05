# -*- coding: Latin-1 -*-
import os
import fonctions
import donnees

nomJoueur = input("Veuillez rentrer votre nom : ")

#charger sauvegarde
#TODO chargement
score = fonctions.chargerScore(nomJoueur)
print("Votre score est de {}".format(score))

jouer = True
while jouer == True :
		
	essaisRestants = donnees.nbrEssaiMax 

	#choisir un mot au hasard
	aTrouver = fonctions.trouverMot()
	lettreJouees = set() #un set empeche les doublons

	#boucle d'interaction par lettre
	while essaisRestants > 0:
		print("Essais restants : {}".format( essaisRestants ) )
		lettreOk = False
		while lettreOk == False :
			lettre = input("Quelle lettre le mot doit-il contenir ? : ")
			#verification de l'entree
			print(len(lettre))
			assert len(lettre) == 1 ,"Vous ne devez renseigner qu'une seule lettre"
			assert lettre.isdigit() == False, "Seules les lettres sont autorisees"
			if (lettre in lettreJouees) == True :
				print ("La lettre saisie a deja ete jouee")
				continue
			lettreOk = True
		essaisRestants -= 1
		lettreJouees.add(lettre)
		
		#la lettre existe-elle dans le mot ? 
		bienJoue, fin = fonctions.devinerLettre(lettre, aTrouver, lettreJouees )
		if bienJoue : 
			essaisRestants += 1

		if fin == True :
			break

    #enregistrement du score
	if fin == True :
		print("Felicitation, vous avez trouve le mot ! Votre score passe de {} a {}".format(score, score + essaisRestants))
		score += essaisRestants
		#TODO sauvegarde
		fonctions.sauverScore(nomJoueur, score)
	else :
		print("Quel dommage, vous n'avez pas trouve le mot {}. Votre score reste de {}".format(aTrouver, score))
		
	jouer = str(input("Desirez-vous rejouer ? oO/nN : ")).lower() == "o"


os.system("pause")
