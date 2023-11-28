def calculate_mode(numbers):
    max_count = 0
    mode = numbers[0]

    for num in numbers:
        num_count = numbers.count(num)
        if num_count > max_count:
            max_count = num_count
            mode = num

    return mode

numbers = [1, 2, 3, 2, 4, 3, 2, 3, 4, 2, 5]
print("Mode:", calculate_mode(numbers))