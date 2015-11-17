# Les packages

Un package n'est pas autre chose pour Python qu'un module contenant des sous-modules. En fait, tout modu ayant un attribut `__path__` est un package. 

Un package est contruit comme une arborescence de dossiers imbriqués. Chaque dossier contient lui-même des modules regroupés à l'intérieur du package.

On distingue deux types de packages :

* Les packages normaux (regular packages)
  * Ce sont des packages contenant simplement une méthode `__init__.py`
* Les packages à espace de nom (namespace packages)
  * Ces packages servent de conteneurs pour des sous-packages. Il peuvent n'avoir aucune contrepartie physique


## Construire un package

Construier un package consiste purement et simplement à créer un dossier dans un répertoire accessible depuis l'interpréteur. En pratique, les packages « métier » seront bin souvent dans le même dossier que l'application principale.

A l'intérieur du dossier, il faut créer le fichier `__init__.py`, qui peut parfaitement être vide, mais est destiné à contenir du code qui sera exécute lors de l'import du package ou de l'un de ses sous-packages.

Il suffit alors de déposer les modules que l'on souhaite regrouper dans ce package et recommencer récursivement.


## Packages à espaces de noms implicite

Il existe une autre méthode pour créer des packages, sans avoir à définir explicitement une méthode d'initialisation. On les appelle _packages à espaces de noms implicite_ parce qu'ils utilisent le tableau `sys.path` pour être trouvés.

Les portions de ces packages ne sont pas obligatoirement hébergées dans la même arborescence de dossiers., ni faire appele au même _loader_.

