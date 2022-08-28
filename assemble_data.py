import os

indexes = ['crime', 'gdp', 'employment', 'corruption', 'inequality', 'law', 'right', 'security', 'conflict', 'health']

in_parent = 'tweets/ukraine/'
out_parent = 'data/ukraine/'

for index in indexes:
    in_path = in_parent + index
    files = os.listdir(in_path)
    out_file = out_parent + index + '.txt'
    with open(out_file, 'w') as outfile:
        for file in files:
            in_file = in_parent + index + '/' + file
            # print(in_file)
            with open(in_file) as infile:
                outfile.write(infile.read())
                infile.close()
        outfile.close()
    break