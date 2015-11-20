# Les booléens

Sont considéré comle `False`:

* `None`
* `False`
* Zéro : 0 ou 0.0 ou 0j (complexe)
* Les séquences vides
* Les dictionaires vides
* Les instances de classes qui définissent une méthode `__bool__` quand elle retourne `False`

Tout autre valeur est considérée comme `True`

## Les opérateurs

Opérateur | Fonction
------- | --------
or | Le second terme est évalué seulement si le premier est `False`
and | Le second terme est évalué seulement si le premier est `True`
not | 

## Les comparaisons

Opérateur | Méthode | Fonction
------- | --------  | --------
< | __lt__ | 
<= |  __lte__ | 
> |  __gt__ | 
>= |  __gte__ | 
== |  __eq__ | 
!= | 
is | | pas de méthode pour les objets
is not | pas de méthode pour les objets
in | | supporté seulement pour les séquences
not in | | supporté seulement pour les séquences

__N.B.__ : Python n'admet par de comparateur `===` permettant de de définir une égalité forte :

```python
3 == '3' # False
```
