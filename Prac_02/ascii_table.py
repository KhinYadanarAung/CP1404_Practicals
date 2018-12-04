def main():
    START_NUMBER = 33
    END_NUMBER = 127
    finished = False
    character = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(character, ord(character)))

    while not finished:
        number = int(input("Enter a number between {} and {}: ".format(START_NUMBER, END_NUMBER)))
        if number >=START_NUMBER and number <= END_NUMBER:
            finished = True
        else:
            print("Invalid number")

    print("The character for {} is {}".format(number, chr(number)))

    for i in range(START_NUMBER, END_NUMBER+1):
        print("{} {:>4}".format(i, chr(i)))
    

main()