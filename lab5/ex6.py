import re 
str = 'dfghjk fghjkl fghjk fghj ,. , . jiu i'
pup = r'[ ,.]'
pop = re.sub(pup,':',str)
print(pop)