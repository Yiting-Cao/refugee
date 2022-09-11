import os
import func

indexes = ['crime', 'gdp', 'employment', 'corruption', 'inequality', 'law', 'right', 'security', 'conflict', 'health']

countries = ['uk', 'france', 'germany', 'us', 'afghanistan']
# countries = ['sudan']

date = '20210315' # change date here

for country in countries:
    in_parent = 'tweets/' + country + date + '/'
    out_parent = 'rawdata/' + country + date

    # for index in indexes:
    #     in_path = in_parent + index
    #     files = os.listdir(in_path)
    #     out_file = out_parent + index + '.txt'
    #     with open(out_file, 'w') as outfile:
    #         for file in files:
    #             in_file = in_parent + index + '/' + file
    #             # print(in_file)
    #             l = func.turn_file_into_list(in_file)
    #             outfile.write(str(l))
    #         outfile.close()

    out_file = out_parent + '.txt'
    with open(out_file, 'w') as outfile:
        for index in indexes:
            in_path = in_parent + index
            files = os.listdir(in_path)
            for file in files:
                in_file = in_parent + index + '/' + file
                # print(in_file)
                try:
                    l = func.turn_file_into_number(in_file)
                    outfile.write(str(l))
                    outfile.write(', ')
                except UnicodeDecodeError:
                    pass
            outfile.write('\n')
        outfile.close()
