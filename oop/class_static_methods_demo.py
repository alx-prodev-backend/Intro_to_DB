# class_static_methods_demo.py
class Calculator:
    # class attribute
    calculation_type = "Arithmetic Operation "

    @staticmethod
    def add(a,b):
        """ Return the sum of two numbers """
        return a+b
    @classmethod
    def multiply(cls, a, b ):
        """ Return the product of two numbers and print the calculation type . """
        print(f"Calculation type: {cls.calculation_type}")
        return a*b

# 🎉 Task 03 Completed!
