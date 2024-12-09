print("Slope Calculator")
print("This is how to write the expression: (x1, y1) and (x2, y2)")


def slope(x1, y1, x2, y2):
    numerator = y2 - y1
    denominator = x2 - x1

    if denominator == 0:
        return "Undefined slope"
    else:
        result = numerator / denominator
        return result


try:
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    slope = slope(x1, y1, x2, y2)
    print("Slope =", slope)

except ValueError:
    print("Fill all the inputs (Run the code again)")
