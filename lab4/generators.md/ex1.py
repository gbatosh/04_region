def power_2(n):
    for i in range(1, n+1):
        yield i**2
n = 7
gen = power_2(n)
for s in gen:
    print(s,end = " ")
