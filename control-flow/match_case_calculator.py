# simple cal
f_num = float(input("Enter the first number:"))
s_num =float(input("Enter the second number:"))
operator = input("Choose the operation (+, -, *, /):")
# # operation

#
# if operator== "+":
#     print(f"The result is {f_num + s_num}")
# elif operator == "-":
#     print(f"The result is {f_num - s_num}")
# elif operator == "*":
#     print(f"The result is {f_num * s_num}")
# elif operator == "/":
#     print(f"The result is {f_num / s_num}")
# elif s_num ==0 and operator == "/":
#     print("Cannot divide by zero.")

"""
will never be reached, because the earlier elif operator == "/" runs first — and Python will already try to divide by zero,
causing a crash (ZeroDivisionError) before that line executes.
"""
# match_case_calculator.py

match operator:
    case "+":
        print(f"The result is {f_num + s_num}")
    case "-":
        print(f"The result is {f_num - s_num}")
    case "*":
        print(f"The result is {f_num * s_num}")
    case "/":
        if s_num == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {f_num / s_num}")
    case _:
        print("Invalid operation selected.")
