import re 
str = 'jkhkdkjsk_kcm'
pep = re.split(r'_', str)
pop = pep[0]
for word in pep[1:]:
    pop+=word.capitalize()
print(pop)