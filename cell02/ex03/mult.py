#!/usr/bin/env python3
print("Enter the first number:")
num1 = float(input())
print("Enter the second number:")
num2 = float(input())
result = num1 * num2
if result.is_integer():
    display_result = int(result)
else:
    display_result = result

if num1.is_integer():
    display_num1 = int(num1)
else:
    display_num1 = num1

if num2.is_integer():
    display_num2 = int(num2)
else:
    display_num2 = num2
print(f"{display_num1} x {display_num2} = {display_result}")

# Check
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
