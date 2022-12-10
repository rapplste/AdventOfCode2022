#!/usr/bin/python

# Open a file
file = open("input.txt", "r")

sum = 0
inputdata: list[str] = []

for line in file:
    tmp = line.rstrip().replace(' ','')
    inputdata.append(tmp)

# Close opend file
file.close()

for data in inputdata:
    if data == 'CX' or data == 'AY' or data == 'BZ':
        sum = sum + 6
    elif data == 'AX' or data == 'BY' or data == 'CZ':
        sum = sum + 3


    if data[1] == 'X':
        sum = sum + 1
    elif data[1] == 'Y':
        sum = sum + 2
    elif data[1] == 'Z':
        sum = sum + 3

print(sum)