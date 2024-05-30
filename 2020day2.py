sample_inpput = ["1-3 a: abcde",
                 "1-3 b: cdefg",
                 "2-9 c: ccccccccc"]



def day2(input):
    count1,count2 = 0,0
    for each in input:
        philosophy, password = map(str.strip, each.split(":"))
        rng, char = philosophy.split(" ")
        min,max = map(int,rng.split("-"))
        occ = password.count(char)
        if occ <= max and occ >= min:
            count1 += 1
        if password[min-1] == char or password[max-1] == char:
            if password[min-1] != password[max-1]:
                count2 += 1
                
    return count1,count2

with open("read.txt", "r") as f:
    input = list(map(str, f.read().split("\n")))

print("Part 1: {}, Part 2: {}".format(day2(input)[0],day2(input)[1]))
