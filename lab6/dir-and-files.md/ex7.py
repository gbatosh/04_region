with open('ex1.txt', 'r') as f1:
    with open('ex2.txt', 'w') as f2:
        f2.write(f1.read())
        