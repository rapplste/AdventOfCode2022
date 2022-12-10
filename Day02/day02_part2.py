#!/usr/bin/python

# Open a file
file = open("input.txt", "r")

inputdata: list[str] = []

for line in file:
    tmp = line.rstrip().replace(' ','')
    inputdata.append(tmp)

# Close opend file
file.close()
#print(inputdata)

def calc(changedinputdata):
    sum = 0
    for data in changedinputdata:
        if data == 'CX' or data == 'AY' or data == 'BZ':
            sum = sum + 6
        elif data == 'AX' or data == 'BY' or data == 'CZ':
            sum = sum + 3


        if data[1] == 'X':      # stone
            sum = sum + 1
        elif data[1] == 'Y':    # paper
            sum = sum + 2
        elif data[1] == 'Z':    # scissors
            sum = sum + 3

    print(sum)

def winloosedrawchange() -> list:
    inputdatacopy = inputdata.copy()
    newdata: list[str] =[]

    for data in inputdatacopy:
        # X means loose
        if data[1] == 'X':
            if data[0] == 'A':
                data = 'AZ'
            elif data[0] == 'B':
                data = 'BX'
            elif data[0] == 'C':
                data = 'CY'

        # Y means draw
        elif data[1] == 'Y':
            if data[0] == 'A':
                data = 'AX'
            elif data[0] == 'B':
                data = 'BY'
            elif data[0] == 'C':
                data = 'CZ'
            
        # Z means win
        elif data[1] == 'Z':
            if data[0] == 'A':
                data = 'AY'
            elif data[0] == 'B':
                data = 'BZ'
            elif data[0] == 'C':
                data = 'CX'

        newdata.append(data)

    return newdata

changedinputdata = winloosedrawchange()
#print(f'\n{changedinputdata}\n')
calc(changedinputdata)
