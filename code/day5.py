
def seat_from_binary(s):
    col = int(s[-3:].replace("L", "0").replace("R", "1"), 2)
    row = int(s[:-3].replace("F", "0").replace("B", "1"), 2)
    return row, col, row*8+col


if __name__ == "__main__":
    with open("./inputs/day5.txt") as f:
        data = f.read().splitlines()
    seats = []
    seat_ids = []
    for seat in data:
        row, col, seat_id = seat_from_binary(seat)
        seats.append((row, col))
        seat_ids.append(seat_id)
    seat_ids.sort()
    print(seat_ids[-1])
    print(seat_ids[[a-b for a, b in zip(seat_ids, seat_ids[1:])].index(-2)]+1)
