with open("read.txt","r") as f:
    input = list(map(int, f.read().split("\n")))

##part1
# print(sum([num//3 - 2 for num in input]))

##part2
def get_fuel(num):
    fuel = num//3-2
    add = fuel//3-2
    while add>0:
        fuel += add
        add = add//3 -2
    return fuel

print(sum([get_fuel(num) for num in input]))
