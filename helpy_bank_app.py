import os
import random

# Initialize a dictionary to store user accounts
accounts = {}

while True:
    try:
        print("\n1. Open account\n2. Withdrawal\n3. Deposit\n4. Loan\n5. Exit")
        option = input("Choose an option: ")

        if option == "1":
            firstname = input("Enter your firstname: ")
            lastname = input("Enter your lastname: ")
            age = int(input("Enter your age: "))
            gender = input("Enter your gender: ")
            while gender.lower() not in ["male", "female"]:
                print("Invalid option. Please enter 'male' or 'female'.")
                gender = input("Enter your gender: ")
            phone = input("Enter your phone number: ")

            if age < 15 or not phone.isdigit():
                print("Invalid details. You must be at least 15 years old and phone number must be digits.")
                continue

            account_number = int("9" + str(random.randint(100000000, 999999999)))
            accounts[account_number] = {"balance": 0.00, "loans": 0.00}
            title = "Mr." if gender.lower() == "male" else "Mrs."
            print(f"Account opened for {title} {firstname} {lastname}. Your account number is {account_number}.")

        elif option == "2":
            while True:
                account_number = int(input("Enter your account number: "))
                if account_number in accounts:
                    break
                else:
                    print("Invalid account number.")
                    retry = input("Do you want to try again or exit? (retry/exit): ")
                    if retry.lower() == "exit":
                        exit(0)
            amount = float(input("Enter amount to withdraw: "))

            if account_number not in accounts or amount > accounts[account_number]["balance"]:
                print("Insufficient funds.")
                continue

            accounts[account_number]["balance"] -= amount
            print(f"Withdrew {amount}. New balance is {accounts[account_number]['balance']}.")

        elif option == "3":
            while True:
                account_number = int(input("Enter your account number: "))
                if account_number in accounts:
                    break
                else:
                    print("Invalid account number.")
                    retry = input("Do you want to try again or exit? (retry/exit): ")
                    if retry.lower() == "exit":
                        exit(0)
            amount = float(input("Enter amount to deposit: "))

            accounts[account_number]["balance"] += amount
            print(f"Deposited {amount}. New balance is {accounts[account_number]['balance']}.")

        elif option == "4":
            while True:
                account_number = int(input("Enter your account number: "))
                if account_number in accounts:
                    break
                else:
                    print("Invalid account number.")
                    retry = input("Do you want to try again or exit? (retry/exit): ")
                    if retry.lower() == "exit":
                        exit(0)

            if account_number not in accounts or accounts[account_number]["balance"] < 5000:
                print("Not eligible for a loan.")
                continue

            amount = float(input("Enter amount to borrow: "))
            accounts[account_number]["loans"] += amount
            accounts[account_number]["balance"] += amount
            print(f"Loan of {amount} granted. New balance is {accounts[account_number]['balance']}.")

        elif option == "5":
            print("Thank you for using Helpy Bank app.")
            break

        else:
            print("Invalid option. Please choose a valid option.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        retry = input("Do you want to perform another transaction? (yes/no): ")
        if retry.lower() != "no":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            break