from itertools import combinations

if __name__ == "__main__":
    with open("./inputs/day1.txt") as f:
        data = sorted([int(n) for n in f.readlines()])
    s = 2020
    pairs = [(a, b, a*b) for a, b in list(filter(lambda l: sum(l)
                                                 == s, list(combinations(data, 2))))]
    triples = [(a, b, c, a*b*c) for a, b,
               c in list(filter(lambda l: sum(l) == s, list(combinations(data, 3))))]
    print(pairs)
    print(triples)
