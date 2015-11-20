# L'encapsulation

L'encapsulation traite de l'interface des objets avec leur environnement, c'est-à-dire de ce qu'ils _exposent_ aux autres objets.

En d'autres termes, tout objet a une partie publique et une partie privée.

## Propriétés privées

Pour Python, cependant, toutes les composantes d'un objet sont publiques.

Néanmoins, il est possible de protéger des propriétés ou des méthodes en faisant précéder leur nom de deux caractères `_`(au moins) et en fasant suivre leur nom d'un caractères `_` (au plus).

Dans ce cas, l'accès est syntaxiquement protégé car le nom interne de la propriété devient préfixé par le nom de la classe.

```python
class Carre2(Rectangle):
  def __init__(self, cote):
    self.__longueur = cote
    self.__largeur = cote

y = Carre2(10)
y._Carre2__largeur

```

Il et alors nécessaire de définir des accesseurs (`get_`) des des mutateurs (`set_` et `del_`) pour faciliter la manipulation de ces propriétés. Tous ces accesseurs peuvent être regroupés par la fonction `property`, qui sert à définir une propriété.

```python
largeur = property(get_largeur, set_largeur, del_largeur, "Largeur du carré")
```


## Propriétés de classe, propriétés d'instance

Il est quelquefois nécessaire de dissocier les propriétés des objets (ce qui est contingent) des propriétés des classes (ce qui est nécessaire).

En Python, toute propriété définie dans la portée de la classe est une propriété de classe, contrairment aux propriétés définies dans les méthodes comme le constructeur.

Ainsi, on peuttout à fait écrire :

```python
class Carre:
   cotes = 4

Carre.cotes # affiche 4
```

Néanmoins, à l'inverse de langages comme PHP5, Java et autres, il n'y a pas de distinction claire car les propriétés de classe sont également des propriétés des instances.

De même, il est possible de définir des méthodes de classe en utilisant une _annotation_ : `@staticmethod`

```python
class Carre:
    @staticmethod
    def hasCotes():
        return Carre.cotes
```







