array_of_numbers = [1, 1, 1, 1, 1, 2, 1, 1, 1, 1]
array_of_numbers.sort()
num1 = array_of_numbers[0]
num2 = array_of_numbers[len(array_of_numbers)-1]
unique_el = None

if num1 == array_of_numbers[1]:
    unique_el = num2
else:
    unique_el = num1

print(unique_el)
