#ex4
def filter_prime(nums):
    li=[]
    p=0
    for i in nums:
        for j in range(i+1):
            if i % (j+1) == 0:                
                p+=1
        if p == 2:
            li.append(i)
        p=0
    return li
for i in filter_prime([1,2 ,3,4,5,7,9,11]):
    print(i)