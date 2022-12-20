import string


def main():
    # Open file
    file = open("input.txt", "r")

    # Declare variables
    sum_priorities = 0

    while True:
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        if not line3:
            break

        # Break string into group of 3
        rucksack1 = line1.rstrip('\n')
        rucksack2 = line2.rstrip('\n')
        rucksack3 = line3.rstrip('\n')

        # Find intersection
        _temp = set(rucksack1).intersection(rucksack2)
        _temp = set(_temp).intersection(rucksack3)
        intersect = list(_temp)

        # Find priority
        priority = string.ascii_letters.index(intersect[0]) + 1
        sum_priorities += priority

        # Print
        print('Priority of %s is %d' % (intersect[0], priority))

    # Close file
    file.close()
    # Print sum of priorities
    print('Total: %d' % sum_priorities)


if __name__ == "__main__":
    main()
