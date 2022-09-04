in_file = 'tweets/ukraine/crime/2022-05-16.txt'
import random

with open(in_file, 'r') as infile:
    contents = [line for line in infile.readlines()]
    l = []
    for content in contents:
        new_content = content.strip()
        new_content = float(new_content)
        l.append(new_content)
    infile.close()
    l = [x for x in l if x !=0]
    ll = len(l)
    if ll == 0:
        l = [0 for x in range(10)]
    if ll < 10:
        for _ in range(10-ll):
            n = round(sum(l)/ll + random.uniform(-0.1, 0.1), 6)
            l.append(n)

    print(l)

# import random

# x = random.uniform(-0.1, 0.1)
# print(x)
