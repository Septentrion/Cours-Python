# Les ensembles

Les ensembles supportent notamment les opérations... ensemblistes.

Opérateur | Fonction
------- | --------
len(ens) | Cardinal de l'ensemble
e in ens | e appartient à ens
e not in ens | e n'appartient pas à ens
e1.issubset(e2) | e1 <= e2
e1.issuperset(e2) | e1 >= e2
e1.union(e2) | union de e1 et e2 (aussi e1|e2) 
e1.intersect(e2) | intersection de e1 et e2 (aussi e1&e2)
e1.difference(e2) | e1 - e2
e1.symmetric_difference(e2) | l'union - l'intersection 

Les `frozenset`sont immuables, mais les `set`admettent aussi des méthodes pour mdifier leur contenu.


Opérateur | Fonction
------- | --------
e1.update(e2) | ajouter les éléments de e2 à e1 (aussi e1|=e2)
e1.intersection_update(e2) | conserve juste les éléments communs (aussi e1&=e2)
e1.difference_update(e2) | conserve juste les éléments non contenus dans e2 (aussi e1-=e2)
e1.symmetric_difference_update(e2) | conserve juste les éléments non communs (aussi e1^=e2)
add | 
remove | 
pop | 
discard | 
clear | 
