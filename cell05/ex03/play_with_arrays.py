arr = [2, 8, 9, 48, 8, 22, -12, 2]
newArr = [x + 2 for x in arr if x > 5]

print(arr)
print(list(set(newArr)))