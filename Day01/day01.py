#!/usr/bin/python

# Open a file
f = open("input.txt", "r")
#print(f'Name of the file: {f.name}')

elf1 = 0
sum = 0
tmp = 0
sumlist: list[int] = []
#maxthree:list[int] = []

for line in f:
    #print(line, end='')
    if line != '\n':
        tmp = tmp + int(line)
    else:
        elf1 += 1
        sumlist.append(tmp)
        #print(sumlist)
        if tmp>sum:
            sum=tmp
            tmp=0
        else:
            tmp=0

# Close opend file
f.close()

print(f'Elf {elf1} hat die Summe von: {sum}')

# PART TWO
maxthree = sorted(sumlist, reverse=True)[:3]
print(f'Max calories: {maxthree}')

maxsum=0
for num in maxthree:
    maxsum += num
print(f'Max calories: {maxsum}')
