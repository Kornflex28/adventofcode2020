def parse(command):
    parsed = command.split()
    return parsed[0], int(parsed[1])


def execute(instrs):
        hasLoop = False
        visited = set()
        next_command_id = acc = 0
        while next_command_id < len(instrs):
            com, value = instrs[next_command_id]
            if next_command_id in visited:
                hasLoop = True
                break
            visited.add(next_command_id)
            if com == 'jmp':
                next_command_id = next_command_id + value
                continue
            elif com == "nop":
                next_command_id += 1
                continue
            elif com == 'acc':
                acc += value
                next_command_id += 1
        return (acc, hasLoop)


if __name__ == "__main__":

    with open('inputs/day8.txt') as fp:
        data = fp.read().splitlines()

    instructions = [parsed for parsed in list(map(parse, data))]

    print(execute(instructions))

    command_swap = {'nop': 'jmp', 'jmp': 'nop'}
    for i, (com, value) in enumerate(instructions):
        if com == 'nop' or com == 'jmp':
            newInstructions = instructions[:i] + \
                [(command_swap[com], value)] + instructions[i+1:]
            accValue, hasLoop = execute(newInstructions)
            if not hasLoop:
                print((accValue, hasLoop))
