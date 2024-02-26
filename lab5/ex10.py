import re
str = "fglhjnAk"
pup = re.sub(r'(?<!^)(?=[A-Z])',r'_', str ).lower()
print(pup)
