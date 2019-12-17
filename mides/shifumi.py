import random  # on importe une fonction qui va nous servir à choisir une action au hasard

# le joueur et l'ordi peuvent choisir parmi ces 3 éléments
action_list = ["pierre", "papier", "ciseaux"]

# on a un compteur pour garder en mémoire dans la boucle le nombre de victoires du joueur
nb_victoires = 0

# tant que le joueur n'a pas gagné 3 manches, on continue la boucle
while nb_victoires != 3:

    # une action au hasard est choisi pour l'ordi
    bot = action_list[random.randint(0, 2)]

    # le joueur doit choisir une action
    choix_joueur = input("Choisis 'pierre', 'papier' ou 'ciseaux' : ")

    # si le joueur et l'ordi ont la même action, c'est égalité
    if bot == choix_joueur:
        print("Égalité !")

    elif (bot == "pierre" and choix_joueur == 'ciseaux') or (bot == "ciseaux" and choix_joueur == 'papier') or (bot == "papier" and choix_joueur == 'pierre'):
        print("C'est perdu !")

    elif (bot == "ciseaux" and choix_joueur == 'pierre') or (bot == "papier" and choix_joueur == 'ciseaux') or (bot == "pierre" and choix_joueur == 'papier'):
        print("Tu as gagné une manche !")
        nb_victoires = nb_victoires + 1 # comme le joueur vient d egagner une manche, on incrémente son nombre de victoires
        print("Nouveau score :", nb_victoires)

    print("Ton score actuel est", nb_victoires)
    print("Prêt pour une nouvelle partie ?")
    print()

print("Tu as remporté 3 manches, tu as gagné au shifumi !")
