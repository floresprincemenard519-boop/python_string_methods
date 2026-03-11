# get 10 numbers 
# store numbers in a list 
# if a number is in the list remove it and just retain the non duplicated ones
list = []
for num in range(10):
    numbers = float(input("Input a number: "))
    list.append(numbers) 
    if numbers in list:
        list.remove(numbers)

print(list)