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
Couples= {(Alien.Nom, Alien.NoCabine for NoAllee in Cabine) for Alien in BaseAliens}
print("4. La réponse est ",Couples)

### Question 5 : quel est l'ensemble de tous les aliens de l'allée 2 ?

### Question 6 : quel est l'ensemble de toutes les planètes dont sont originaires les aliens habitant une cellule de numéro pair ?

### Question 7 : quel est l'ensemble des aliens dont les gardiens sont originaires de Terminus ?

### Question 8 : quel est l'ensemble des gardiens des aliens féminins qui mangent du bortsch ?

### Question 9 : quel est l'ensemble des cabines dont les gardiens sont originaires de Terminus ou dont les aliens sont des filles ?

### Question 10 : Y a-t-il des aliments qui commencent par la même lettre que le nom du gardien qui surveille l'alien qui les mange ?

### Question 11 : Y a-t-il cdes aliens originaires d'Euterpe ?

### Question 12 : Est-ce que tous les aliens ont un 'x' dans leur nom ?

### Question 13 : Est-ce que tous les aliens qui ont un 'x' dans leur nom ont un gardien qui vient de Terminus ?

### Question 14 : Existe-t-il un alien masculin originaire de Trantor qui mange du Bortsch ou dont le gardien vient de Terminus ?
