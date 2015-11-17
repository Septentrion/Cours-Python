# Un programme principal

Exécuter un module Python automatiquement au chargement (comme programme principal) se fait très simplement par la syntaxe :

```python
def main()
    if argv is None:
        argv = sys.argv
    else:
        ma_variable = argv[1]

if __name__ == __main__:
    sys.exit(main())
```

Lorsqu'un module est appelé directement par l'interpréteur, son nom est `__main__`, contrairement à ce qui se passe si un module est appelé comme dépendance d'un autre module.

Dès lors on exécute une fonction prédéfinie à laquelle on peut passer des arguments comme on le ferait pour un programme en C.

L'indice 0 tableau `argv` contient le nom du module et peut être modifié par l'option `-c`.

Le module `sys` donne accès à une vaste collection d'informations sur l'environnement système. La méthode `sys.exit()` assure que les exceptions levées lors de l'exécution seront honorées avant la terminaison du programme.
