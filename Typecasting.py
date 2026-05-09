# Typecasting is the process of converting a variable from one data type to another
# str(), int(), float(), bool()

name = "Aksh C."
age = 20
gpa = 3.7
is_student = True

print(type(gpa))

gpa = int(gpa)
print(gpa)
print(type(gpa))

age = float(age)
print(age)

age += 1  # "age = age +1" works the same

print(age)

age = str(age)
age += "1"
print(age)

name = bool(name)
print(name)