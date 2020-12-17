import re
import pprint as pp

def valid_bags_rec(bag,bag_containers,valid_bags=set()):
    if bag not in bag_containers:
        return valid_bags
    else:
        for b in bag_containers[bag]:
            valid_bags=valid_bags.union(set(valid_bags_rec(b,bag_containers,valid_bags)))
        valid_bags=valid_bags.union(set(bag_containers[bag]))
        return valid_bags

def n_bags_rec(bag,bag_rules):
    if not bag_rules[bag]:
        return 0
    else:
        n=0
        for b in bag_rules[bag]:
            n+=bag_rules[bag][b]*(n_bags_rec(b,bag_rules)+1)
        return n


if __name__ == "__main__":

    with open("inputs/day7.txt") as f:
        data = f.read().splitlines()

    bag_of_interest = "shiny gold"
    bag_rules ={}
    bag_containers={}
    for rule in data:
        bag = rule.split("bags")[0][:-1]
        content = {bag:n for bag,n in list(map(lambda l: (" ".join(l[:-1].split(" ")[1:]).replace(" bags","").replace(" bag",""),int(l[:-1].split(" ")[0])),re.findall(r"\d+ \D+[,\.]+",rule)))}
        bag_rules[bag]=content
        for b in content:
            if b in bag_containers:
                bag_containers[b].append(bag)
            else:
                bag_containers[b] = [bag]
    # pp.pprint(bag_rules)
    # pp.pprint(bag_containers)

    valid_bags = valid_bags_rec(bag_of_interest,bag_containers)
    print(len(valid_bags))
    print(n_bags_rec(bag_of_interest,bag_rules))
