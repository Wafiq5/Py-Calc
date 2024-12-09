
# def calculate(A):
#     return eval(f"2**3{A}")


# A = input("Enter")
# print(calculate(A))

print("Average rate of change calculator")
print("This is how to write the expression: Equation = 2**3*x, Interval = [A, B]")

def averageRateOfChange(equation,A,B):
    print(equation)
    equation_test = equation.replace("x", str(A))
    value = eval(equation_test)
    return value



equation = input("Enter the equation (ie. 2**3x): ")
A = float(input("Enter the start of the interval [A]: "))
B = float(input("Enter the end value of the interval [B]: "))

result_test = averageRateOfChange(equation, A, B)
print(result_test)

