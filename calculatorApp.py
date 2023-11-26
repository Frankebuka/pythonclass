import os  # Import the os module

while True:  # Start an outer loop for starting another app
    print("\n\tCalculator App")

    while True:  # Start an inner loop for the calculator operations
        option = input("\n\tChoose an option:\n\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division\n\t5. Exit\n\t")

        if option == "1":
            num1 = int(input("\n\tEnter first number: "))
            num2 = int(input("\tEnter second number: "))
            print("\n\tSum of",num1,"and",num2,"is",num1+num2)
        elif option == "2":
            num1 = int(input("\n\tEnter first number: "))
            num2 = int(input("\tEnter second number: "))
            print("\n\tDifference of",num1,"and",num2,"is",num1-num2)
        elif option == "3":
            num1 = int(input("\n\tEnter first number: "))
            num2 = int(input("\tEnter second number: "))
            print("\n\tProduct of",num1,"and",num2,"is",num1*num2)
        elif option == "4":
            num1 = int(input("\n\tEnter first number: "))
            num2 = int(input("\tEnter second number: "))
            result = num1 / num2  # Perform the division
            if result.is_integer():  # If the result is a whole number
                result = int(result)  # Convert it to an integer
            print("\n\tQuotient of",num1,"and",num2,"is",result)
        elif option == "5":
            print("\n\tThank you for using the calculator app. Goodbye!")
            exit()  # End the program
        else:
            print("\n\tInvalid option. Please try again.")

        while True:  # Start a loop to ask the user if they want to perform another calculation
            perform_another_calculation = input("\n\tDo you want to perform another calculation? (yes/no): ").lower()  # Ask the user if they want to perform another calculation and convert their answer to lowercase
            if perform_another_calculation == "yes":  # If the user wants to perform another calculation
                break  # End the loop and continue with the next calculation
            elif perform_another_calculation == "no":  # If the user doesn't want to perform another calculation
                print("\n\tThank you for using the calculator app. Goodbye!")
                exit()  # End the program
            else:  # If the user entered anything other than "yes" or "no"
                print("\n\tInvalid option. Please try again.")  # Print an error message

        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console