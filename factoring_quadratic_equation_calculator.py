from fractions import Fraction
import math
print("Factor quadratic equation")
print("This is how to write the expression: (A)x^2 + (B)x + (C) = 0")

def factor_quadratic(A, B, C):
    A = Fraction(A)
    B = Fraction(B)
    C = Fraction(C)

    discriminant = pow(B, 2) - 4 * A * C

    if discriminant < 0:
        return "No real roots"
    else:
        POSITIVE_quadratic_function_numerator = -B + math.sqrt(discriminant)
        NEGETIVE_quadratic_function_numerator = -B - math.sqrt(discriminant)
        quadratic_function_denominator = 2*A

    root1 = float(POSITIVE_quadratic_function_numerator/quadratic_function_denominator)
    root2 = float(NEGETIVE_quadratic_function_numerator/quadratic_function_denominator)

    root1 = Fraction.from_float(root1).limit_denominator()
    root2 = Fraction.from_float(root2).limit_denominator()

    if A == 1:
        return f"(x {"-" if root1 >= 0 else "+"} {abs(root1)})(x {"-" if root2 >= 0 else "+"} {abs(root2)})"
    else:
        return f"{A}(x {"-" if root1 >= 0 else "+"} {abs(root1)})(x {"-" if root2 >= 0 else "+"} {abs(root2)})"


try:
    A = input("(A) = ")
    B = input("(B) = ")
    C = input("(C) = ")
    result = factor_quadratic(A, B, C)
    print("Simplified factored form =", result)
except ValueError:
    print("Fill all the inputs (Run the code again)")