# Les dictionnaires

Les dictionnaires sont des conteneurs un peu particuliers, puisque les valeurs des éléments sont indexées par des clefs.

Chaque est _hachée_, donc tout objet pouvant être haché est susceptible d'être une clef.

Chaque clef est naturellement unique. En particulier la clef `1` et la clef `1.0` sont identiques.


## Les « dictionary views »

Les objetx retournés par `keys()`, `values()` et `items()` sont des _vues dynamiques_. Ainsi, si le contenu du dictionnaire change au cours de l'application, ces objets sont mis à jour automatiquement.

Ces objets sont itérables, et admenttent des méthodes particulières

Opérateur | Fonction
------- | --------
len | Taille de la vue 
iter |  retourne un itérateur sur la vue
in | retourne `True` si la valeur appartient à la vue
