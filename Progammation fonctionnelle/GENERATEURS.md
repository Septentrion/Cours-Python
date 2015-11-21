# Les générateurs

On appelle __générateur__ une fonction qui parcourt un ensemble donné pour calculer, à la demande, la valeur suivante de cet ensemble. Cet ensemble peut être fini ou infini.

En Python, un générateur est une simple fonction pourvue d'une clause `yield`


```python
def N() :
yield 'Hello, world !'
```

Une fois l'ensemble épuisé, le générateur rend une erreur.

```python
def N() :
# Parcourt les nombres entiers pairs
i = 0
while True :
  if i % 2 == 0 : yield i
  i = i + 1
```

Le contexte du générarteur est conservé pendant toute la durée de l'exécution.

La notion de générateur est inséparable de celle d'itérateur.


