# Function code

from math import pi

# defining function area
def area(radius):
	# Area formula
	A = pi * radius**2
	print("\nThe Area of the circle is ")
	print("Actual value: ", A)
	print("Approximate value: ", round(A, 2))

print("AREA OF CIRCLE CALCULATOR\n")
print("To calculate the area of a circle.")

# radius input
radius = int(input("Enter the value of the radius of a circle: "))
# Calling function
area(radius)
