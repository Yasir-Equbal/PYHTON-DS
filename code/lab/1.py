def process_numbers(numbers):
    # 1. Remove duplicates
    unique_numbers = list(set(numbers))
    
    # 2. Sort the list in ascending order
    unique_numbers.sort()
    
    # 3. Reverse the sorted list
    reversed_list = unique_numbers[::-1]
    
    # 4. Find the second largest number
    second_largest = unique_numbers[-2] if len(unique_numbers) > 1 else None
    
    # 5. Find the sum of all elements in the list
    total_sum = sum(unique_numbers)
    
    # Display results
    print("Original List:", numbers)
    print("Unique Numbers:", unique_numbers)
    print("Reversed List:", reversed_list)
    print("Second Largest Number:", second_largest)
    print("Sum of Elements:", total_sum)

# Example usage
numbers = [10, 20, 20, 30, 40, 10, 50]
process_numbers(numbers)