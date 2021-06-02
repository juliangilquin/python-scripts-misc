#!/usr/bin/env python

"""acromaker.py, écrit par Julian Gilquin, le 04/03/2021.
Dernière mise à jour le 04/03/2021.
Ce programme permet de fabriquer des acronymes.
"""

def acromaker(phrase):
	acro = []
	for word in phrase.split():
		acro.append(word[0])
	bel_acro = " ".join(acro)
	return bel_acro.upper()


def main():

	print("Bienvenue sur Acromaker ! Saisis une phrase, tape sur Entree et repars avec un acronyme de dingue !")
	la_phrase_du_user = input("Saisis ta phrase maintenant : \n")
	l_acronyme = acromaker(la_phrase_du_user)
	print(f"\n\nVoici ton acronyme de ouf : {l_acronyme}\n\n")
	input("Merci d'avoir utilise mon programme.\nAppuyer sur Entree pour fermer")


if __name__ == '__main__':
	main()
