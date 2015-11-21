# La bibliothèque functools

La bibliothèqe `functools` permet de définir des fonctions d'ordre supérieur, c'est-à-dire des fonctions qui opérent sur des fonctions.

Méthode | Fonction
------- | --------
cmp_to_key | 
lru_cache | 
total_ordering | 
partial | 
partialmethod | 
reduce | 
singledispatch | 
update_wrapper | 
wraps | 


## Partiels

La méthode `partial()` crée un objet qui admet trois arguments

* __func__ : le nom de la fonction
* __args__ : une liste, éventuellement partielle, d'arguments _positionnels_ (les plus à gauche)
* __keywords__ : une liste, éventuellement partielle, d'arguments _nommés_ (les plus à gauche)

Les partiels sont très commodes pour définir des fonctions comme valeur de retour, et en particulier comme mécanisme de __curryfication__.

```python
from functools import partial
basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
basetwo('10010')
18
``