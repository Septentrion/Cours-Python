# Syntaxe des expressions régulières

## Les caractères

Caractère | Signification
--------- | -------------
a | Tout caractère ASCII peut faire partie d'une expressin régulière
\u064B | Tout caractère Unicode peut faire partie d'une expressin régulière
[abc] | Les crochets délimitent un ensemble de caractères possibles
[a-z] | Le tiret à l'intérieur des crochets permet de définir un intervalle
[a\-z] | Le _backslash_ est le caractère d'échappement. Ici l'ensemble contient trois caractères et non les 26 lettres minuscules
[^0-9] | le `^`prend l'ensemble complémentaire à celui décrit
^ | correspond au début de ligne
$ | correspond à la fin de ligne
\w | Tout caractère alphanumérique
\d | Tout chiffre
\b | Délimiteur de mots
\s | Tout caractère d'espacement (y compris les tabulations)
\n | Saut de ligne
. | Joker représentant n'importe quel caractère

## Les quantificateurs

Symboles | Signification
--------- | -------------
? | Motif présent une fois ou zéro
+ | Motif présent une fois ou plus
* | Motif présent zéro fois ou plus
{2} | Entre accolades, on peut préciser un nombre d'occurences déterminées
{3,5} | Détermine un intervalle de répétitions possibles

Tous les quantificateurs sont par défaut __voraces__ : ils choisissent la chaîne la plus longue possible. Pour obtenir un comportement __économe__, on les fait suivre d'un `?`

```python
[a-z]{1,8}?
```

## Groupes et alternatives

Symboles | Signification
--------- | -------------
| | Le _pipe_ définit une alternative dans le motif à rechercher
(.*) | Les parenthèses enclosent un groupe, dont la fonction proincipale est de __capturer__ une partie d'un motif
(?:.*) | Syntaxe pour une groupe non capturant
(?P<name>) | Définition d'un groupe nommé (qui peut être réutilisé plus loin)
(?P=name) | Référence arrière à un groupe nommé
(?=) | Lookahead : Vérifie la présence de l'expression dans la _consommer_
(?!) | Lookahead négatif : Vérifie l'absence de l'expression suivante dans la _consommer_
(?<=) | Lookbehind : Vérifie la présence de l'expression (en arrière) dans la _consommer_
(?<!) | Lookabehind négatif : Vérifie l'absence de l'expression suivante dans la _consommer_


