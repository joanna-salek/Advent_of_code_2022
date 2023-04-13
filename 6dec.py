with open("input/6dec.txt") as file:
    code = file.read()

def find_marker(k):
    # divide code to k element sequences
    for n in range(len(code) - (k + 1)):
        seq = code[n:n + k]

        # if no duplicate chars in string break loop
        # and return position index+1 of last char in sequence
        if len(set(seq)) == len(seq):
            return n+k
print ("Before the first start-of-packet marker is detected we need to procces " + str(find_marker(4)) + " characters")
print ("Before the first start-of-message marker is detected we need to procces " + str(find_marker(14)) + " characters")

