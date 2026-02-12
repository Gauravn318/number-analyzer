def get_input():
    n = int(input("Enter the total number of elements: "))
    
    if n <= 0:
        return []
    
    numbers = []
    print("Enter the numbers:")
    for _ in range(n):
        numbers.append(int(input()))
    
    return numbers

def count_numbers(numbers):
    return len(numbers)

def total_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def max_finder(numbers):
    return max(numbers)

def min_finder(numbers):
    return min(numbers)

def average_finder(numbers):
    return total_sum(numbers) / len(numbers)

def odd_even_counter(numbers):
    odd = 0
    even = 0
    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even

def second_largest_finder(numbers):
    if len(numbers) < 2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num != largest and num > second_largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        return None
    
    return second_largest

def sort_checker(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False
    return True

def show(numbers):
    print("\n------ Analysis Result ------")
    print("Total numbers:", count_numbers(numbers))
    print("Sum:", total_sum(numbers))
    print("Largest:", max_finder(numbers))
    print("Smallest:", min_finder(numbers))
    print("Average:", average_finder(numbers))
    
    odd, even = odd_even_counter(numbers)
    print("Odd count:", odd)
    print("Even count:", even)
    
    second = second_largest_finder(numbers)
    if second is None:
        print("Second Largest: Not available")
    else:
        print("Second Largest:", second)
    
    if sort_checker(numbers):
        print("Array is Sorted")
    else:
        print("Array is Not Sorted")


numbers = get_input()
if numbers:
    show(numbers)
else:
    print("No numbers entered.")
