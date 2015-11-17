# Déclenchement d'une exception

Il est possible de déclencher une exception, et cela peut se faire dans deux cas de figures :

1. On souhaite étendre le champ d'exceptions existentes
1. On souhaite créer ses propres classes d'exceptions


## Mécanisme

Une exception est levée « manuellement » par la clause `raise`.

```python
try:
  raise NameError('HiThere')
except NameError:
  print('An exception flew by!')
```

Dans l'exemple, on voit qu'il est possible de passer des valeurs à l'exception. Celles-ci peuvent ensuite être récupérées dans les clauses except en nommant l'objet.

__N.B. :__ `raise`peut être redéclarée à la fin d'une exception si elle n'a pas été traitée.

## Manipuler l'objet Exception

Pour avoir accès aux données liées à l'erreur, il suffit de nommer cet objet avec `as :

```python
try:
   raise Exception('spam', 'eggs')
except Exception as inst:
   print(type(inst))    # the exception instance
   print(inst.args)     # arguments stored in .args
   print(inst)          # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
   x, y = inst.args     # unpack args
   print('x =', x)
   print('y =', y)
```

## Créer ses propres classes d'exception

Une classe d'exception peut se créer très simplement en spécialisant la classe `Exception`.


```python
class AdHocError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
```

* Le constructeur `__init__` permet de déclarer des arguments attendus.
* La méthode `__str__`sérialise l'objet et permet de définir le message d'erreur associé à l'exception.

