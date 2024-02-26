import re
str = "fglhjnAk jj njk hj l"
pup = re.findall('[A-Z][^A-Z]*', str)
print(pup)
