priorities_sum1 = 0
priorities_sum2 = 0

# Convert character to integer according to Unicode
# then decode to priorities described in task:
#    - Lowercase item types a through z have priorities 1 through 26.
#    - Uppercase item types A through Z have priorities 27 through 52.
def decode_priorities(supplies):
    for ele in supplies:
        if 97 <= ord(ele) <= 122:
            return ord(ele) - 96
        elif 65 <= ord(ele) <= 90:
            return ord(ele) - 38
        else:
            raise ValueError("Invalid type of element: " + str(ele) + " allowed types are a-z and A-Z")

# Task one
with open("input/3dec.txt") as file:
    read = file.readlines()
    for line in read:
        line = line.strip()
        items_len = len(line)

        if int(items_len) % 2 != 0:
            raise ValueError("Invalid input data, number of items in rucksack must be even. Items: " + str(line))

        comp_len = int(items_len / 2)

        # divide input for two compartments
        first_comp = set(line[:comp_len])
        second_comp = set(line[comp_len:])

        # find duplicated element, decode it priority value and add to
        priorities_sum1 += decode_priorities(first_comp.intersection(second_comp))


# Task two

# iterate every 3 rucksacks
# find intersection between first two rucksacks
# and then between found intersection and 3 rucksack
# decode to appropriate priority

for n in range(0, len(read), 3):
    inter = set(read[n].strip()).intersection(read[n+1].strip())
    inter = inter.intersection(read[n+2].strip())
    priorities_sum2 += decode_priorities(inter)

print("Answer to task 1: Sum of priorities of duplicated items is: " + str(priorities_sum1))
print("Answer to task 2: Sum of priorities of repeated items for every group of 3 elfs  " + str(priorities_sum2))