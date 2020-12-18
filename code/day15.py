from itertools import islice

# https://oeis.org/A181391
def van_eck(start=[]):
    seen = {}
    for i,val in enumerate(start):
        seen[val]=i
        yield val
    n, val = len(start) , 0
    while True:
        yield val
        last = {val: n}
        val = n - seen.get(val, n)
        seen.update(last)
        n += 1


if __name__ == "__main__":
    with open("inputs/day15.txt") as f:
        start = list(map(int,f.readline().split(",")))
    nth = 2020
    mth = 30000000
    print(list(islice(van_eck(start=start), nth))[-1])
    print(list(islice(van_eck(start=start), mth))[-1])