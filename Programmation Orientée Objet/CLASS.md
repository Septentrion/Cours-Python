# Les classes dans Python

## Création d'une classe

Une classe est définie par son nom, et regroupe des _déclarations_ (statements) qui sont principalement des variables et des fonctions. Dans le langage des objets :

* variable => propriété
* fonction => méthode

Une classe simple s'écrit ainsi :

```python
class Carre :
    cote = 50

    def perimetre(self) :
        return self.cote * 4
 ```

__N.B.__ : Dans les méthodes, le premier argument dans la signature est toujours l'objet lui-même. Celui-ci est dénoté par le mot-clef `self`.

## Instanciation

L'instanciation se fait très simplement en apelant le nom de la classe :

```python
carre_1 = Carre()
```

## Constructeur

Les classes Python possèdent un certain nombre de _méthodes spéciales_ prédéfinies dont le nom est entouré par deux caractères `_`.

La première de ces méthodes est le constructeur : `__init__`. Cette méthode est exécutée automatiquement lors du processus d'instanciation, et permet notamment d'affecter des valeurs initiales aux propriétés de l'objet.

```python
class Carre :
    def __init__(self, cote) :
        self.cote = cote

    def perimetre(self) :
        return self.cote * 4
```

__N.B.__ : On remarque que les propriétés n'ont pas besoin d`être déclarées préalablement dans la classe. Ceci n'est pas le cas dans de nombreux langages objet.

Inversement, il existe un _destructeur_, la méthode `__del__`, qui est exécutée lorsque l'objet est détruit.

Le destructeur peut être appelé soit par le _ramasse-miettes_ (garbage collector), soit explicitement par la fonction `del`.




