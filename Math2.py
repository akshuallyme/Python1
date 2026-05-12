import math

# Ex. 1

# print(math.pi)   (3.14...)
# print(math.e)   (2.71...)
# result = math.sqrt(x)    (square root)
# result = math.ceil(x)   (Round up)
# result = math.floor(x)   (Round down)

#Ex. 2

# radius = float(input("Enter the radius of a circle: "))
# circumference = 2 * math.pi * radius
# area = math.pi * radius * radius
# print(f"The circumference is: {round(circumference, 2)}cm")
# print(f"The area is: {round(area, 2)}cm²")

#Ex. 3

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a,2) + pow(b,2))

print(f"Side C is: {c}cm")


