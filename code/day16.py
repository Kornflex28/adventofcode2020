
def get_conditions(s):
    ranges = s.split(" or ")
    limits = tuple(list(map(int, ranges[0].split(
        "-")))), tuple(list(map(int, ranges[1].split("-"))))
    return limits


def parse_field_line(line):
    args = line.split(": ")
    return args[0], get_conditions(args[1])


def check_if_valid(n, limits):
    # print(f"{(limits[0][0]<=n<=limits[0][1]) or (limits[1][0]<=n<=limits[1][1])} : ({limits[0][0]}<={n}<={limits[0][1]}) or ({limits[1][0]}<={n}<={limits[1][1]})")
    return (limits[0][0] <= n <= limits[0][1]) or (limits[1][0] <= n <= limits[1][1])


def check_if_all_field(n, conditions):
    return {field: check_if_valid(n, limits) for (field, limits) in conditions.items()}


def check_ticket(ticket, conditions):
    tickets_n_valids = []
    for n in ticket:
        valids = check_if_all_field(n, conditions)
        tickets_n_valids.append(valids)
        if not(any(valids.values())):
            return False, n, tickets_n_valids
    return True, -1, tickets_n_valids

    # return is_valid,out


if __name__ == "__main__":

    with open("inputs/day16.txt") as f:
        data = f.read().splitlines()

    is_user_ticket = False
    is_nearby_ticket = False
    nearby_tickets = []
    conditions = {}

    for line in data:
        if not(line):
            pass
        elif line == "your ticket:":
            is_user_ticket = True
        elif line == "nearby tickets:":
            is_nearby_ticket = True
        elif is_user_ticket:
            user_ticket = list(map(int, line.split(",")))
            is_user_ticket = False
        elif is_nearby_ticket:
            nearby_tickets.append(list(map(int, line.split(","))))
        else:
            field, limits = parse_field_line(line)
            conditions[field] = limits

    # print(user_ticket)
    # print(conditions)
    # print(nearby_tickets)

    invalid_tickets_n = []
    valid_tickets = []
    for ticket in nearby_tickets:
        is_valid, n, _ = check_ticket(ticket, conditions)
        if not(is_valid):
            invalid_tickets_n.append(n)
        else:
            valid_tickets.append(ticket)

    print(sum(invalid_tickets_n))
    # print(valid_tickets)

    fields_valids = {}
    for ticket in valid_tickets:
        # print(ticket)
        _, _, tickets_n_valids = check_ticket(ticket, conditions)
        # print(tickets_n_valids,"")
        for field in conditions:
            if field in fields_valids:
                fields_valids[field].append(
                    [el[field] for el in tickets_n_valids])
            else:
                fields_valids[field] = [[el[field] for el in tickets_n_valids]]

    possible_field_pos = {}
    definite_field_pos = {}

    for field, tickets_valids in fields_valids.items():
        for i in range(len(user_ticket)):
            if all([ticket[i] for ticket in tickets_valids]):
                if field in possible_field_pos:
                    possible_field_pos[field].append(i)
                else:
                    possible_field_pos[field] = [i]
                # user_ticket_data[field] = user_ticket[i]
    looping = True
    while looping:
        for field, field_pos in possible_field_pos.items():
            if len(field_pos) == 1:
                definite_field_pos[field] = field_pos
                for field_2, field_pos_2 in possible_field_pos.items():
                    if field != field_2:
                        if field_pos[0] in field_pos_2:
                            field_pos_2.remove(field_pos[0])
                            definite_field_pos[field_2] = field_pos_2
        looping = (len(user_ticket) != sum(
            [len(pos) for pos in definite_field_pos.values()]))

    user_ticket_data = {
        field: user_ticket[definite_field_pos[field][0]] for field in definite_field_pos}

    m = 1
    for field, n in user_ticket_data.items():
        if field.startswith("departure"):
            m *= n
    print(m)
