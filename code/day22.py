def recursive_combat(player_1, player_2, played=set()):
    while player_1 and player_2:

        config = (tuple(player_1), tuple(player_2))
        if config in played:
            return False
        played.add(config)

        card_p1, card_p2 = player_1.pop(0), player_2.pop(0)

        if (recursive_combat(player_1[:card_p1], player_2[:card_p2], played=set()) if (len(player_1) >= card_p1 and len(player_2) >= card_p2) else card_p2 > card_p1):
                player_2.extend([card_p2, card_p1])
        else:
                player_1.extend([card_p1, card_p2])

    return not(player_1)


if __name__ == "__main__":
    player_1 = []
    player_2 = []
    is_p1_deck = False
    with open('inputs/day22.txt') as f:
        for line in f.read().splitlines():
            if not(line):
                continue
            if "Player 1" in line:
                is_p1_deck = True
                continue
            elif "Player 2" in line:
                is_p1_deck = False
                continue
            elif is_p1_deck:
                player_1.append(int(line))
            else:
                player_2.append(int(line))
    n = len(player_1)
    r = 0
    _player_1, _player_2 = player_1[:], player_2[:]
    while len(_player_1) > 0 and len(_player_2) > 0:
        card_p1, card_p2 = _player_1.pop(0), _player_2.pop(0)
        if card_p1 > card_p2:
            _player_1.extend([card_p1, card_p2])
        if card_p1 < card_p2:
            _player_2.extend([card_p2, card_p1])
        r += 1

    if not(_player_1):
        print(sum([(2*n-i)*card for i, card in enumerate(_player_2)]))
    else:
        print(sum([(2*n-i)*card for i, card in enumerate(_player_1)]))

    recursive_combat(player_1, player_2)
    print(player_1, player_2)
    if not(player_1):
        print(sum(((len(player_2)-i)*card for i, card in enumerate(player_2))))
    else:
        print(sum(((len(player_1)-i)*card for i, card in enumerate(player_1))))
