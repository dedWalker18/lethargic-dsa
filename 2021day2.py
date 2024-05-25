with open("read.txt","r") as f:
    input = list(map(str, f.read().split("\n")))

## part 2
x,y,aim = 0,0,0
for each in input:
    direction, step = each.split(" ")
    match direction:
        case "forward": 
            x += int(step)
            y += int(step) * aim
        case "up": aim-=int(step)
        case "down": aim+=int(step)
print(x*y)