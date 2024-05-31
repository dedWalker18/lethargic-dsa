def part1(frequencies):
    return sum(frequencies)

def part2(frequencies):
    seen = set()
    current_frequency = 0
    while True:
        for freq in frequencies:
            current_frequency += freq
            if current_frequency in seen:
                return current_frequency
            seen.add(current_frequency)

if __name__ == "__main__":
    with open("read.txt", "r") as f:
        frequencies = [int(line.strip()) for line in f.readlines()]

    print("Part 1:", part1(frequencies))
    print("Part 2:", part2(frequencies))
