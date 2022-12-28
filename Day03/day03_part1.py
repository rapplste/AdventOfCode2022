#!/usr/bin/python

# Open a file
file = open("./input.txt", "r")

sum = 0
lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_letters = []
index = 0
idx = 0
group = []
group_sum = 0

for letter in lower_letters:
    upper_letters.append(letter.upper())

all_letters = lower_letters + upper_letters
#print(all_letters)

def calc_group(group):
    tmp = ''
    sum = 0
    #print(group)

    # Find the longest string in the list
    group.sort(reverse = True, key=len)
    #print(group)

    for letter in group[0]:
        if letter in group[1] and letter in group[2] and letter != tmp:
            #print(letter)
            index= all_letters.index(letter)+1
            #print(index)
            tmp = letter
    return index

for line in file:
    half_len = int(len(line)/2)
    first_part = line[:half_len]
    sec_part = line[half_len:]

    #print(line.strip())
    #print(first_part)
    #print(sec_part)

    tmp = ''
    for l in first_part:
        if l in sec_part and l != tmp:
            #print(l)
            index= all_letters.index(l)+1
            #print(index)
            sum += index
            #print(f'{sum}\n')
            tmp = l

    # Part 2:
    group.append(line.strip())
    
    if idx == 2:
        #print(group)
        tmp_sum = calc_group(group)
        group_sum += tmp_sum
        #print(group_sum)
        
        idx = 0
        group.clear()
    else:
        idx += 1


# Close opend file
file.close()

print(f'Solution of Part1: {sum}')
print(f'Solution of Part2: {group_sum}')