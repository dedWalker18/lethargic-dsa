with open("read.txt","r") as f:
    input = list(map(int, f.read().split(",")))

# input = [16,1,2,0,4,2,7,1,2,14]

##part 1
# input = sorted(input)
# median = input[len(input)//2]
# print(sum([abs(each-median) for each in input]))


""" 
Although this doesn't work becaus mean is not the ideal target 
But if it could, this would save time by tunning in O(n)

mean = round(sum(input)/len(input))
print(sum([(abs(each-mean)*(abs(each-mean)+1))//2 for each in input]))

"""

## part 2 This Works
print(min(sum(abs(crab - target) * (abs(crab - target) + 1) // 2 for crab in input) for target in range(min(input), max(input) + 1)))