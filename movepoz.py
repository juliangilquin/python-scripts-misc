import pyautogui as pag
import random

# variables taille ecran
s_width = pag.size().width
s_height = pag.size().height

# fonction pour un chiffre random en fonction d'un chiffre donné
def rnd_pos(num):
    return random.randint(1, num)

# variable pour un chiffre random entre 1 et 5 pour la duree de deplacement
def rnd_duration():
    return random.randint(1, 5)

def rnd_move():
    pag.moveTo(rnd_pos(s_width), rnd_pos(s_height), duration=rnd_duration())


def main():
    print("\n\nEntre le nombre de mouvements et regarde la souris bouger toute seule.")
    print("Pour arreter, deplace ton curseur tout en haut a gauche de ton ecran.\n\n")
    nb_moves = input("Nombre de moves \n")
    for move in range(int(nb_moves)):
        rnd_move()

if __name__ == "__main__":
    main()