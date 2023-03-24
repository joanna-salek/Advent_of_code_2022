
def elf_calories():
    elfs = []
    calories = 0

    # Iterate over input file and count calories per elf
    with open(r"input\1dec.txt") as file:
        for line in file.readlines():
            if line.isspace():
                elfs.append(calories)
                calories = 0
            else:
                calories += int(line.strip())
    return elfs

calories = elf_calories()

# Task one:
back_up_calories = max(calories)
print ("Answer to task 1: elf carrying most calories has: ", back_up_calories,  "calories")

# Task two:
calories.remove(back_up_calories)
second_max_calories = max(calories)
back_up_calories += second_max_calories

calories.remove(second_max_calories)
back_up_calories += max(calories)
print ("Answer to task 2: 3 elfs carrying most calories have: ", back_up_calories,  "calories")