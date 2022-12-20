import bisect


def print_feeding_log(elf_id, total_calories):
    print()
    print('Elf #%d fed total: %d' % (elf_id, total_calories))
    print('---')
    print()


def main():
    # Read input
    file = open('input.txt', 'r')

    # Declare variables
    calories = 0
    elf_id = 1
    elves = []

    while True:
        line = file.readline()

        # EOF
        if not line:
            print_feeding_log(elf_id, calories)
            break
        # Each Elf Seperator
        if line == '\n':
            # Current Elf
            bisect.insort(elves, calories)
            print_feeding_log(elf_id, calories)

            # New Elf
            elf_id += 1
            calories = 0
            continue

        # Adding calories of multi-time of one elf
        cal = int(line)
        calories += cal
        print('Fed reindeer %d calories' % cal)

    # Print result
    print('The most total calories of one Elf carried: ')
    print(elves[-1:])
    print('Top 3 Elves: ')
    print(elves[-3:])
    print('Total Calories of Top 3 Elves: ')
    print(sum(elves[-3:]))


if __name__ == "__main__":
    # Find the Elf carrying the most Calories.
    # How many total Calories is that Elf carrying?
    main()
