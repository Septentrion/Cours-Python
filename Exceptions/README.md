# La gestion des erreurs

La gestion des erreursdans Python n'est pas très différente que celle d'autres langages et se fait via la structure `try ... except`.


## Structure de base

```python
try:
   x = int(input("Please enter a number: "))
except ValueError:
   print("Oops!  That was no valid number.  Try again...")
```

Le mot-clef `try`indique lde début du bloc de la structure de contrôle.
Si l'opétation réussit, la séquence continue en ommetant la clause `except`.
Sinon, si une erreur est détectée, la clause `except` prend le relais et examine le type d'erreur. Dans l'exemple, si l'erreur est de type `ValueError`, alors le message s'affiche

[Voir les types d'erreurs](ERREURS.md)

### Except multivalué

Une même clause peut répondre à plusieurs types d'erreurs :

```python
except (ValueError, TypeError, RuntimeError):
   print("Oops! ")
```

### Except alternatifs

De la même manière, il es possible de différencier les traitements en fonction des erreurs :

```python
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
```

### Clause else

La clause `else`, ajoutée après la liste des clauses `except` permet d'exécuter du code supplémentaire si aucune exception n'a été levée.

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

C'est une bonne pratique qui permet de séparer le traitement lui-même d'opérations annexes.

### Clause finally

Enfin, si l'on souhaite que du code soit exécuté quelle que soit la situation, il est possible d'ajouter tout à la fin du bloc une clause `finally`

```python
def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    print("division by zero!")
  else:
    print("result is", result)
  finally:
    print("executing finally clause")
```
