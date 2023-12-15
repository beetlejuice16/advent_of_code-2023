import string

with open("./input.txt", mode='r') as f:
    print((f.readline().strip(string.ascii_letters)))
    # print(int(f.readline().strip(string.ascii_letters)))
