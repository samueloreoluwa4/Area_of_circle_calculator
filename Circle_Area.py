from math import pi

print("AREA OF CIRCLE CALCULATOR\n")
print("To calculate the area of a circle.")

# Define input radius
radius = int(input("Enter the value of the radius of a circle: "))
# Area of circle formular
A = pi * (radius**2)

# Printing actual and approximate value of area
print("\nThe Area of the circle is ")
print("Actual value: ", A)
print("Approximate value: ", round(A, 2))
