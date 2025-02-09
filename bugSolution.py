def function_with_uncommon_error(a, b):
    if a == 0 and b == 0:
        raise ZeroDivisionError("Division by zero is not allowed when both inputs are 0")
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

try:
    result = function_with_uncommon_error(0,0)
    print(result)
except ZeroDivisionError as e:
    print(f"Error: {e}")
    