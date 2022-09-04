import random
in_file = 'tweets/sudan20200511/health/2020-05-11.txt'
l = []
with open(in_file, 'r') as infile:
    contents = [line for line in infile.readlines()]
    for content in contents:
        new_content = content.strip()
        new_content = float(new_content)
        l.append(new_content)
    infile.close()
l = [x for x in l if x !=0]
ll = len(l)
if ll == 0:
    n = 0.0
else:
    n = round(sum(l)/ll, 6)
print(n)

