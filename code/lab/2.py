def process_tuple(numbers):
    # 1. Find the minimum and maximum value in the tuple
    min_value = min(numbers)
    max_value = max(numbers)
    
    # 2. Convert the tuple into a list and add a new element to it
    numbers_list = list(numbers)
    numbers_list.append(25)
    
    # 3. Convert the list back into a tuple and print the final tuple
    modified_tuple = tuple(numbers_list)
    
    # Display results
    print(f"Minimum: {min_value}, Maximum: {max_value}")
    print("Modified Tuple:", modified_tuple)

# Example usage
numbers = (5, 12, 7, 18, 3)
process_tuple(numbers)