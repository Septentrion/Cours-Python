# Les chaînes de caractères

Une châine de caractères est créée de deux manières :

```python
# Directement
x = 'Expression'
# Les triples quotes permettent les sauts de lignes
y = """Merci
pour
le
café"""
# Utiliser le constructeur / opérateur de transtypage
z = str('123')
```

Pour tout type, il est possible de définir une méthode spéciale `__str__` pour linéariser les objets (i.e. les convertir en chaînes de caractères)

__N.B.__ : Les chaînes de caractères sont itérables. On peut notamment écrire :

```python
for i in 'pythonesque':
  print(i+'\n')
```

## Les méthodes sur les chaînes

La bibliothèque standard dispose de [nombreuses méthodes](https://docs.python.org/3.5/library/stdtypes.html#string-methods), dont un « pretty-printer » (formatteur) : `printf`

```python
print('%(language)s has %(number)03d quote types.' {'language': "Python", "number": 2})
Python has 002 quote types.
```
