
if __name__ == "__main__":
    alpha = "abcdefghijklmnopqrstuvwxyz"
    with open("./inputs/day6.txt") as f:
        data1 = []
        data2 = []
        group1 = set()
        group2=set(alpha)
        for line in f.read().splitlines():
            if line:
                group1=group1.union(set(line))
                group2=group2.intersection(set(line))
            else:
                data1.append(sorted(list(group1)))
                data2.append(sorted(list(group2)))
                group1 = set()
                group2 = set(alpha)
        data1.append(group1)
        data2.append(group2)
    # print(data2[:3])
    n_yeses1 = [len(questions) for questions in data1]
    n_yeses2 = [len(questions) for questions in data2]
    print(sum(n_yeses1))
    print(sum(n_yeses2))
    