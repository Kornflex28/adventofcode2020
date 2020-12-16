if __name__ == "__main__":
    with open("./inputs/day2.txt") as f :
        data=[]
        for line in f.readlines():
            temp = line.split()
            data.append((sorted(list(map(int,temp[0].split("-")))),temp[1][0],temp[2]))
        print(data[:3])
        n_valid_1=0
        n_valid_2=0
        for counts,letter,pwd in data:
            if counts[0] <= pwd.count(letter) <= counts[1]:
                n_valid_1+=1
            if (pwd[counts[0]-1]==letter) != (pwd[counts[1]-1]==letter):
                n_valid_2+=1
        print(n_valid_1)
        print(n_valid_2)
