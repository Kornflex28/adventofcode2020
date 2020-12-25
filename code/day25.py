def brute_loop_size(public_key,subject_n=7):
    num=1
    loop_size = 0
    found = False
    while 1:
        num*=subject_n
        num = num%20201227
        loop_size+=1
        if num == public_key :
            print(f"public key {num} found with loop_size of {loop_size}")
            return public_key,loop_size

def encrypt(subject_n,loop_size):
    num=1
    for _ in range(loop_size):
        num*=subject_n
        num = num%20201227
    return num

if __name__ == "__main__":
    with open("inputs/day25.txt") as f:
        door_pub_key = int(f.readline())
        card_pub_key = int(f.readline())
    print(door_pub_key,card_pub_key)

    _,door_loop_size = brute_loop_size(door_pub_key)
    _,card_loop_size = brute_loop_size(card_pub_key)

    print(door_loop_size,card_loop_size)

    door_encryption = encrypt(door_pub_key,card_loop_size)
    card_encryption = encrypt(card_pub_key,door_loop_size)

    print(door_encryption,card_encryption)
