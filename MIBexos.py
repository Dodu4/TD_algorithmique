# -*- coding: utf-8 -*-

from MaBase_MIB import *

### Question 1 : quel est l'ensemble des gardiens?
les_gardiens = {gardien.Nom for gardien in BaseGardiens}



les_gardiens = {gardien.Nom for gardien in BaseGardiens}

In [16]: les_villes_agents = {agent.Ville for agent in BaseAgents}

In [17]: les_villes_agents
Out[17]: {'Hesperos', 'Kalgan', 'Terminus', 'Uco'}


In [18]: triples = { (alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens  for gardien in BaseGardiens if gardien.NoCabine == alien.NoCabine}

In [19]: triples
Out[19]: 
{('1', 'Zorglub', 'Branno'),
 ('2', 'Blorx', 'Darell'),
 ('3', 'Urxiz', 'Demerzel'),
 ('4', 'Darneurane', 'Seldon'),
 ('4', 'Zbleurdite', 'Seldon'),
 ('6', 'Mulzo', 'Hardin'),
 ('7', 'Zzzzzz', 'Trevize'),
 ('8', 'Arghh', 'Pelorat'),
