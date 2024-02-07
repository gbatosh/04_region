def reverse1(s):
    a=s.split()
    a.reverse()
    for i in range(len(a)):
        print(a[i], end = " ")
s = str(input()) 
reverse1(s)
