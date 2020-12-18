
import re

def apply_mask(mask,value):
    occ_0 = [s.start() for s in re.finditer("0", mask)]
    occ_1 = [s.start() for s in re.finditer("1", mask)]
    for occ in occ_0:
        value=value[:occ]+"0"+value[occ+1:]
    for occ in occ_1:
        value=value[:occ]+"1"+value[occ+1:]
    return value

def apply_mask_2(mask,value):
    occ_X = [s.start() for s in re.finditer("X", mask)]
    occ_1 = [s.start() for s in re.finditer("1", mask)]
    for occ in occ_X:
        value=value[:occ]+"X"+value[occ+1:]
    for occ in occ_1:
        value=value[:occ]+"1"+value[occ+1:]
    return value

def exec_line_1(line,mask,mem):
    if "mask" in line:
        mask = line.split("mask = ")[-1]
    if "mem" in line:
        mem[re.search(r"\d+",line).group(0)]=int(apply_mask(mask,format(int(line.split("= ")[-1]),"036b")),2)
    return mask,mem

def exec_line_2(line,mask,mem):
    if "mask" in line:
        mask = line.split("mask = ")[-1]
    if "mem" in line:
        init_address = format(int(re.search(r"\d+",line).group(0)),"036b")
        masked_address = apply_mask_2(mask,init_address)
        possible_addresses = get_addresses_rec(masked_address)
        value = int(line.split("= ")[-1])
        for address in possible_addresses:
            mem[str(int(address,2))]=value
    return mask,mem

def get_addresses_rec(bits):
    if "X" not in bits:
        return [bits]
    else:
        idx_of_X = bits.index("X")
        bits_0 = bits[:idx_of_X]+"0"+bits[idx_of_X+1:]
        bits_1 = bits[:idx_of_X]+"1"+bits[idx_of_X+1:]
        return get_addresses_rec(bits_0)+get_addresses_rec(bits_1)


if __name__ == "__main__":
    with open("inputs/day14.txt") as f:
        data = f.read().splitlines()
    mask_1=""
    mem_1={}
    mask_2=""
    mem_2={}
    for line in data:
        mask_1,mem_1 = exec_line_1(line,mask_1,mem_1)
        mask_2,mem_2 = exec_line_2(line,mask_2,mem_2)
    print(sum(mem_1.values()))
    print(sum(mem_2.values()))

