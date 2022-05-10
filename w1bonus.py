a = float(input("Please enter the value of a:"))
b = float(input("Please enter the value of b:"))
c = float(input("Please enter the value of c:"))

d = b ** 2 - 4 * a * c 

print(d)

if d > 0:
    print("The quadratic equation has 2 real solutions.")
elif d < 0:
    print("The quadratic equation has 2 complex solutions.")
else:
    print("The quadratic equation has 1 real solution.")