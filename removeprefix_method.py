string = "   What a beautiful world! Helloooooo!"
prefix_to_remove = "   W"

# how removeprefix() works
print(string.removeprefix('   W'))

# same functionality without using removeprefix()
string = string[len(prefix_to_remove):]
print(string)