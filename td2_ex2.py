import random
def cout_transport(solution):
    x11, x12, x13, x21, x22, x23 = solution
    return 5*x11 + 3*x12 + 4*x13 + 6*x21 + 7*x22 + 2*x23
def generer_voisins(sol):
    voisins = []
    for j, (demande, idx1, idx2) in enumerate([(4, 0, 3), (5, 1, 4), (8, 2, 5)]):
        for delta in [-1, 1]:
            new_sol = list(sol)
            if new_sol[idx1] + delta >= 0 and new_sol[idx1] + delta <= demande:
                new_sol[idx1] += delta
                new_sol[idx2] -= delta
                voisins.append((tuple(new_sol), (idx1, delta)))
    return voisins
def recherche_taboue_exercice2(max_iter=50, taille_tabou=5):
    courante = (2, 3, 4, 2, 2, 4)
    meilleure = courante
    meilleur_cout = cout_transport(courante)
    liste_taboue = []
    for _ in range(max_iter):
        voisins = generer_voisins(courante)
        meilleur_voisin = None
        mouvement_retenu = None
        min_cout_voisin = float('inf')
        for v, mouv in voisins:
            c = cout_transport(v)
            if v not in liste_taboue or c < meilleur_cout:
                if c < min_cout_voisin:
                    min_cout_voisin = c
                    meilleur_voisin = v
                    mouvement_retenu = mouv
        if meilleur_voisin is None:
            break
        courante = meilleur_voisin
        if mouvement_retenu:
            liste_taboue.append(meilleur_voisin)
            if len(liste_taboue) > taille_tabou:
                liste_taboue.pop(0)
        if min_cout_voisin < meilleur_cout:
            meilleure = meilleur_voisin
            meilleur_cout = min_cout_voisin
    return meilleure, meilleur_cout
sol_opt, cout_opt = recherche_taboue_exercice2()
print(f"Exercice 2 - Solution Taboue optimale (x11, x12, x13, x21, x22, x23) : {sol_opt}")
print(f"Coût total minimal trouvé : {cout_opt}")