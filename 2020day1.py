sample_input = [1721,979,366,299,675,1456]

## part 1
def product(input):
    for each in input:
        diff = 2020-each
        if diff in input:
            return diff*each
        
## part 2
def find_three_numbers(nums, target):
    nums.sort()
    
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return nums[i]*nums[left]*nums[right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

with open("read.txt","r") as f:
    input = list(map(int, f.read().split("\n")))

print(product(input))
print(find_three_numbers(nums=input,target=2020))