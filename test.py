import random

password = '8888'
chances = 3
while chances > 0:
    user_pin = input('Enter 4 digit PIN:')
    if user_pin == password:
        print("Correct!Acsess allowed")
        balance = 100  # start with 100 manat as bonus from israel
        while True:
            print("1. Top up balance")
            print("2. Deposit money")
            print("3. Show balance")
            print("4. Logout")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                topup = int(input("Enter your balance: "))
                monitrr = random.randint(1,50)
                if topup > 0:
                    balance = balance + topup + monitrr
                    print("Your new balance is: ", balance)
            elif choice == 2:
                deposit = int(input("Enter your balance: "))
                if deposit <= balance:
                    balance = balance - deposit + monitrr
                    print("Your new balance is: ", balance)
                else:
                    print("Insufficient funds")
            elif choice == 3:
                print("Your balance is: ", balance)
            elif choice == 4:
                print("Goodbye, Gay!")
                break
            else:
                print("Invalid choice")
        break
    else:
        chances -= 1
        if chances > 0:
            print("Wrong pin! you have:", chances, "Attempts left")
        else:
            print("Sorry you have:", chances, "Attempts left")
            break






