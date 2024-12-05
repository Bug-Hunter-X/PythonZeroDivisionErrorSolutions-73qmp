def calculate_average_safe(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers) if len(numbers)>0 else 0

# Example usage demonstrating the fix
my_list = []
average = calculate_average_safe(my_list) 
print(f"Average: {average}")

my_list = [10, 20, 30, 0, 0, 0]
average = calculate_average_safe(my_list) 
print(f"Average: {average}")

my_list = [10, 20, 30, 40, 50]
average = calculate_average_safe(my_list) 
print(f"Average: {average}") 