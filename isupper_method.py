string = "abcdefg hi! eheheheh"

# how isupper() works
print(string.isupper())

for char in string:
    if char > string[string.index(char)+1]:
        print(char)

print(string.index("a"))