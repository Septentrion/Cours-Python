# Les séquences

Un certain nombre d'opérateurs s'appliquent spécifiquement sur les séquences :

Operateur | Resultat | Notes
--------- | -------- | -----
x in s | x est un élément de s |
x not in s | x n'est pas un élément de s |
s + t | union de s et t |
s * n or n * s | réplication n fois de s | 
s[i] | le i-ème de s |
s[i:j] | le segment entre les positions i et j de s |
s[i:j:k] | le segment entre les positions i et j de s, avec un pas de k |
len(s) | cardinal of s |  
min(s) | plus petit élément de s |  
max(s) | plus grand élément de s |  
s.index(x[, i[, j]]) | première occurrence de x dans s, avec restrictins sur les positins i et j  |
s.count(x) | cardinal des occurences de x dans s | 


D'autre opérateurs ne s'appliquent que sur les séquences variables (les `list` pour les types prédéfinis) :

Operateur | Resultat | Notes
--------- | -------- | -----
s[i] = x |  |  
s[i:j] = t | |  t doit être itérable 
del s[i:j] | efface les éléments |  
s[i:j:k] = t | | t doit être itérable 
del s[i:j:k] | |  
s.append(x) |  ajoute x à la fin de s |  
s.clear() | vide s |
s.copy() | |
s.extend(t) or s += t | | avec t itérable 
s *= n |  |
s.insert(i, x) | |  
s.pop([i]) | ôte le i-ème élément de s |
s.remove(x) | supprime la première occurrence de x |
s.reverse() | |


## Créer ses propres séquences

[Documentation officielle](https://docs.python.org/3.5/library/collections.abc.html)