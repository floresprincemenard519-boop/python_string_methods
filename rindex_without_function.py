# get string
# get parameter
# make for loop
# find the first index of parameter
# print it 

string = "The rindex('p') of this string should print 38."

for i in range(len(string)-1, -1, -1):
    if string[i] == 'p':
        print(i)
        break