#input
inty = input("Expression: ")

#convert to variables
x, y, z = inty.split()

#change to float
fltx = float(x)
fltz = float(z)

#calculate
if y == "+":
    answer = fltx + fltz
elif y == "-":
    answer = fltx - fltz
elif y == "*":
    answer = fltx * fltz
elif y == "/":
    answer = fltx / fltz

print(round(answer, 1))
