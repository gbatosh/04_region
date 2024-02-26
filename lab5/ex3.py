import re
str = " dhjzkcjk'zxckxz_kjzxkjckxzj"
pup = '[a-z]_[a-z]'
pip = re.findall(pup, str)
print(pip)