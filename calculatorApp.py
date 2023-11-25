print("\n\tCalculator App")

option = input("\n\tChoose an option:\n\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division\n\t5. Exit\n\t")

while option != "5":
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
        print("\n\tQuotient of",num1,"and",num2,"is",num1/num2)
    else:
        print("\n\tInvalid option. Please try again.")

    option = input("\n\tChoose an option:\n\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division\n\t5. Exit\n\t")
    
print("\n\tThank you for using the calculator app. Goodbye!")

