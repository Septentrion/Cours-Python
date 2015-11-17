import re

pattern = re.compile("d")
print (pattern.search("dog"))    # Match @ index 0
print (pattern.match("dog"))    # Match au début de la chaîne
print (pattern.search("dog", 1))  # Match @ index 1 ; Aucun résultat