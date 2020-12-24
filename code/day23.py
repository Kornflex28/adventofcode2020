
def make_move(current_cup,cups):
    # print(f"cups: {' '.join([str(c) if c!=current_cup else f'({c})' for c in cups])}")
    n = len(cups)
    temp_cups = cups[:]
    current_idx = cups.index(current_cup)
    three_cups_idx = [(current_idx+i)%n for i in range(1,4)]
    three_cups = [temp_cups[idx] for idx in three_cups_idx]
    for c in three_cups :
        cups.remove(c)
    # print(f"pick-up: {','.join(map(str,three_cups))}")
    found_destination = False
    destination = current_cup - 1
    while not(found_destination):
        if destination < min(temp_cups):
            destination = max(temp_cups)
        if destination in three_cups :
            destination+=-1
        else:
            found_destination = True
    
    # print(f"destination {destination}\n")
    destination_idx = cups.index(destination)
    for i,c in enumerate(three_cups):
        cups.insert((destination_idx+i+1)%n,c)
    current_idx = cups.index(current_cup)
    new_current_cup = cups[(current_idx+1)%n]
    return(new_current_cup,cups)


def make_move_2(cups, n):
    cur_val = cups[0]
    max_val = max(cups)

    cups_dict = dict(zip(cups, cups[1:]))
    cups_dict[cups[-1]] = cups[0]

    def pick_up(n=3):
        pick = [cups_dict[cur_val]]
        for _ in range(n-1):
            pick.append(cups_dict[pick[-1]])
        return pick

    for r in range(n):
        pick = pick_up()

        next_val = cur_val-1
        while next_val <= 0 or next_val in pick:
            next_val -= 1
            if next_val <= 0:
                next_val = max_val

        cups_dict[cur_val] = cups_dict[pick[-1]]
        cups_dict[pick[-1]] = cups_dict[next_val]
        cups_dict[next_val] = pick[0]

        cur_val = cups_dict[cur_val]

    return cups_dict






if __name__ == "__main__":
    with open("inputs/day23.txt") as f:
        cups = list(map(int,f.readline()))
        _cups = cups[:]
    current_cup = cups[0]
    for k in range(100):
        # print(f"-- move {k+1} --")
        current_cup,_cups = make_move(current_cup,_cups)

    one_index = cups.index(1)
    out = ""
    for i in range(len(cups)):
        out+=str(_cups[(one_index+i)%len(cups)])
    print(out[1:])

    cups+= list(range(9+1, 1000000+1))
    cups = make_move_2(cups, n=10000000)
    print(cups[1]*cups[cups[1]])

