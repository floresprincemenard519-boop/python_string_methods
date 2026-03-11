# get 1st num
first_number = float(input("Give me a number: "))
# get another
second_number = float(input("Give me another: "))
# and another
third_number = float(input("Another: "))
# sum all of them
print(first_number + second_number + third_number)

list = []

for number in range(5):
    number = float(input("Give me a number: "))
    list.append(number)
    
print(sum(list))