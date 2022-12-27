import string


def get_crane_position(file):
    cr_list_pos = []
    currline_pos = 0

    while True:
        line = file.readline()
        if not line:
            break

        if line[1].isdigit():
            c = line.rstrip()
            c = list(c)

            for i in range(len(c)):
                if c[i].isdigit():
                    cr_list_pos.append(int(i))
            break

        currline_pos += 1

    # Remove the last just line of numbers
    return cr_list_pos, currline_pos


def get_content_each_crane(file, crane_list_pos, currline_pos, container):
    # Go back to top of file
    file.seek(0)

    # Iterate through the file
    for i in range(currline_pos):
        l = file.readline()

        line_c = get_content_each_line(l, crane_list_pos)
        for j in range(len(line_c)):
            if line_c[j] is not None:
                container[j][(len(crane_list_pos) - 1) - i] = line_c[j]

    # using filter()
    # to remove None values in list
    for index, it in enumerate(container):
        res = list(filter(lambda item: item is not None, it))
        container[index] = res


def get_content_each_line(line, crane_list_pos):
    content_list = []
    # Get the content of each line
    line = line.rstrip()

    for i in range(len(crane_list_pos)):
        if line[crane_list_pos[i]] != ' ':
            content_list.append(line[crane_list_pos[i]])
        else:
            content_list.append(None)

    return content_list


# def get_instructions(file, crane_list_pos, currline_pos):

def follow_instructions(file, currline_pos, container):
    # Skip numberic line and blank line
    # file.seek(currline_pos + 2)

    while True:
        # Skip numberic & blank lines
        line = file.readline()
        if not line:
            break
        else:
            if line == '\n':
                continue
            elif line[1]:
                if line[1].isdigit():
                    continue

        # Sanitize input
        # Get the content between 'move ' and ' from'
        how_many = line[line.find('move ') + 5:line.find(' from')].rstrip()
        how_many = how_many.strip()

        # Get the content between 'from ' and ' to'
        from_stack_pos = line[line.find('from ') + 5:line.find(' to')]
        from_stack_pos = from_stack_pos.strip()
        from_idx = int(from_stack_pos) - 1

        # Get the content between 'to ' and ' '
        to_stack_pos = line[line.find('to ') + 3:line.find('\n')]
        to_stack_pos = to_stack_pos.strip()
        to_idx = int(to_stack_pos) - 1

        for i in range(int(how_many)):
            container[to_idx].append(container[from_idx].pop())
        # container[to_idx].append(container[from_idx][int(how_many):])


def main():
    file = open("input.txt", "r")

    crane_list_pos, currline_pos = get_crane_position(file)
    container = []

    for i in range(currline_pos + 1):
        container.append([])
        container[i] = [None] * len(crane_list_pos)

    # Rebuild container
    get_content_each_crane(file, crane_list_pos,
                           currline_pos, container=container)

    # Follow instructions
    follow_instructions(file, currline_pos, container)

    # print(container)
    for i in range(len(container)):
        print(container[i].pop(), end='')


if __name__ == "__main__":
    main()
