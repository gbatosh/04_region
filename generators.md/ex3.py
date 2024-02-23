def pup(n):
    for i in range(n):
        if i%2 == 0 or i%4 == 0:
            yield i
n = int(input())
s=pup(n)
for i in s:
    print(i,end=" ")