#!/usr/bin/env python3

original = [2, 8, 9, 48, 8, 22, -12, 2]

new_values = []

for number in original:
    if number > 5:
        new_values.append(number + 2)

new_array = set(new_values)

print(original)
print(new_array)
