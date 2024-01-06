
x = input("Fraction: ")


while True:
    try:
        list = x.split("/")
        numerator = int(list[0])
        denominator = int(list[1])
        result = (numerator/denominator)
        if result <= 1:
            break
    except(ValueError, ZeroDivisionError):
        pass
needs_rounding = result * 100
final = round(needs_rounding)
if final <= 1:
    print("E")
elif final >= 99:
    print("F")
else:
    print(f"{final}%")


