#ex3
def solve(numlegs,numheads):
    rabbit = (numlegs-numheads*2)/2
    chicken =(numheads-rabbit)
    print(chicken,rabbit)
solve(32,11)