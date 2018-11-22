from MaBase_MIB import *

### Question 1 : quel est l'ensemble des gardiens?
Gardien = { Gardien.Nom for Gardien in BaseGardiens }
print("1. La réponse est ",Gardien)

### Question 2 : quel est l'ensemble des villes d'origine des agents?
Villes = { Agent.Ville for Agent in BaseAgents }
print("2.La réponse est ",Villes)

### Question 3 : quel est l'ensemble des triplets (no de cabine,alien,gardien) pour chaque cabine?
Triples = { (Alien.NoCabine, Alien.Nom, Gardien.Nom)
for Alien in BaseAliens
for Gardien in BaseGardiens if Gardien.NoCabine == Alien.NoCabine}
print("3. La réponse est ",Triples)

### Question 4 : quel est l'ensemble des couples (alien,allée) pour chaque alien:
