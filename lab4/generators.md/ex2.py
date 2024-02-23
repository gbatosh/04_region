def even(n):
    f=int(n/2)+1
    for i in range(0,f):
        yield i*2
n=int(input())
p=even(n)
for i in p:
    print(i)