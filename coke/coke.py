def main():
    amount_due = 50
    while amount_due > 0:
        print("Amount Due: ", amount_due)
        coin_inserted = int(input("Insert Coin: "))
        if coin_inserted == 25 or coin_inserted == 10 or coin_inserted == 5:
            amount_due -= coin_inserted
    print("Change Owed: ", abs(amount_due))


if __name__ == "__main__":
    main()