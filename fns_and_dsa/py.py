def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9


# Ask user
choice = input("Convert (1) C→F or (2) F→C ? ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    result_f = c_to_f(c)
    print(f"{c}°C = {result_f:.2f}°F")

elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    result_c = f_to_c(f)
    print(f"{f}°F = {result_c:.2f}°C")

else:
    print("Invalid choice!")
