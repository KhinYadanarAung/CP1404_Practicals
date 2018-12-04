def main():
    DISCOUNT = 0.9
    total = 0.0
    num = int(input("Enter number of items"))
    while (num <= 0):
        print("Enter a positive number")
        num = int(input("Enter number of items"))
    for i in range(0, num):
        price = float((input("Enter price of item")))
        total += price
    print("Total = ", total)

    if (total >= 100):
        total = DISCOUNT * total
        print("Total price for ", num, " items is $",total)
    else:
        print("Total price for ", num, " items is $",total)

main()