# L'héritage

Toute classe Python peut hériter des propriétés et des méthodes d'une autre classe. Elle devient alors une _sous-classe_ decette dernière.

Pour ce faire, il suffit de déclarer la _classe-mère_ dans la signature de la classe :

```python
class Rectangle :
   def __init__(self, longueur, largeur) :
        self.longueur = longueur
        self.largeur = largeur

   def perimetre(self) :
       return (self.longueur + self.largeur) * 2

class Carre(Rectangle) :
    def __init__(self, cote)
        self.longueur = cote
        self.largeur = cote
```

L'héritage permet de redéfinir les méthodes pour les adapter aux class plus spécifiques. Dans notre exemple, le calcul du `perimetre`pourrait être plus simple.

## Héritage multiple

D'un point de vue théorique, l'héritage multiple pose des problèmes (cf. Diamant de Nixon). Aussi beaucoup de langages ont choisi soit de ne pas l'implémenter, soit de le contourner en ajoutant d'autres fonctionnalités (interfaces, traits, etc.)

Pyrhon posède un algorithme de résolution appelé C3 ou MRO, qui permet d'assurer la _monotonicité_ de la recherche parmi les ancêtres.

Ainsi, il est possible de définir quelque chose comme :

```python
class Vehicule
    pass

class Voiture(Vehicule)
    pass

class Avion(Vehicule)
    pass

class VoitureVolante(Voiture, Avion)
    pass
```
