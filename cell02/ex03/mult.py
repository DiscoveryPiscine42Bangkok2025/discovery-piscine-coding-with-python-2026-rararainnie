num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
sum = num1 * num2

print(f"{num1} x {num2} = {sum}")

if sum == 0:
    print("This result is positive and negative.")
elif sum > 0:
    print("This result is positive.")
else:
    print("This result is negative.")