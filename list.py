numbers = []

for _ in range(4):
    num = int(input("Enter a number: "))  
    numbers.insert(0, num)  

average = sum(numbers) / len(numbers)

print("Sorted list:", numbers)
print("Average:", average)