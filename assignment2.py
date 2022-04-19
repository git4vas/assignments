x = int(input("Please enter the first number:"))
y = int(input("Please enter the second number:"))
z = int(input("Please enter the third number:"))
if (x >= y and x >= z):
    largest = x
else: 
    if y >= z:
        largest = y
    else:
        largest = z
print("The largest number is", largest)