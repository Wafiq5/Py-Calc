import math

print("Pythagorean distance calculator")
print("This is how to write the expression: (x1, y1) and (x2, y2)")


def pythagoreanDistance(x1, y1, x2, y2):
    a_squared = pow(x2 - x1, 2)
    b_squared = pow(y2 - y1, 2)
    c_squared = a_squared + b_squared

    pythagoreanDistance = math.sqrt(c_squared)
    return pythagoreanDistance


try:
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    result = pythagoreanDistance(x1, y1, x2, y2)
    print("Distance =", result)

except:
    print("Fill all the inputs (Run the code again)")
