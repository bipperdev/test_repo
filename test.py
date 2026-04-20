balance = 100 # start with 100 manat as bonus from israel
while True:
    print("1. Top up balance")
    print("2. Deposit money")
    print("3. Show balance")
    print("4. Logout")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        topup = int(input("Enter your balance: "))
        balance = balance + topup
        print("Your new balance is: ", balance)
    elif choice == 2:
        deposit = int(input("Enter your balance: "))
        balance = balance - deposit
        print("Your new balance is: ", balance)
    elif choice == 3:
        print("Your balance is: ", balance)
    elif choice == 4:
       print("Goodbye, Gay!")
       break
