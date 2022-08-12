

import sys

def main():
    # Get the list of integers as input from the user.
    list = [int(x) for x in input().split()]

    # Print the list of integers separated by space.
    print(' '.join([str(x) for x in list]))

    return 0


if __name__ == '__main__':
    sys.exit(main())
