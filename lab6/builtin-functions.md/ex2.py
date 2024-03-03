import re
def sort(str):
    pup = r'[a-z]'
    smallletters = re.findall(pup, str)
    pip = r'[A-Z]'
    capitalletters = re.findall(pip, str)
    print(len(smallletters),len(capitalletters))
sort('gf.jhjkaj JKLHJK FJKehfj jef ')
