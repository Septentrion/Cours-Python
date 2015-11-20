# La délégation

La délégation a un rapport avec la dépendance et à la composition. En ce sens, il offre un mécanisme cimplémentaire à l'héritage.

La délégation consiste pour un objet à déléguer à un autre objet la respnsabilité de calculer la réponse à un message.

> L'héritage est une forme de délégation puisque si un objet ne connaît pas une méthode, il peut demander à ses ancêtres s'ils la connaissent.

Pour cela, on tire parti de capacités _fonctionnelles_ de Python, qui autorise à passer des fonctions (ou des classes) en argument d'une fonction.

```python
class Moteur:
   def __init__(self, rendement):
       self.rendement =  rendement

   def calcul_rendement(self, arg):
       self.delegate = rendement(arg)
       return sel.delegate.calcul()
```

On obtient un mécanimse beaucoup plus souple que celui de l'héritage pour créer des liens entre classes