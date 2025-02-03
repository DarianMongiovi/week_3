# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.

# Problem 1: Write a program that takes a list of numbers and prints out the sum of all the numbers in the list.

def list_sum(numbers):
    
    sum = 0
    for i in numbers:
        sum += i

    return sum


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'Sum: {list_sum(numbers)}')


# Problem 2: Write a program that takes a list of numbers and prints out the average of all the numbers in the list.

def list_average(numbers):
    
    sum = 0
    for i in numbers:
        sum += i

    average = sum / len(numbers)

    return average


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'Average: {list_average(numbers)}')


# Problem 3: Write a program that takes a list of numbers and prints out the largest number in the list.

def list_max(numbers):
    
    max = 0
    for i in numbers:
        if i > max:
            max == i
        else:
            pass

    return max


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'Max: {list_max(numbers)}')