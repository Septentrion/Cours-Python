# La Programmation Orientée Objet

# Fondements

Il existe (au moins) trois _saveurs_ de la programmation objet, qui sont :

* Les langages à base de classes (comme C++, PHP5, Python, etc.)
* Les langages à prototypes (comme JavaScript) – ex langages de frames
* Les langages d'acteurs, plus rares (cf. Akka) – utilisés notamment pour le temps-réel

## Les langages à classes

Les langages à classes se définissent par la prodédure d'instanciation. Une classe est une matrice qui engendre, par le biais d'un _constructeur_, une instance qui est l'entité concrète qui va entrer en jeu dans le programme.

La POO est définie par quatre principes :

* L'__héritage__, qui permet d'organiser des classes en une taxonomie de plus en plus spécialisée
* L'__encapsulation__, qui détermine ce qui est public ou privé, i.e. ce qui est accessible en dehors du périmètre de l'objet
* Le __polymorphisme__, qui permet au programme de déterminer lors de l'exécution quelle méthode appliquer en fonction du type des objets
* La __délégation__, qui permet à un objet de déléguer à un autre objet le soin de répondre à un « message ».