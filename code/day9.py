from itertools import combinations

def gen_contiguous_sets(data):
    len_data = len(data)
    for first_index in range(0, len_data - 1):
        for second_index in range(first_index + 1, len_data):
            yield data[first_index: second_index + 1]

if __name__ == "__main__":


    with open("inputs/day9.txt") as f:
        data = list(map(int,f.read().splitlines()))
    n_preamble = 25
    invalid_n = -1
    for idx,n in enumerate(data[n_preamble:]):
        pairs = [(a, b, a*b) for a, b in list(filter(lambda l: sum(l)
                                                    == n, list(combinations(data[idx:n_preamble+idx], 2))))]
        if not(pairs):
            invalid_n = n
            break
    print(invalid_n)

    sets = gen_contiguous_sets(data)
    for _set in sets:
        if sum(_set) == invalid_n:
            solution_contiguous_sets = sorted(_set)
            print(solution_contiguous_sets[0]+solution_contiguous_sets[-1])
            break
    