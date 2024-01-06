
Tweet = input("Input: ")

print("Output: ", end="")

for letter_list in Tweet:
    if not letter_list.lower() in ["a", "e", "i", "o", "u"]:
        print(letter_list, end="")

print()

