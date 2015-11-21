# Les fonctions anonymes

Une fonction anonyme est donc une fonction qui n'est associée à aucun symbole, et qui n'a donc aucune existence dans la table des symboles du programme.

Elle est introduite par le mot-clef `lambda`.

Python admet une version très restrictives des fonctions anonymes (ou lamdda-fonctions)

* La fonction doit tenir sur une ligne
* Le corps de la fonction consiste en une expression unique
* La portée des varaibles et purement lexicale

Dans ces conditions, il est possible d'écrire :

```python
x = lambda x, y : x ** y
```

__N.B.__ : les arguments de la fonction anonyme ne sont pas entourés de parenthèses.


## Engendrer une fonction

Un fonction peut notamment avoir pour résultat une fonction. Mais définir une fonction implique le mot-clef `def` qui est interdit dans une expression de retour.

Mais utiliser une fonctiona anonyme est possible.

``python
# La syntaxe des arguments de la lambda-fonction est dûe à la portée lexicale
def f (x, y) : return lambda x=x, y=y : x ** y

x = f(2,3)
```

