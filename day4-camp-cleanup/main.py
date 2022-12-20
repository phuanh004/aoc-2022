def main():
    file = open('input.txt', 'r')
    total_fully_contains = 0

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

        # Check if fully contains
        if e1_start - e2_start >= 0 and e1_end - e2_end >= 0:
            total_fully_contains += 1
            print('Fully contains')
        elif e2_start - e1_start <= 0 and e2_end - e1_end >= 0:
            total_fully_contains += 1
            print('Fully contains')

        print('-----------------------')

    # Close file
    file.close()
    # Print result
    print('Total fully contains: %s' % total_fully_contains)


if __name__ == '__main__':
    main()
