# Les itérateurs

Les itérateurs sont une autre manière de gérer des flux de données. Au contraire des générateurs qui snt des fonctions, les itérateurs sont des types.

Les itérateurs définissent deux méthodes spéciales : `__iter__` et `__next__`

* `__iter__` renvoie l'objet lui-même
* `__next__` calcule la valeur suivante dans le flux

De surcroît, les itérateurs doivent gérer la terminaison de l'exploration. Ceci se fait en levant une exception de type `StopIteration`


```python
class Iter():
    
    current=0

    def __init__(self, stop):
        self.stop=stop

    # Définit la classe comme itérable
    def __iter__(self) :
        return self
    # Définit la classe comm itérateur
    def __next__(self) :
        self.current+= 1
        
        if self.current > self.stop:
            raise StopIteration

        if self.current == 5:
            return "Cinq"
        else :
            return self.current
```
