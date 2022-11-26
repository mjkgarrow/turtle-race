import random
from math import sqrt

# Turtle race to reach your destination using 2-d approach

# race track is of 400 x 400 space

# any random place will be selected to ensure winning trophy for a turtle

# turtle can move in x y plane using up, down, left and right keywords
# u, d, 1,
# once turtle reaches destination it will be announced winner

# Turtle will be given hint of its current location when the arrow is pressed

SPACE = [10, 10]
TROPHY = (random.randint(0, SPACE[0]), random.randint(0, SPACE[1]))
TURTLE = [0, 0]


def move_loc(x, y, original):
    # Check if new position is within space
    if (0 <= x <= SPACE[0]) and (0 <= y <= SPACE[1]):
        # This section is the hint - it compares the distance between the turtle and trophy for the old position and new position (using pythagoras)
        d1 = sqrt(((TROPHY[0] - original[0])**2) +
                  ((TROPHY[1] - original[1])**2))
        d2 = sqrt(((TROPHY[0] - x)**2) +
                  ((TROPHY[1] - y)**2))
        if d1 < d2:
            print('Hint: Colder')
        else:
            print('Hint: Warmer')

        # If new position is within space, return the new position
        return [x, y]
    else:
        # If not then print a prompt and return the old position
        print("You've hit a wall")
        return TURTLE


while True:
    # Get user input
    move = input("Which way to move the turtle (u, d, l, r) q to quit: ")

    # Match turtle movement to the input
    match move:
        case 'u':
            TURTLE = move_loc(TURTLE[0], TURTLE[1] + 1, TURTLE)
        case 'd':
            TURTLE = move_loc(TURTLE[0], TURTLE[1] - 1, TURTLE)
        case 'l':
            TURTLE = move_loc(TURTLE[0] - 1, TURTLE[1], TURTLE)
        case 'r':
            TURTLE = move_loc(TURTLE[0] + 1, TURTLE[1], TURTLE)
        case 'q':
            break
        case _:
            continue

    # If the turtle has found the trophy, break the loop
    if TURTLE == list(TROPHY):
        print("You've won")
        break
