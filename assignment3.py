x = float(input("Please enter the first angle:"))
y = float(input("Please enter the second angle:"))
z = float(input("Please enter the third angle:"))

if (x > 0 and y > 0 and z > 0 and x+y+z==180):
    if (x >= y and x >= z):
        largest = x
    elif y >= z:
        largest = y
    else:
        largest = z
else:
    print("not an euclidean triangle")

if largest > 90:
    type = "obtuse"
elif largest == 90:
    type = "right"
else:
    type = "acute" 

print("The triangle is", type)    
