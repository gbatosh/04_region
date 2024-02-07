from itertools import permutations 
def permut(str):
    a=permutations(str) 
    for i in list(a): 
        print("".join(i))
permut("ABC")