from collections import defaultdict

current_path = []

# Dictionary of all paths and its sizes
all_paths = defaultdict(int)

# Dictionary for counting total sizes of directories (and all subdirectories)
hit_map = {}

# Variable for keep uniqueness of directories
counter = 0


with open("input/7dec.txt") as file:

    for line in file.readlines():
        if line.startswith("$ cd .."):
            # move up one level
            current_path.pop(-1)

        elif line.startswith("$ cd /"):
            # move up to outer most directory
            current_path = []

        elif line.startswith("$ cd"):
            # move in to directory [name]
            name = line[4:].strip()

            # if directory name already exists
            # add to it's name counter value to make it unique
            if name in hit_map.keys():
                counter += 1
                name = name + str(counter)

            # initialize values
            hit_map[name] = 0
            current_path.append(name)

        if line[0].isdigit():

            # if line starts with digit, split line and extract size
            number = int(line.split()[0])

            # add size of current directory, if current path is empty it is equal to ""
            if current_path:
                all_paths[tuple(current_path)] += number
            else:
                all_paths[""] += number

for (key, value) in all_paths.items():
    if key:
        # count and add size of all inner directories
        for r in range(1, len(key)+1):
            hit_map[key[-r]] += value


sum_of_100000_dirs = 0
dir_to_possible_delete = []

for (key, value) in hit_map.items():
    # task one
    if value <= 100000:
        sum_of_100000_dirs += value

    # task two
    if value >= 6090134:
        dir_to_possible_delete.append(value)

print("Answer to task 1: Sum of the total sizes of directories "
      "with a total size of at most 100000: "
      + str((sum_of_100000_dirs)))

print("Answer to task 2: The smallest directory that, if deleted, "
      "would free up enough space on the filesystem to run the update: "
      + str(min(dir_to_possible_delete)))
