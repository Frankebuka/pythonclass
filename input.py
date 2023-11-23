# calculation
print("\n\n\t Online Calculator")
num1 = int(input("Enter a number from 1-10: "))

if(num1 < 10 and num1 > 1):
    num2 = int(input("Enter another number: "))
elif(num1 == 10 or num1 == 1):
    num2 = int(input("Enter another different number: "))
else: 
    num2 = int(input("Please enter another number: "))
    

    
print(num1, "+", num2, "=", (num1+num2))