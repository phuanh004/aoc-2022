def main():
    file = open('input.txt', 'r')
    overlaps = 0

    while True:
        line = file.readline()
        if not line:
            break

        # Pair of Elves
        elf1, elf2 = line.split(',')

        # Elf 1
        e1_start, e1_end = elf1.split('-')
        e1_start = int(e1_start)
        e1_end = int(e1_end)
        print('Elf 1: %s - %s' % (e1_start, e1_end))

        # Elf 2
        e2_start, e2_end = elf2.split('-')
        e2_start = int(e2_start)
        e2_end = int(e2_end)
        print('Elf 2: %s - %s' % (e2_start, e2_end))

        # Check if one in range of another
        if e1_end >= e2_start and e1_end <= e2_end:
            overlaps += 1
        elif e1_start >= e2_start and e1_start <= e2_end:
            overlaps += 1
        elif e2_end >= e1_start and e2_end <= e1_end:
            overlaps += 1
        elif e2_start >= e1_start and e2_start <= e1_end:
            overlaps += 1

        print('-----------------------')

    # Close file
    file.close()
    # Print result
    print('Total range-overlaps: %s' % overlaps)


if __name__ == '__main__':
    main()
