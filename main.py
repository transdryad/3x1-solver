import math


def main():
    starting_number = input("What number should the checking start at?\n")
    starting_number = int(starting_number)
    current_number = starting_number
    while True:
        check(current_number)
        current_number = current_number + 1


def check(number):
    i = number
    while i != 1:
        ii = i / 2
        if math.floor(ii) == ii:
            i = i / 2
        else:
            i = i * 3 + 1
    number = str(number)
    print(number + " fits the pattern of 3x+1!")


if __name__ == '__main__':
    main()
