import string


def main():
    # Open file
    file = open("input.txt", "r")

    # Declare variables
    sum_priorities = 0

    while True:
        line = file.readline()
        if not line:
            break

        # Break string into 2 half
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]

        # Sort each half
        sorted_first_half = [*first_half.rstrip('\n')]
        sorted_first_half.sort()

        sorted_second_half = [*second_half.rstrip('\n')]
        sorted_second_half.sort()

        # Find intersection
        _temp = set(sorted_first_half).intersection(sorted_second_half)
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
