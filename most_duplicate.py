# make infinite loop
# get numbers
# get the highest num of duplicates
# print the number not the count
list = {}
while True:
    try:
        numbers = float(input("Please input a number: "))
        list[numbers] = list.get(numbers,0) + 1
    except ValueError:
        