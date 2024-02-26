import re
str = "fglhjnAk"
pup = re.sub(r'(?<=[a-z])([A-Z])',r' \1', str )
print(pup)
