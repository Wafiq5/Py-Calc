from fractions import Fraction

def pointSlope(M, B):
    M = Fraction(M)
    B = Fraction(B)

    if B < 0:
        return f"y+{abs(B)}={M}x"
    else:
        return f"y-{B}={M}x"


def standard(M, B):
    M = Fraction(M)
    B = Fraction(B)

    if M < 0:
        return f"{abs(M)}x+y={B}"
    else:
        return f"-{M}x+y={B}"


try:
    M = Fraction(input("(M) = "))
    B = Fraction(input("(B) = "))
    point_slope = pointSlope(M, B)
    standard = standard(M, B)
    print("Point slope from =", point_slope)
    print("Standard from =", standard)
except ValueError:
    print("Fill all the inputs (Run the code again)")

