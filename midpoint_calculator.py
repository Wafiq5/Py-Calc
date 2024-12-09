print("Midpoint calculator")
print("This is how to write the expression: (x1, y1) and (x2, y2)")


def midpoint(x1, y1, x2, y2):
    x_midpoint_coord = (x1 + x2) / 2
    y_midpoint_coord = (y1 + y2) / 2

    return f"({x_midpoint_coord}, {y_midpoint_coord})"


try:
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))

    result = midpoint(x1, y1, x2, y2)

    print("Midpoint =", result)

except ValueError:
    print("Fill all the inputs (Run the code again)")
