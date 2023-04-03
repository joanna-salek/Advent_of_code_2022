me2opp = {"X": "A", "Y": "B", "Z": "C"}
score_board = {"A": 1, "B": 2, "C": 3}

lose = {"A": "C", "B": "A", "C": "B"}
win = {v: k for k, v in lose.items()}

points_task_one = 0
points_task_two = 0


def battle(me, opp):
    if me == "C" and opp == "A":
        return 0
    elif me == "A" and opp == "C":
        return 6
    elif me < opp:
        return 0
    elif me > opp:
        return 6
    elif me == opp:
        return 3
    else:
        raise ValueError("Unsupported battle scenario. Me: " + str(me) + ", Opponent: " + str(opp))


with open("input/2dec.txt") as file:
    for line in file.readlines():
        second_sign = line[2]
        opp = line[0]

        # task one
        points_task_one = points_task_one + battle(me2opp[second_sign], opp) + score_board[me2opp[second_sign]]

        # task two
        if second_sign == "X":
            me = lose[opp]
        elif second_sign == "Y":
            me = opp
            points_task_two += 3
        elif second_sign == "Z":
            me = win[opp]
            points_task_two += 6
        else:
            raise ValueError("Unsupported strategy. Strategy: " + str(second_sign))

        points_task_two += score_board[me]

print("Answer to task 1: My total score according to plan " + str(points_task_one))
print("Answer to task 2: My total score according to plan " + str(points_task_two))
