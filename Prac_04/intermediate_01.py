def main():
    numbers = []
    total = 0
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
        total += number

    average = total/len(numbers)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[len(numbers)-1]))
    number_orders = sorted(numbers)
    print("The smallest number is {}".format(number_orders[0]))
    print("The largest number is {}".format(number_orders[len(number_orders)-1]))
    print("The average of the numbers is {}".format(average))

main()