def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(criteria):
    if len(criteria) < 2 or len(criteria) > 6:
        return False
    if criteria[0].isalpha() == False or criteria[1].isalpha() == False:
        return False
    i = 0
    while i < len(criteria):
        if criteria[i].isalpha() == False:
            if criteria[i] == "0":
                return False
            else:
                break
        i = i + 1

    for character in criteria:
        if character in ['.', "", "!", "?"]:
            return False
    return True


main()
