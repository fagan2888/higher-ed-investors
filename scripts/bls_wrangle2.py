__author__ = 'bomba_000'

"""
Pulling data from a csv and stripping away extraneous characters,
then writing to a new txt file - this does not address the '#' place-holders included in the OES xls files
"""

import csv

origin = raw_input("What is the name of your source file?")
output = raw_input("Please provide a name for your new file.")
ifile = open(origin,"rb")
reader = csv.reader(ifile)
ofile = open(output,"wb")
writer = csv.writer(ofile, delimiter = ';')
for row in reader:
    row = [x.strip(' ') for x in row]
    for i, v in enumerate(row):
        row[i] = v.replace(",","")
        row[i] = v.replace("*","")
    writer.writerow(row)

ifile.close()
ofile.close()