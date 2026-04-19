# for loop
for i in range(5):
    print(i)

# Break
text_to_iterate = "We are going to iterate through this text"
for letter in text_to_iterate:
    if letter == "t":
        break
    print(letter)

# Continue
for i in range(5):
    if i == 3:
        continue # Skips the rest of the code and goes to the next iteration
    print(i)