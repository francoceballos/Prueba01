# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:

#ver https://docs.python.org/3/library/json.html

import json

fd_csvfile = open('csv_file.txt', 'r')
list_csv = fd_csvfile.readlines()
fd_csvfile.close()

Key_list = ['club', 'city', 'country']
dic_key_csv = []

for line in list_csv:
    values_csv = line.strip().split(',')
    values_json = dict(zip(Key_list,values_csv))  #https://likegeeks.com/es/funcion-zip-de-python/

    dic_key_csv.append(values_json)

file = open('json_file.txt', 'w')
json.dump(dic_key_csv, file)
file.close()
