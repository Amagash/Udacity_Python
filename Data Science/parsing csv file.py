# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = "/home/tiffany/lab/Udacity_Python"
DATAFILE = "beatles-discography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        print (header)
        counter = 0
        for line in f:
            if counter == 10:
                break
            fields = line.split(",")
            print (fields)
            entry = {}

            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()
            data.append(entry)
            counter += 1
    print (data)
    return data

datafile = os.path.join(DATADIR, DATAFILE)

def test():
    # a simple test of your implementation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)',
                 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum',
                 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964',
                 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline


# test()

#################################################################################
# Another way to do this with the csv module
import csv
import pprint

def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile, 'rb') as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
    return data

pprint.pprint(parse_csv(datafile))