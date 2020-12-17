if __name__ == "__main__":
    with open("inputs/day13.txt") as f:
        ts = int(f.readline())
        buses = f.readline().split(",")
    bus_ids = list(map(int, filter(lambda s: s != "x", buses)))
    bus_waiting = list(map(lambda n: n-ts % n, bus_ids))
    bus_wait = min(bus_waiting)
    bus_id = bus_ids[bus_waiting.index(bus_wait)]
    print(bus_id*bus_wait)

    bus_offsets = [(int(j), i) for i, j in enumerate(buses) if j != "x"]
    t, step = 0, 1
    for bus_i, offset in bus_offsets:
        while (t + offset) % bus_i != 0:
            t += step
        step *= bus_i
    print(t)
