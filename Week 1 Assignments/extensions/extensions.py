
x = input("whats the name of the file? ")

#makes all input lowercase and strips away white space
y = x.lower().strip()

if y.endswith(".gif"):
    print("image/gif")
elif y.endswith(".jpg"):
    print("image/jpeg")
elif y.endswith(".jpeg"):
    print("image/jpeg")
elif y.endswith(".png"):
    print("image/png")
elif y.endswith(".pdf"):
    print("application/pdf")
elif y.endswith(".txt"):
    print("text/plain")
elif y.endswith(".zip"):
    print("application/zip")
elif y.endswith(".bin"):
    print("application/octet-stream")
elif y == "myfile":
    print("application/octet-stream")
