def checkHex(s):
    s_copy = s.lower()
    if s_copy[0] != "#":
        return False
    for ch in s_copy[1:]:
        if ((ch < '0' or ch > '9') and
                (ch < 'a' or ch > 'f')):
            return False
    return True


def valid_fields(passport):
    return ((1920 <= int(passport['byr']) <= 2002) and
            (2010 <= int(passport['iyr']) <= 2020) and
            (2020 <= int(passport['eyr']) <= 2030) and
            ((passport['hgt'][-2:] == "cm" and 150 <= int(passport['hgt'][:-2]) <= 193) or (passport['hgt'][-2:] == "in" and 59 <= int(passport['hgt'][:-2]) <= 76)) and
            (checkHex(passport['hcl'])) and
            (passport['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) and
            (len(passport['pid']) == 9 and passport['pid'].isnumeric())
            )


if __name__ == "__main__":
    with open("./inputs/day4.txt") as f:
        data = []
        passport = {}
        for line in f.read().splitlines():
            if line:
                for key, value in list(map(lambda l: l.split(':'), line.split())):
                    passport[key] = value
            else:
                data.append(passport)
                passport = {}
        data.append(passport)
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    n_valid_1 = 0
    n_valid_2 = 0
    for passport in data:
        missing_fields = set(required_fields)-set(passport.keys())
        if missing_fields == set() or missing_fields == set(['cid']):
            n_valid_1 += 1
            if valid_fields(passport):
                n_valid_2 += 1

    print(n_valid_1)
    print(n_valid_2)
