# La bibliothèque pickle

La bibliothèque `pickle` est un peu à part puisque qu'elle a pour fonction de sérialiser et désérialiser les objets Python. de ce fait, il est possible de sauvegarder des données tout en conservant leurs propriétés d'objets.

> pickle replit des fonctions semblables à celles de JSON, mais avec des différences notables : le fait que ce soit un format __binaire__ et qu'il soit très spécifique à Python

`pickle` offre une interface simple pour la gestion des objets

Méthode | Fonction
------- | --------
dump | 
dumps | 
load | 
loads | 


## Pickler

Pour des opérations plus fines, on peut utiliser les classes Pickler et Unpickler.
Sont pris en charge par Pickler :

* les booléens
* les nombres (entiers, réels, complexes, etc.)
* les chaînes de caractères, tableaux, binaires
* les tuples, listes, dictionnaires, etc.
* les fonctions définies par `def`
* les fonctions définies à la racine d'un module
* les classes définies à la racine d'un module
* les instances de ces classes


### Pickler

Méthode | Fonction
------- | --------
dump | 
dispatch_table | 

### Unpickler

Méthode | Fonction
------- | --------
load | 
persistent_load | 
find_class | 


## pickletools

De plus, on peut utiliser le module `pickletools` pour analyser le contenu des _pickles_.
`piuckletools`engendre un pseudo-code sous forme de triplet : <opcode, valeur, position>

`pickletools` peut être utilisé en ligne de commande avec diverses options :

Option | Fonction
------- | --------
-a, --annotate | Annotate each line with a short opcode description.
-o, --output=<file> | Name of a file where the output should be written.
-l, --indentlevel=<num> | The number of blanks by which to indent a new MARK level.
-m, --memo | When multiple objects are disassembled, preserve memo between disassemblies.
-p, --preamble=<preamble> | When more than one pickle file are specified, print given preamble before each disassembly.

Le module dispose également d'une API :

Méthode | Fonction
------- | --------
dis | 
genops | 
optimize | 
