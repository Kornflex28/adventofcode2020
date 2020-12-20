import math


def get_borders(tile):
    return (tile[0], [l[-1] for l in tile], tile[-1], [l[0] for l in tile])


def get_flips(tile):
    return [tile, tile[::-1], [l[::-1] for l in tile], [l[::-1] for l in tile][::-1]]


def get_rotations(tile):
    rots = [tile]
    last = tile
    for _ in range(3):
        tile = [l[:] for l in tile]
        for x in range(len(tile)):
            for y in range(len(tile[x])):
                tile[x][y] = last[len(tile[x])-y-1][x]
        last = tile
        rots.append(tile)
    return rots


def get_transforms(tile):
    possible = []
    for flip in get_flips(tile):
        possible.extend(get_rotations(flip))
    output = []
    for pos in possible:
        if pos not in output:
            output.append(pos)
    return output


def rec_tile(tiled, tile_opts, dimension, x=0, y=0, seen=set()):
    if y == dimension:
        return tiled
    next_x = x + 1
    next_y = y
    if next_x == dimension:
        next_x = 0
        next_y += 1
    for id, tiles in tile_opts.items():
        if id in seen:
            continue
        seen.add(id)
        for trans_id, border in tiles.items():
            top, _, _, left = border

            if x > 0:
                neighbor_id, neighbor_trans = tiled[x-1][y]
                _, neighbor_right, _, _ = tile_opts[neighbor_id][neighbor_trans]
                if neighbor_right != left:
                    continue
            if y > 0:
                neighbor_id, neighbor_trans = tiled[x][y-1]
                _, _, neighbor_bottom, _ = tile_opts[neighbor_id][neighbor_trans]
                if neighbor_bottom != top:
                    continue
            tiled[x][y] = (id, trans_id)
            ans = rec_tile(tiled, tile_opts, dimension,
                          x=next_x, y=next_y, seen=seen)
            if ans is not None:
                return ans
        seen.remove(id)
    tiled[x][y] = None
    return None


def get_tiled(tiles):
    tile_opts = {id: get_transforms(tile) for id, tile in tiles.items()}
    tile_border_opts = {}
    for id, tiles in tile_opts.items():
        for idx, tile in enumerate(tiles):
            if id not in tile_border_opts.keys():
                tile_border_opts[id] = {}
            tile_border_opts[id][idx] = get_borders(tile)
    dimension = int(math.sqrt(len(tile_opts)))
    tiled = [[None] * dimension for _ in range(dimension)]
    return tile_opts, rec_tile(tiled, tile_border_opts, dimension)


def remove_guides(tile_opts, tiled):
    out = []
    for row in tiled:
        tiles = []
        for num, trans_id in row:
            tile = tile_opts[num][trans_id]
            tiles.append([l[1:-1] for l in tile[1:-1]])
        for y in range(len(tiles[0][0])):
            new_row = []
            for id in range(len(tiles)):
                new_row.extend(tiles[id][x][y] for x in range(len(tiles[id])))
            out.append(new_row)
    return out


MONSTER = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''


def parse_monster():
    monster_locs = []
    max_x, max_y = 0, 0
    for y2, line in enumerate(MONSTER.splitlines()):
        for x2, char in enumerate(line):
            if char == "#":
                monster_locs.append((x2, y2))
                max_x = max(x2, max_x)
                max_y = max(y2, max_y)
    return monster_locs, max_x, max_y


def check_monsters(grid):
    monster_locs, max_x, max_y = parse_monster()

    monster_spots = set()
    for y in range(len(grid)):
        if y + max_y >= len(grid):
            break
        for x in range(len(grid[y])):
            if x + max_x >= len(grid[y]):
                break
            is_monster = True
            for x_off, y_off in monster_locs:
                if grid[y+y_off][x+x_off] != "#":
                    is_monster = False
                    break
            if is_monster:
                for dx, dy in monster_locs:
                    monster_spots.add((x+dx, y+dy))
    if len(monster_spots) == 0:
        return None
    all_filled = set()
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '#':
                all_filled.add((x, y))
    return len(all_filled - monster_spots)


def part2(tile_opts, tiled):
    grid = remove_guides(tile_opts, tiled)

    grid_opts = get_transforms(grid)

    for opt in grid_opts:
        ans = check_monsters(opt)
        if ans is not None:
            return ans



if __name__ == "__main__":

    tiles = {}
    with open("inputs/day20.txt") as f:
        for rawTile in f.read().split("\n\n"):
            name, *lines = rawTile.splitlines()
            num = int(name[5:-1])
            lines = [list(l) for l in lines]
            tiles[num] = lines

    tile_opts, tiled = get_tiled(tiles)
    print(tiled[0][0][0] * tiled[0][-1][0] * tiled[-1][0][0] * tiled[-1][-1][0])

    grid = remove_guides(tile_opts, tiled)

    grid_opts = get_transforms(grid)
    for opt in grid_opts:
        water_roughness = check_monsters(opt)
        if water_roughness is not None:
            break
    print(water_roughness)
