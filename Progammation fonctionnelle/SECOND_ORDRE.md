## Les fonctions de second ordre

Parmi les fonctions prédéfinies de Pyrhon on trouve `map` et `filter`. Leur rôle est d'appliquer une fonction à un itérable pour obtenir un autre itérable.

Dans toutes ces fonctions, un nom de fonction est passé en argumnent.

### map

`map` applique à chaque élément de l'itérable la fonction indiquée

```python
def sqr(x) : return x ** 2

liste = [1,2,3,4,5]
r = range(20)

list(map(sqr, liste))
list(map(sqr, r))
```

La fonction map admet autant de paramètres que la fonction appliquée, ceux-ci étant des listes.

```python
def pw(x, y) : return x ** y

liste = [1,2,3,4,5]

list(map(pw, liste, [3]*len(liste)))
```


### filter

`filter` retourne une liste de tous les éléments pour lesquelles la fonction appliquée retourne `True`

```python
def pair(x) : return (x ** 3) % 2 == 0

r = range(20)

list(map(pair, r))
```


### reduce

`reduce` a un fonctionnement un peu plus complexe, car c'est un accumulateur.

```python
def acc(x, y) : return x + y

import functools
functools.reduce(acc, range(10))
```

__N.B.__ : En Python, la fonction reduce est définie dans la bibliothèque `functools`, évoquée un peu plus loin.


## Composition

Naturellement,ces fonctions (hormis `reduce`) opérant comme des lois de composition interne, elles peuvent tout à fait être enchaînées.

```python
list(filter(pair, map(pw, liste, [5]*len(liste))))
```

Pour rendre la chose plus simple et plus lisible, Python admet une syntaxe dite _en compréhension_.

```python
[ x ** 2 for x in range(20) if x % 2 == 0]
```

1. Les `[ ... ]` œuvrent comme un `map`
1. On déclare la fonction appliquée
1. le `for ... in ...` definit l'ensemble support
1. le `if ...` définit un filtre

Par suite :

```python
# reduce
functools.reduce(acc, [ x ** 2 for x in range(20) if x % 2 == 0])
# composition
[ x ** 2 for x in [ x ** 2 for x in range(20) if x % 2 == 0] if x ** 2 < 1000]
```