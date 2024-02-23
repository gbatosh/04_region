def pup(n):
    for i in range(-n,1):
        yield i
n=12
s=pup(n)
for i in s:
    print(i*(-1))
    