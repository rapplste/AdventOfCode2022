#!/usr/bin/python

# Open a file
file = open("./input.txt", "r")

sum = 0
cnt_all = 0
cnt_overlap = 0

for line in file:
    cnt_all += 1
    line = line.replace("\n", "")
    sections = line.split(',')
    first_section = sections[0].split('-')
    second_section = sections[1].split('-')

    first_range = set(range(int(first_section[0]),int(first_section[1])+1))
    second_range = set(range(int(second_section[0]),int(second_section[1])+1))

    # print(first_section)
    # print(first_range)
    # print(second_section)
    # print(second_range)
    
    if first_range.isdisjoint(second_range) == False:
        # PART TWO
        cnt_overlap +=1

        #PART ONE
        if first_range.issubset(second_range) or second_range.issubset(first_range):
            sum += 1

# Close opend file
file.close()

print(f'Cnt all lines: {cnt_all}')
print(f'Solution of Part1: {sum}')
print(f'Solution of Part2: Cnt all overlap: {cnt_overlap}')

