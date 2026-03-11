odd_counter = 0

for number in range(5):
    number = float(input("Give me a number: "))

    if number %2 != 0:
        odd_counter += 1

print(odd_counter)