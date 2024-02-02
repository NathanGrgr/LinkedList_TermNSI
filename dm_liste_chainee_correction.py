"""
DM NSI a completer a la maison
Vous devez remplacer toutes les fonctions qui contiennent "pass" par leur implementation.
Les tests sont déjà fournis.
Il y a une petite explication de ce que fait chaque fonction.
Sinon regardez les tests pour voir des exemples.
Vous ne voyez pas tous les tests ceux ci sont juste pour vous aider.

Il y aura quelques points sur la qualité des noms de variables.
J'ai mis le nombre de points sur 20 entre parenthese pour chaque fonction.
Je vais regarder le code, je ne mets pas 0 à une question par ce que le test ne passe pas.
Vous ne devez pas modifier les tests.
"""

import io, sys # pour les tests

class Cellule:
    """Une cellule de la liste chainée.
    ATTENTION c'est suivante avec e.
    Si vous faites cellule.suivant = quelque chose, cela va marcher mais pas comme vous voulez."""
    def __init__(self, valeur_initiale: int):
        self.valeur = valeur_initiale # la valeur de la cellule est initialisée avec la valeur initiale
        self.suivante = None # la cellule suivante dans la liste ou None si il n'y a pas de cellule suivante

    def __repr__(self):
        return str(self.valeur)

class ListeChainee:
    """Une liste chainee, on ne peut accéder que à la tête de la liste.
    Au début elle est toujours vide"""
    def __init__(self):
        self.tete = None # au debut la liste est vide

    def ajouter_en_tete(self, valeur_nouvelle_cellule: int): # (4 points)
        # ajoute la nouvelle valeur dans une cellule en tete de la liste chainee
        cell = Cellule(valeur_nouvelle_cellule)
        cell.suivante = self.tete
        self.tete = cell

    def ajouter_en_queue(self, valeur_nouvelle_cellule: int): # (4 points)
        # ajoute la nouvelle valeur dans une cellule a la fin de la liste chainee
        if self.tete is None:
            self.ajouter_en_tete(valeur_nouvelle_cellule)
            return

        cell = Cellule(valeur_nouvelle_cellule)
        courant = self.tete
        while courant.suivante is not None:
            courant = courant.suivante

        courant.suivante = cell

    def remplir(self, valeurs_pour_remplir: [int]): # (2 points)
        # remplit la liste chainee avec les valeurs donnees en conservant l'ordre des valeurs dans le tableau
        # si il y a deja des elements, les nouveaux elements sont ajoutes a la fin
        for v in valeurs_pour_remplir:
            self.ajouter_en_queue(v)

    def afficher_liste(self): # (2 points)
        # affiche la liste chainee dans la console avec un print, attention le format est tres precis
        # si la liste chainee est vide il faut afficher 'Liste chainee vide'.
        # si par exemple elle contient 1 2 et 3 dans cette ordre il faut afficher '1 -> 2 -> 3' sur une seule ligne
        # vous devez garder le \n mis par defaut par la fonction print.
        if self.tete is None:
            print("Liste chainee vide")
        else:
            print(self.tete.valeur, end='')
            courant = self.tete.suivante
            while courant is not None:
                print(' ->', courant.valeur, end='')
                courant = courant.suivante
            print('')

    def chercher(self, valeur_a_trouver: int) -> Cellule: # (2 points)
        # recherche la premiere occurrence de la valeure donnee dans la liste.
        # ATTENTION, vous devez retourner la *cellule* AVANT la cellule contenant la valeur que vous chercher
        # Exemple pour chercher 2 dans 1 -> 2 -> 1 il faut retourner la cellule qui contient le premier 1
        # pour chercher 1 dans 1 -> 2 vous devez retourner None car il n'y a aucune cellule avant.
        # si la valeur n'est pas présente vous devez executer l'instruction Python suivante :
        # 'raise ValueError("La valeur n'est pas presente dans la liste")'
        if self.tete.valeur == valeur_a_trouver:
            return None
        courant = self.tete
        while courant.suivante is not None:
            if courant.suivante.valeur == valeur_a_trouver:
                return courant
            courant = courant.suivante
        raise ValueError("La valeur n'est pas presente dans la liste")

    def chercher_bonus(self, valeur_a_trouver: int) -> Cellule: # (bonus) la fonction n'est pas testee par moi
        # retourne la cellule qui contient la premiere occurrence de la valeur donnee
        # (pas la cellule avant comme dans la question precedente).
        res = self.chercher(valeur_a_trouver)
        if res is None:
            return self.tete
        else:
            return res.suivant.suivant

    def supprimer(self, valeur_a_supprimer: int): # (2 points)
        # supprime la premiere cellule qui contient la valeur a supprimer
        # conseil, si vous utilisez la methode self.chercher, vous devez l'entourer d'un bloc try, except
        # si vous arrivez dans la clause except, il n'y a rien a faire vous pouvez juste retourner de la fonction
        try:
            res = self.chercher(valeur_a_supprimer)
        except:
            return
        if res is None:
            self.tete = self.tete.suivante
        else:
            res.suivante = res.suivante.suivante

    def fusionner(self, autre_liste): # autre_liste est une instance de ListeChainee (2 points)
        # ajouter le contenu de l'autre liste chainee a la fin de celle ci
        # ATTENTION l'autre liste doit etre vide a la fin de cette fonction.
        derniere = self.tete
        while derniere.suivante is not None:
            derniere = derniere.suivante
        derniere.suivante = autre_liste.tete
        autre_liste.tete = None

    def transformer_en_liste(self) -> [int]: # cette fonction n'a pas de sens mais qui sert pour les tests
        liste = []
        courant = self.tete
        while courant is not None:
            liste.append(courant.valeur)
            courant = courant.suivante
        return liste

