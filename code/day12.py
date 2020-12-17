def rotate_ship(init_dir,dir,angle):
    dirs="NESW"
    idx = angle//90 if dir=="R" else -angle//90
    return dirs[(dirs.index(init_dir)+idx)%4]

def rotate_wp(init_dirs,dir,angle):
    temp = init_dirs.copy()
    dirs="NESW"
    idx = angle//90 if dir=="R" else -angle//90
    for init_dir in temp:
        init_dirs[dirs[(dirs.index(init_dir)+idx)%4]]=temp[init_dir]
    return init_dirs

if __name__ == "__main__":
    with open("inputs/day12.txt") as f :
        instructions = list(map(lambda s:(s[0],int(s[1:])),f.read().splitlines()))

    ship_moves1 = {"N":0,"E":0,"S":0,"W":0}
    ship_moves2 = {"N":0,"E":0,"S":0,"W":0}
    waypoint_moves = {"N":1,"E":10,"S":0,"W":0}
    ship_dir = "E"
    for inst, n in instructions:
        if inst == "F":
            ship_moves1[ship_dir]+=n
            for dir_ in waypoint_moves:
                ship_moves2[dir_]+=n*waypoint_moves[dir_]
        elif inst in ["R","L"]:
            ship_dir = rotate_ship(ship_dir,inst,n)
            waypoint_moves = rotate_wp(waypoint_moves,inst,n)

        else :
            ship_moves1[inst]+=n
            waypoint_moves[inst]+=n

    print(abs(ship_moves1["E"]-ship_moves1["W"])+abs(ship_moves1["N"]-ship_moves1["S"]))
    print(abs(ship_moves2["E"]-ship_moves2["W"])+abs(ship_moves2["N"]-ship_moves2["S"]))



