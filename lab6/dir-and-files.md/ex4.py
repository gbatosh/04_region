import os
path = r'новый_файл.txt'
with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in ', len(lines))