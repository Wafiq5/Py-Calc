from fractions import Fraction
print("Y and X intercepts from equations in standard form")
print("This is how to write the expression: (A)x+(B)x=(C)")

def x_y_intercept(A, B, C):

    A = Fraction(A)
    B = Fraction(B)
    C = Fraction(C)

    if A != 0:
        x_intercept = C / A
    else:
        return "No X-intercept"

    if B != 0:
        y_intercept = C / B
    else:
        return "No Y-intercept"

    return (f"X-intercept = ({x_intercept}, 0)" 
            "\n" f"Y-intercept = (0, {y_intercept})")


try:
    A = float(input("(A) = "))
    B = float(input("(B) = "))
    C = float(input("(C) = "))
    result = x_y_intercept(A, B, C)
    print(result)
except ValueError:
    print("Fill all the inputs (Run the code again)")