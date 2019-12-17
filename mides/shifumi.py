import random

action_list = ["pierre", "papier", "ciseaux"]

nb_victoires = 0

while nb_victoires != 3:
    bot = action_list[random.randint(0, 2)]
    choix_joueur = input("Choisis 'pierre', 'papier' ou 'ciseaux' : ")
    if bot == choix_joueur:
        print("Égalité !")
    elif (bot == "pierre" and choix_joueur == 'ciseaux') or (bot == "ciseaux" and choix_joueur == 'papier') or (bot == "papier" and choix_joueur == 'pierre'):
        print("C'est perdu !")
    elif (bot == "ciseaux" and choix_joueur == 'pierre') or (bot == "papier" and choix_joueur == 'ciseaux') or (bot == "pierre" and choix_joueur == 'papier'):
        print("Tu as gagné une manche !")
        nb_victoires = nb_victoires + 1
        print("Nouveau score :", nb_victoires)
    print("Ton score actuel est", nb_victoires)
    print("Prêt pour une nouvelle partie ?")
    print()
print("Tu as remporté 3 manches, tu as gagné au shifumi !")
