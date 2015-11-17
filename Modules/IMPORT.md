# La gestion des dépenances avec `import`


## Introduction

`import` permet de charger des bibliothèques dont vont dépendre les traitements.

La bibliotèque standard `sys` dispose d'un tableau `sys.path` qui contient, comme la variable PATH d'UNIX, tous les répertoires dans lesquels des modules sont accessibles. Donc Python va successivement chercher dans :

1. le répertoire courant du module appelant
1. les répertoires contneus dans `sys.path`
1. des répertoires dépendant de la configuration système

Ainsi, il suffit d'écrire la ligne suivante pour que les déclarations soient accessibles :

```python
import mon_module
```

Il est possible de faire des imports partiels avec la syntaxe :

```python
# import partiel
from mon_module import f, g, une_classe

# équivaut (presque) à l'import global
from mon_module import *
```

En utilisant `from`, on fait disparaître la référence au module. Il se peut donc que cela crée des conflits de nommage, auquel cas, le dernier à parler (importé) à raison.