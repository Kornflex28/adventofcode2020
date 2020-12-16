if __name__ == "__main__":
    with open("./inputs/day3.txt") as f :
        data= f.read().splitlines()
    n=len(data[0])
    rights = [1,3,5,7,1]
    downs = [1,1,1,1,2]
    # print(n,data[:3])
    pos=0
    tree = "#"
    n_tree = 0

    for line in data[::downs[1]]:
        if line[pos]==tree:
            n_tree+=1
        pos=(pos+rights[1])%n
    print(n_tree)

    n_trees=1
    for right,down in zip(rights,downs):
        n_tree = 0
        pos=0
        for line in data[::down]:
            if line[pos]==tree:
                n_tree+=1
            pos=(pos+right)%n
        n_trees*=n_tree
    print(n_trees)
