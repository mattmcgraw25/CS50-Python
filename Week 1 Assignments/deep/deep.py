
# user inputs their answer
x = input("What is the answer to the Great Question of Life, the Universe and Everything? ")


if x.strip() == "42":
    print("yes")
elif x.lower().strip() == "forty-two":
    print("yes")
elif x.lower().strip() == "forty two":
    print("yes")
else:
    print("no")

