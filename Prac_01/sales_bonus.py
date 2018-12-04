def main():
    sales = float(input("Enter sales: $"))
    while (sales < 0):
        print("Invalid Choice")
        sales = float(input("Enter sales: $"))

    if sales < 1000:
        bonus = 0.1
    else:
        bonus = 0.15

    sale_bonus = sales * bonus
    print("Bonus: $", sale_bonus)

main()