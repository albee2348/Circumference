def circumference(radius):
    c = 2 * 3.1416 * radius
    return c

r = float(input("Enter the radius of the circle: "))

result = circumference(r)

print("The circumference of the circle is:", result)