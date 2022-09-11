from os import listdir
from os.path import isfile, join
import random

path = 'data/0/'
infiles = [f for f in listdir(path) if isfile(join(path, f))]
for x in infiles:
    if not x.endswith('.txt'):
        infiles.remove(x)

for infile in infiles:
    in_file = path + infile
    print(in_file)
    for i in range(1, 5):
        out_file = in_file.replace('.txt', '') + '_' + str(i) + '.txt'
        with open(out_file, 'w') as outfile:
            with open(in_file, 'r') as infile:
                contents = [line for line in infile.readlines()]
                for content in contents:
                    numbers = content.split(', ')
                    numbers.pop(-1)
                    numbers = [float(x) for x in numbers]
                    # print(numbers)
                    for n in numbers:
                        new_n = round(n + random.uniform(-0.1, 0.1), 6)
                        while n <= -1 or n >= 1:
                            new_n = round(n + random.uniform(-0.1, 0.1), 6)
                        outfile.write(str(new_n))
                        outfile.write(', ')
                    outfile.write('\n')
                infile.close()
            outfile.close()
            print(out_file, 'completed')

