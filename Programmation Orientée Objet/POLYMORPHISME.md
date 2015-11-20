# Le polymorphisme

Le polymorphsime est lié à la question de l'homonymie, c'est-à-dire la possibilité pour l'interpréteur de discriminer plusieurs fonctions portant le même nom, en fonctin de leur signature, au moment de l'appel de la fonction.

Il existe plusieurs formes de polymorphisme :
* Ad hoc
* Paramétré (cf. Haskell ou les templates C++, Scala)
* Par sous-typage (qui tire partie de la hiérarchie des classes)

[Polymorphiqme sur Wikipedia en)](http://www.wikiwand.com/en/Polymorphism_%28computer_science%29)

En Python les possibilités de polymorphisme sont nécessairement limitées puisque les signatures des fonctions ne sont pas typées (aps de _type hinting_).

En conséquence, on peut faire du polymorphisme par sous-typage (cf. [exemple](exemple_polymorphisme.py)), soit en profitant des méthodes spéciales permettant de redéfinir les opérateurs standard.


```python
class Vecteur:
    def __init__(self, x1, y1, x2, y2):
    	self.x1 = x1
    	self.y1 = y1
    	self.x2 = x2
    	self.y2 = y2

    def __add__(self, v):
    	xr = self.x2 + (v.x2 - v.x1)
    	yr = self.y2 + (v.y2 - v.y1)
    	resultante = Vecteur(self.x1, self.y1, xr, yr )
```

