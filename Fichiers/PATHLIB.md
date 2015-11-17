# La bibliothèque pathlib


Ce module offre des classes qui permettent de gérer des systèmes de fichiers indépendamment du système d'exploitation. Les classes Path sont divisées en :

* _Pure paths_, qui sont des représentations « abstraites »
* _Concrete paths_, qui sont héritent des premiers mais implémentent l'interface I/O

## PurePath

[Documentation de la classe PurePath](https://docs.python.org/3/library/pathlib.html#pure-paths)

Méthode | Fonction
------- | --------
parts | 
drive | 
root | 
anchor | 
parents | 
parent | 
name | 
suffix | 
stem | 
as_uri | 
is_absolute | 
joinpath | 
match | 
relative_to | 


## ConcretePath

[Documentation des classes ConcretePath](https://docs.python.org/3/library/pathlib.html#concrete-paths)

Méthode | Fonction
------- | --------
cwd | 
home | 
chmod | 
exists | 
expanduser | 
glob | 
is_dir | 
is_file | 
is_socket | 
is_fifo | 
iterdir | 
mkdir | 
open | 
owner | 
read_bytes | 
read_text | 
rename | 
replace | 
resolve |
rmdir |
samefile |
symlink_to |
touch |
unlink |
write_bytes |
write_text |
