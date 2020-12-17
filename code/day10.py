def n_arr_rec(base, joltages):
    if len(joltages) == 0:
        return 0
    elif len(joltages) == 1:
        return 1
    else:
        n_arr = 0
        for i in [1, 2, 3]:
            try:
                _next = joltages.index(joltages[0] + i, 1)
                n_arr += n_arr_rec(base[:] + [joltages[0]], joltages[_next:])
            except:
                1
        return n_arr


def n_arr_part(joltages):
    jolt_diffs = [b-a for a, b in zip(joltages, joltages[1:])]
    next3 = 0
    result = 1
    while len(joltages) > 0 and len(jolt_diffs) > 0:
        next3 = jolt_diffs.index(3)
        upperlimit = next3+2
        lowerlimit = next3+1
        result *= n_arr_rec([], joltages[:upperlimit])
        joltages = joltages[lowerlimit:]
        jolt_diffs = jolt_diffs[lowerlimit:]
    return result

if __name__ == "__main__":
    with open("inputs/day10.txt") as f:
        data = sorted(list(map(int,f.read().splitlines())))
    joltages = [0]+sorted(data)+[max(data)+3]
    jolt_diffs= [b-a for a, b in zip(joltages, joltages[1:])]
    print(jolt_diffs.count(1)*jolt_diffs.count(3))
    print(n_arr_part(joltages))