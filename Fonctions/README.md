# Les fonctions

Un fonction est déclarée par le mot-clef `def`.

```python
def fib(n) :    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
```

__N.B.__ : La chaîne de caractères sur la ligne qui suit la déclaration de fonction est appelée __chaîne de documentation__


## Arguments optionnels

On peut fournir des valeurs par défaut arguments des fonctions en les plaçant dans la signature :

```python
def fib(n=1) :    # write Fibonacci series up to n
    pass
```

* Les valeurs par défaut ne sont pas des constantes, mais sont évaluées lors de l'exécution du programme.
* Néanmoins, la valeur est évaluée une seule fois, lors du premier appel de la fonction.

## Paramètres nommés

Les appels de fonctions admettent le nommage des paramètres, conformément à la signature de la fonction

```python
def diff (a, b) :
    return a-b

x = diff(b=5, a=8) # Retourne 3 

## Arguments arbitraires

Une fonction peut admettre un argument arbitraire en préfixant le nomde l'argument par le caractère `*`.

```python
def g(a, b, *c) :
   print(c)	

g(1,2,3,4,5) # Affiche 3,4,5
```
La notation `*` peut servir également à « décompacter » une liste.

```python
segment = [0,15]
list(range(*segment)) # Equivaut à list(range(0,15))
```

Enfin, il est possible de passer une liste d'arguments via un dictionnaire en utilisant la syntaxe `**`

```python
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
...
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

## Fonctions anonymes

[Voir le chapitre sur la programmation fonctionnelle](../Programmation%20fonctionnelle/README.md)


