import re

pattern = re.compile(u'[d\u064B]')
print (pattern.search('بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ'))    # Match at index 0
print (pattern.search("dog", 1))  # No match; search doesn't include the "d"