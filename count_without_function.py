# get string
# count a char in string
# print count

string = "This string should contain 4 t's."
t_counter = 0

for char in string:
    if char == 't' or char == 'T':
        t_counter += 1

print(t_counter)