list = []

while True:
    try:
        numbers = float(input("Please give me a number: "))
        list.append(numbers)
    except ValueError:
        print(sum(list)/len(list))
        break