import re

MUL = "*"
ADD = "+"
PAR_L = "("
PAR_R = ")"


def evaluate_op(operator, x, y):
    if operator == MUL:
        return x*y
    if operator == ADD:
        return x+y


def find_first_op(s):
    start = [m.start() for m in re.finditer(f"\{PAR_L}", s)]
    end = [m.start() for m in re.finditer(f"\{PAR_R}", s)]
    if len(start) > 0:
        end = end[0]
        start = max([i for i in start if i < end])
        return start, end
    else:
        return None, None


def evaluate(expr):
        items = expr.split()
        x = int(items.pop(0))
        while len(items) > 0:
            op = items.pop(0)
            y = int(items.pop(0))
            x = evaluate_op(op, x, y)
        return x


def evaluate_line(line):
    start, end = find_first_op(line)
    while start is not None:
        res = str(evaluate(line[start + 1:end]))
        line = line[:start] + res + line[end+1:]
        start, end = find_first_op(line)
    return evaluate(line)


def evaluate_line_2(line):
    items = line.split()
    add_indices = [i for i, j in enumerate(items) if j == '+']
    for i in add_indices:
        items[i-1] = f"{PAR_L}" + items[i-1]
        items[i+1] = items[i+1] + f"{PAR_R}"
    return eval(" ".join(items))


if __name__ == "__main__":
    with open("inputs/day18.txt") as f:
        data = f.read().splitlines()
    print(sum(list(map(evaluate_line, data))))
    print(sum(list(map(evaluate_line_2, data))))
