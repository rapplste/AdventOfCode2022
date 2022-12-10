#!/usr/bin/python

# Open a file
f = open("input.txt", "r")
#print(f'Name of the file: {f.name}')

elf = 0
sum = 0
tmp = 0

for line in f:
    #print(line, end='')
    if line != '\n':
        tmp = tmp + int(line)
    else:
        elf += 1
        if tmp>sum:
            sum=tmp
            tmp=0
        else:
            tmp=0

# Close opend file
f.close()

print(f'Elf {elf} hat die Summe von: {sum}')