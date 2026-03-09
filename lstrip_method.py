string = "   What a beautiful world! Helloooooo!"
spaceless_string = ""
non_space_detected = False

for char in string:
    if char != " " or non_space_detected:
        spaceless_string += char
        non_space_detected = True

print(spaceless_string)