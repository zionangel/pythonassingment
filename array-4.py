def contains_value(arr, value):
    return value in arr


arr = [10, 20, 30, 40, 50]
value = 30

if contains_value(arr, value):
    print(f"Array contains the value {value}")
else:
    print(f"Array does not contain the value {value}")