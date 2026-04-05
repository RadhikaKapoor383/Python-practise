# === TUPLE BANANA ===
point      = (10, 20)                  # x, y
color      = (255, 128, 0)             # RGB
student    = ("Ali", 20, "CS", 3.8)    # naam, age, dept, gpa
single     = (42,)                     # ek element — comma zaroori!
empty      = ()                        # khali tuple

print(point[0])
print(student[-1])
print(color[1:])

# point[0] = 99 type error tuple doesnot support assignment

point = (33.74, 73.44)
lat, lon = point
print(point)
print(lat, " ", lon)
student = ("Ali", 20, "CS")
name, age, dept = student
print(name, age, dept)

# unpacking in loop
cities = [
    ("Karachi",  24.86, 67.01),
    ("Lahore",   31.55, 74.35),
    ("Islamabad",33.72, 73.04),
]
for city, lat, lon in cities:
    print(f"{city}: {lat}, {lon}")
    
# Ek value ignore karna — underscore use karo
name, age, _ = ("Ali", 20, "CS")   # age ignore kiya
print(name, age)   # Ali  20

# Shift to list when have to add the elements
t = (1, 2, 3)
print(t)
l = list(t)
l.append(4)
t = tuple(l)
print(t)

# enumerate and zip
# enumerate when we want index too
fruits = ("apple", "mango", "banana")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
    
# zip when we want to loop two lists at the same time
names  = ("Ali", "Sana", "Usman")
marks  = (85,    92,     78    )
for name, mark in zip(names, marks):
    print(f"{name}: {mark}")