def test_ajouter_en_tete():
    l1 = ListeChainee()
    if l1.transformer_en_liste() != []:
        raise ValueError("La liste chainee l1 n'est pas vide")
    l1.ajouter_en_tete(5)
    if l1.transformer_en_liste() != [5]:
        raise ValueError("La liste chainee l1 devrait contenir 5")
    l1.ajouter_en_tete(8)
    if l1.transformer_en_liste() != [8, 5]:
        raise ValueError("La liste chainee l1 devrait contenir 8 -> 5")

def test_ajouter_en_queue():
    l1 = ListeChainee()
    if l1.transformer_en_liste() != []:
        raise ValueError("La liste chainee l1 n'est pas vide")
    l1.ajouter_en_queue(5)
    if l1.transformer_en_liste() != [5]:
        raise ValueError("La liste chainee l1 devrait contenir 5")
    l1.ajouter_en_queue(8)
    if l1.transformer_en_liste() != [5, 8]:
        raise ValueError("La liste chainee l1 devrait contenir 5 -> 8")

def test_remplir():
    l1 = ListeChainee()
    l1.remplir([])
    if l1.transformer_en_liste() != []:
        raise ValueError("La liste chainee l1 n'est pas vide")
    l1.remplir([1, 2, 3])
    if l1.transformer_en_liste() != [1, 2, 3]:
        raise ValueError("La liste chainee l1 devrait contenir 1 -> 2 -> 3")
    l1.remplir([4, 5])
    if l1.transformer_en_liste() != [1, 2, 3, 4, 5]:
        raise ValueError("La liste chainee l1 devrait contenir 1 -> 2 -> 3 -> 4 -> 5")

def test_afficher_liste():
    sortie = io.StringIO()
    stdout_origin = sys.stdout
    sys.stdout = sortie

    l1 = ListeChainee()
    l1.afficher_liste()
    if sortie.getvalue() != "Liste chainee vide\n":
        sys.stdout = stdout_origin # restore stdout
        raise ValueError("La sortie doit être 'Liste chainee vide'")

    # reset sortie
    sortie.truncate(0)
    sortie.seek(0)

    l1.remplir([1, 2, 3])
    l1.afficher_liste()

    if sortie.getvalue() != "1 -> 2 -> 3\n":
        sys.stdout = stdout_origin # restore stdout
        raise ValueError("La sortie doit être '1 -> 2 -> 3'")

    sys.stdout = stdout_origin

def test_chercher():
    l1 = ListeChainee()
    l1.remplir([1, 2, 3, 4, 5, 1])
    if l1.chercher(1) is not None:
        raise ValueError("Il n'y a pas de cellule avant 1 dans 1 -> 2 -> 3 -> 4 -> 5 -> 1.")

    resultat = l1.chercher(5)
    if not isinstance(resultat, Cellule):
        raise ValueError("Le type de retour de la recherche de 5 devrait etre une cellule.")
    if resultat.valeur != 4:
        raise ValueError("La cellule avant le 5 contient 4 dans 1 -> 2 -> 3 -> 4 -> 5 -> 1.")


def test_supprimer_cellule():
    l1 = ListeChainee()
    l1.remplir([1, 2, 3, 4, 1, 5])

    l1.supprimer(6)
    if l1.transformer_en_liste() != [1, 2, 3, 4, 1, 5]:
        raise ValueError("La liste chainee 1 -> 2 -> 3 -> 4 -> 5 devrait etre inchangee apres la suppression de 6.")

    l1.supprimer(4)
    if l1.transformer_en_liste() != [1, 2, 3, 1, 5]:
        raise ValueError("La cellule qui contient 4 n'a pas ete supprimee dans la liste chainee 1 -> 2 -> 3 -> 4 -> 1-> 5.")

    l1.supprimer(1)
    if l1.transformer_en_liste() != [2, 3, 1, 5]:
        raise ValueError("La cellule qui contient 1 n'a pas ete supprimee dans la liste chainee 1 -> 2 -> 3 -> 1 -> 5.")

    l1.supprimer(5)
    if l1.transformer_en_liste() != [2, 3, 1]:
        raise ValueError("La cellule qui contient 5 n'a pas ete supprimee dans la liste chainee 2 -> 3 -> 1 -> 5.")

def test_fusionner():
    l1 = ListeChainee()
    l2 = ListeChainee()

    l1.remplir([1, 2, 3])
    l2.remplir([4, 5])

    l1.fusionner(l2)
    if l1.transformer_en_liste() != [1, 2, 3, 4, 5]:
        raise ValueError("Erreur dans la fusion de 1 -> 2 -> 3 et 4 -> 5.")
    if l2.transformer_en_liste() != []:
        raise ValueError("Apres la fusion, 4 -> 5 doit etre une liste vide.")

def lancer_test(function_test):
    try:
        function_test()
        print("Test", function_test.__name__, "passe avec succes.")
    except Exception as e:
        print("Erreur dans le test", function_test.__name__ + ".", str(e))

if __name__ == "__main__":
    # ici vous pouvez ecrire des petits tests a la main pour vos fonctions (pas evalue, c'est pour vous)
    l1 = ListeChainee() # vous pouvez supprimer ca c'est pour l'exemple
    l1.remplir([1, 2, 3]) # ca aussi
    l1.afficher_liste()

    # lancement des tests
    lancer_test(test_ajouter_en_tete)
    lancer_test(test_ajouter_en_queue)
    lancer_test(test_remplir)
    lancer_test(test_afficher_liste)
    lancer_test(test_chercher)
    lancer_test(test_supprimer_cellule)
    lancer_test(test_fusionner)