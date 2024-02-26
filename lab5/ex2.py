import re 
str = 'gdsjkhfj abbkbnjf jkhjd aabbb'
pup = 'a{1}b{2,3}'
pip = re.findall(pup,str)
print(pip) 