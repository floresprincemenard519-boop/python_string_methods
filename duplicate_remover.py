list = []

for num in range(10):
    numbers = float(input("Input a number: "))
    if numbers in list:
        list.remove(numbers)
    else:
        list.append(numbers) 

for num in list:
    print(num, end=" ")