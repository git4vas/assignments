x = float(input("Please enter the first angle:"))
y = float(input("Please enter the second angle:"))
z = float(input("Please enter the third angle:"))

if (x > 0 and y > 0 and z > 0):
    if (x+y+z==180):
        if (x >= y and x >= z):
            largest = x
        elif y >= z:
            largest = y
        else:
            largest = z

            if largest > 90:
                triangle = "n obtuse"
            elif largest == 90:
                triangle = " right"
            else:
                triangle = "n acute" 

            print("The triangle is a" + triangle, "triangle")    

    else:
        print("The entered values are not valid.")

else:
    print("Angles smaller than 0 are not valid.")



