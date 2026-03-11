# get a string
# if chr is lower make it upper
string = "This string should be in UPPer Case."

for char in string:
    if not char.isupper():
        print(char.swapcase(), end="")
    else:
        print(char, end="")