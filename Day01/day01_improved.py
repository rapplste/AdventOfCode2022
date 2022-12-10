#!/usr/bin/python

# Open a file
f = open("input.txt", "r")

sum = 0
sumlist: list[int] = []

for line in f:
    if line != '\n':
        sum = sum + int(line)
    else:
        sumlist.append(sum)
        sum=0

# Close opend file
f.close()

maxthree = sorted(sumlist, reverse=True)[:3]
#print(f'Max calories: {maxthree}')

print(f'PART 1: Elf carries "{maxthree[0]}" calories!')

maxsum=0
for num in maxthree:
    maxsum += num
print(f'PART 2: Top three elfs carring "{maxsum}" calories!')
