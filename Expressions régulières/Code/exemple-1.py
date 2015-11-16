import re

pattern = re.compile("d")
print (pattern.search("dog"))    # Match at index 0
print (pattern.search("dog", 1))  # No match; search doesn't include the "d"