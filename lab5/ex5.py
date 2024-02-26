import re
str = "adfghjkb"
pup = r'a\w+b'
pip = re.findall(pup, str)
print(pip)