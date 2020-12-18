ACT = "#"
INACT = "."
import tqdm


def add_shell(space):
    X, Y, Z = zip(*space.keys())
    x1, x2 = min(X), max(X)
    y1, y2 = min(Y), max(Y)
    z1, z2 = min(Z), max(Z)
    for j in range(x1 - 1, x2 + 2):
        for i in range(y1 - 1, y2 + 2):
            for k in range(z1 - 1, z2 + 2):
                coord = (j, i, k)
                if coord not in space:
                    space[coord] = INACT


def get_neighbors(x, y, z):
    return [
        (j, i, k)
        for j in range(x-1, x+2)
        for i in range(y-1, y+2)
        for k in range(z-1, z+2)
        if j != x or i != y or k != z
    ]


def next_state(space):
    new_space = dict()
    add_shell(space)
    for (coord), value in space.items():
        active_neighbors = 0
        for n_coords in get_neighbors(*coord):
            if space.get(n_coords, INACT) == ACT:
                active_neighbors += 1
        if (value == ACT and 2 <= active_neighbors <= 3
                or value == INACT and active_neighbors == 3):
            new_value = ACT
        else:
            new_value = INACT
        new_space[coord] = new_value
    return new_space


def add_shell_4d(space):
    X, Y, Z, W = zip(*space.keys())
    x1, x2 = min(X), max(X)
    y1, y2 = min(Y), max(Y)
    z1, z2 = min(Z), max(Z)
    w1, w2 = min(W), max(W)
    for j in range(x1 - 1, x2 + 2):
        for i in range(y1 - 1, y2 + 2):
            for k in range(z1 - 1, z2 + 2):
                for l in range(w1 - 1, w2 + 2):
                    coord = (j, i, k, l)
                    if coord not in space:
                        space[coord] = "."


def get_neighbors_4d(x, y, z, w):
    return [
        (j, i, k, l)
        for j in range(x-1, x+2)
        for i in range(y-1, y+2)
        for k in range(z-1, z+2)
        for l in range(w-1, w+2)
        if j != x or i != y or k != z or l != w
    ]


def next_state_4d(space):
    new_space = dict()
    add_shell_4d(space)
    for coord, value in space.items():
        active_neighbors = 0
        for n_coords in get_neighbors_4d(*coord):
            if space.get(n_coords, ".") == "#":
                active_neighbors += 1
        if (value == "#" and 2 <= active_neighbors <= 3
            or value == "." and active_neighbors == 3):
            new_value = "#"
        else:
            new_value = "."
        new_space[coord] = new_value
    return new_space

if __name__ == "__main__":
    with open("inputs/day17.txt") as f:
        grid = list(map(list, f.read().splitlines()))

    shift = (1 - len(grid)) // 2
    space = {
        (j + shift, i + shift, 0): grid[i][j]
        for i in range(len(grid))
        for j in range(len(grid[i]))
    }
    
    space_4d = {
    (j + shift, i + shift, 0, 0) : grid[i][j]
        for i in range(len(grid))
        for j in range(len(grid[i]))
    }

    for _ in tqdm.trange(6):
        space = next_state(space)
        space_4d = next_state_4d(space_4d)

    print(list(space.values()).count(ACT))
    print(list(space_4d.values()).count(ACT))
