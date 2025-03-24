def basic_list_operations(numbers, count_number):
    # 1. Find the largest and smallest numbers in the list
    largest = max(numbers)
    smallest = min(numbers)
    
    # 2. Count the occurrence of a user-given number in the list
    count = numbers.count(count_number)
    
    # Display results
    print(f"Largest: {largest}, Smallest: {smallest}")
    print(f"Count of {count_number}: {count}")

# Example usage
numbers = [10, 20, 30, 40, 50, 20, 10]
count_number = 20
basic_list_operations(numbers, count_number)