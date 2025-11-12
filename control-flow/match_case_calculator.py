# simple cal
f_num = int(input("Enter the first number:"))
s_num =int(input("Enter the second number:"))
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

match operator:
    case "+":
        print(f"The result is {f_num + s_num}")
    case "-":
        print(f"The result is {f_num - s_num}")
    case "*":
        print(f"The result is {f_num * s_num}")
    case "/":
        if s_num ==0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {f_num / s_num}")
    case _:
        print("Invalid operation selected.")