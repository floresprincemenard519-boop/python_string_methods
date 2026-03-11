# get two nums
# get the numbers in the middle using range or maybe i can use a while loop
first_number = float(input("Please input a number: "))
second_number = float(input("please input another number: "))

if first_number > second_number:
    while first_number != second_number:
        print(first_number)
        first_number -= 1