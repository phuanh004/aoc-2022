from enum import Enum


class OpShape(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'


class MyShape(Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'


class ShapeScore(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class RoundScore(Enum):
    WIN = 6
    LOSE = 0
    TIE = 3


def is_win(my_choice: MyShape, op_choice: OpShape):
    if my_choice == MyShape.ROCK and op_choice == OpShape.SCISSORS:
        return True
    elif my_choice == MyShape.PAPER and op_choice == OpShape.ROCK:
        return True
    elif my_choice == MyShape.SCISSORS and op_choice == OpShape.PAPER:
        return True
    else:
        return False


def choose_to_lose(op_choice: OpShape):
    if op_choice == OpShape.ROCK:
        return MyShape.SCISSORS
    elif op_choice == OpShape.PAPER:
        return MyShape.ROCK
    else:
        return MyShape.PAPER


def choose_to_win(op_choice: OpShape):
    if op_choice == OpShape.ROCK:
        return MyShape.PAPER
    elif op_choice == OpShape.PAPER:
        return MyShape.SCISSORS
    else:
        return MyShape.ROCK


def main():
    # Read input file
    file = open('input.txt', 'r')

    # Declare variables
    round = 1
    game_score = 0

    while True:
        line = file.readline()
        if not line:
            break

        # Each Round
        choice = line.split()
        oponent_choice = OpShape(choice[0])
        my_choice = MyShape(choice[1])

        if choice[1] == 'X':    # Means Lose
            my_choice = choose_to_lose(oponent_choice)
        elif choice[1] == 'Y':  # Means Draw
            my_choice = MyShape[oponent_choice.name]
        elif choice[1] == 'Z':  # Means Win
            my_choice = choose_to_win(oponent_choice)

        # If Tie
        game_score += ShapeScore[my_choice.name].value
        if oponent_choice.name == my_choice.name:
            game_score += RoundScore.TIE.value
        else:
            if is_win(my_choice, op_choice=oponent_choice):
                game_score += RoundScore.WIN.value
            else:
                game_score += RoundScore.LOSE.value

    # Print result
    print('Total game score: %d' % game_score)


if __name__ == "__main__":
    main()
