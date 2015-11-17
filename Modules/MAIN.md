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