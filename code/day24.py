
def get_neighbors(tile):
    return [tile + 1 - 1j, tile - 1 - 1j, tile + 1 + 1j, tile - 1 + 1j, tile + 2, tile - 2, ]

def tick(tiles):
    next_tiles = set()
    for tile in tiles:
        num_neighbors = 0
        for neighbor in get_neighbors(tile):
            if neighbor in tiles:
                num_neighbors += 1
            else:
                grand_num_neighbors = 0
                for grand_neighbor in get_neighbors(neighbor):
                    if grand_neighbor in tiles:
                        grand_num_neighbors += 1
                if grand_num_neighbors == 2:
                    next_tiles.add(neighbor)
        if 0 < num_neighbors <= 2:
            next_tiles.add(tile)
    return next_tiles


if __name__ == "__main__":
    with open("inputs/day24.txt") as f:
        tiles = set()
        for line in f.read().splitlines():
            new_line = (
                line.replace(r"se", "(1 - 1j) + ").replace(r"sw", "(-1 - 1j) + ").replace(r"ne", "(1 + 1j) + ").replace(r"nw", "(-1 + 1j) + ").replace(r"e", "2 + ").replace(r"w", "-2 + "))
            tile = eval(new_line + "0")
            if tile in tiles:
                tiles.remove(tile)
            else:
                tiles.add(tile)
    print(len(tiles))
    for _ in range(100):
        tiles = tick(tiles)
    print(len(tiles))
