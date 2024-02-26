import re
str = "dhDFGHjzkcjk'zxckxz_kjzxkjckxzj"
pup = r'[A-Z][a-z]+'
pip = re.findall(pup, str)
print(pip)