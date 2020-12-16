from itertools import combinations 


if __name__ == "__main__":
    s = 2020
    pairs = []
    remains={}
    with open("inputs/day1.txt") as f :
        data = sorted([int(n) for n in f.readlines()])
    for n in data:
        remain = s-n
        if remain in remains:
            pairs.append((n,remain,n*remain))
        remains[n]=n
    
    triples = [(a,b,c,a*b*c) for a,b,c in list(filter(lambda l: sum(l)==s, list(combinations(data, 3)))) ]
    print(pairs)
    print(triples)