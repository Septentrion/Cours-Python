# IO

Le module `io` fournit une interface pour gérer des entrées/sorties qui sont de types : __text__, __binary__ ou __raw__. Les objets concrets de ces divers types sont appelés __fichiers__ (_file object_) ou aussi _streams_ et _file-like objects_.

## Classes abstraites

### IOBase

`io` fournit une hiérarchie de classes correspondant aux différents types de _flots_ (streams). La classe racine est `IOBase`. C'est une classe abstraite (pas de constructeur public).

Méthode | Fonction
------- | --------
close | 
closed | 
fileno | 
flush | 
isatty | 
readable | 
readline | 
readlines | 
seek | 
seekable | 
tell | 
truncate | 
write | 
writable | 


### RawIOBase

Méthode | Fonction
------- | --------
read | 
readall | 
readinto | 
write | 


### BufferedIOBase

Méthode | Fonction
------- | --------
detach | 
read | 
read1 | 
readinto | 
readinto1 | 
write | 


### TextIOBase

Méthode | Fonction
------- | --------
encoding | 
errors | 
detach | 
read | 
readline | 
seek | 
tell | 
write | 

## Classes concrètes

### FileIO

* Hérite de `RawIOBase`

Méthode | Fonction
------- | --------
mode | 
name |


### BytesIO

* Hérite de `BufferedIOBase`

Méthode | Fonction
------- | --------
getvalue | 


### TextIOWrapper

* Hérite de `TextIOBase`

Méthode | Fonction
------- | --------
line_buffering | 


### StringIO

* Hérite de `TextIOBase`

Méthode | Fonction
------- | --------
getvalue | 

