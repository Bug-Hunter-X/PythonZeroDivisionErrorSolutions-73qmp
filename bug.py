def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage that can cause ZeroDivisionError
my_list = []
average = calculate_average(my_list) 
print(f"Average: {average}") #This will print 0 as intended

my_list = [10, 20, 30, 0, 0, 0]
average = calculate_average(my_list) 
print(f"Average: {average}") #This will print 0 as intended

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list) 
print(f"Average: {average}") #This will print 30 as intended

# Example that demonstrates how to prevent this error: 

def calculate_average_safe(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers) if len(numbers)>0 else 0

my_list = []
average = calculate_average_safe(my_list) 
print(f"Average: {average}") #This will print 0 as intended

my_list = [10, 20, 30, 0, 0, 0]
average = calculate_average_safe(my_list) 
print(f"Average: {average}") #This will print 0 as intended

my_list = [10, 20, 30, 40, 50]
average = calculate_average_safe(my_list) 
print(f"Average: {average}") #This will print 30 as intended