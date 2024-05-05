import requests
import re

response = requests.get(url= 'https://adventofcode.com/2023/day/1/input', headers={"Cookie":"Fill Your Own Cookie"})
input  = response.text
input = input.split("\n")
sum = 0
digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]
digits_dict = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

for word in input:
    d = {}
    l = []
    for i in range(len(word)):
        if word[i].isdigit() and i not in d:
            d[i] = int(word[i])
            l.append(i)
    for digit in digits:
        l2 = list([m.start() for m in re.finditer(digit, word)])
        for each in l2:
            num = digits_dict[digit]
            d[each] = num
            l.append(each)
            
    l = sorted(l)
    if len(l) >= 1:
        min = 10 * d[l[0]]
        max = d[l[-1]]
        sum += min+max

print(sum)