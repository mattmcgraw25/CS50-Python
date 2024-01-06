
#bank teller gives the customer a greeting
x = input("Greeting: ")

#makes all input lowercase and strips away white space
y = x.lower().strip()

#if it starts with hello you get $0 or if it starts with h you get $20
if y.startswith("hello"):
    print("$0")
elif y.startswith("h"):
    print("$20")
else:
    print("$100")
