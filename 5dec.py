from copy import deepcopy

crates_1 = {}

# prepare crates stack data from file input
with open(r"input\5dec.txt") as file:
    read = file.readlines()
    count = 0
    for line in read:
        if not line.startswith("move"):
            count += 1
            # move every 4 chars to divide data to columns
            # data looks like ----[G]-[M]-----[S]-
            for r in range(0, len(line), 4):
                # if data starts with "[" take it's index
                # and use it as key, key=index+1
                # then extract char and add it to list in
                # dictionary for it's key
                if line[r] == "[":
                    if int(r/4)+1 in crates_1.keys():
                        # add item to the front of list
                        crates_1[int(r/4)+1][:0] = line[r+1:r+2]
                    else:
                        # key don't exist so create it with new item
                        crates_1[int(r / 4) + 1] = list(line[r+1:r+2])

crates_2 = deepcopy(crates_1)

for line in read[count:]:
    # Extract instruction for moving crates:
    instruction = [int(x) for x in line.strip().split() if x.isdigit()]
    amount = instruction[0]
    from_crate = instruction[1]
    to_crate = instruction[2]

    # Part one
    # for every crate in amount, pop it from starting stack
    # and add it to target one
    for turn in range(0, amount):
        crates_1[to_crate].append(crates_1[from_crate].pop())

    # Part two
    # take slice of desire crates, add it to target stack
    # and remove it from old stack
    crates_2[to_crate] += crates_2[from_crate][-amount:]
    crates_2[from_crate] = crates_2[from_crate][: -amount]


def get_last_crate_from_each(crates):
    # take crate on top from every stack and add it to answer
    answer = ""
    for crate in sorted(crates.keys()):
        answer += crates[crate][-1]
    return answer

print("Answer to task 1: concateneited items at the top of each stack in crate: " + str(get_last_crate_from_each(crates_1)))
print("Answer to task 2: concateneited items at the top of each stack in crate: " + str(get_last_crate_from_each(crates_2)))
