total_even = 0

for num in range(10):
    numbers = float(input("Please input a number: "))

    if numbers % 2 == 0:
        total_even += 1

print(total_even)