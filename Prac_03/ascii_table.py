def main():
    START_NUMBER = 33
    END_NUMBER = 127
    finished = False
    character = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(character, ord(character)))

    number = get_number(START_NUMBER, END_NUMBER)

    print("The character for {} is {}".format(number, chr(number)))

def get_number(START_NUMBER, END_NUMBER):
    finished = False
    while not finished:
        try:
            number = int(input("Enter a number between {} and {}: ".format(START_NUMBER, END_NUMBER)))
            if number >= START_NUMBER and number <= END_NUMBER:
                finished = True
        except ValueError:
            print("Please enter a valid number!")

    return number

main()