

import random as rd
mu = 1
nu = 1

def make_liste_arrivees(n):
    t = 0
    liste_arrivees = []
    for i in range(n):
        t += rd.expovariate(mu)
        liste_arrives.append(t)
    return liste_arrivees

class Individu:
    def __init__(self):
        self.numero = 0
        self.temps_arrivee = -10
        self.temp_service = -10

class File:
    def __init__(self):
        self.data = []
        self.mu = 1
        self.nu = 0.5
        self.liste_taille = []
    def enfiler(self,elt):
        self.data.append(elt)
    def longueur(self):
        return len(self.data)
    def est_vide(self):
        return self.longueur() == 0
    def defiler(self):
        return self.data.pop(0)
    def dernier(self):
        return self.data[-1]
    def ajout_avec_liste(self,liste,t):
        for temps_arrivee in liste:
            if temps < t:
                if File.est_vide:
                    compteur = 0
                else:
                    dernier_individu = File.dernier()
                    compteur = dernier_individu.numero + 1
                temp_individu = Individu()
                temp_individu.numero = compteur
                self.data.append(temp_individu)
    def service(self,t_fin):
        t = 0
        t_arrivee = rd.expovariate(mu)
        t_service = 0
        while t < t_fin:
            t+= min(mu,nu)/10
            if t > t_service:
                self.liste_taille.append(self.longueur())
                if not self.est_vide():
                    self.defiler()
                    t_service = t + rd.expovariate(nu)
                    print("Service")
                    print(self.longueur())
            if t > t_arrivee:
                self.liste_taille.append(self.longueur())
                t_arrivee += rd.expovariate(mu)
                if self.est_vide():
                    compteur = 0
                    t_service = t_arrivee + rd.expovariate(nu)
                else:
                    dernier_individu = self.dernier()
                    compteur = dernier_individu.numero + 1
                temp_individu = Individu()
                temp_individu.numero = compteur
                self.enfiler(temp_individu)
                print(self.longueur())







