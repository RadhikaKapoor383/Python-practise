# Dictionary is key and value thing
student = {
    "name": "Radhika kapoor",
    "age": 20,
    "course": ["Eng", "maths", "urdu"],
    "marks": [80, 90, 88],
    "dept": "CS"
}
print(student["marks"][0])
print(student.get("gpa"))
print(student.get("gpa"), 0.0)
student["gpa"] = 3.33
student["city"] = "Sukkur"
student["age"] = 21
print(student)

# del student["city"]            # key hatao
# popped = student.pop("age")    # hatao aur value return karo
# print(student)
print(len(student))

d = {"a": 1, "b": 2, "c": 3}
for key in d:
    print(key, d[key])

for key, val in d.items():    # yeh zyada achha tarika
    print(f"{key} → {val}")
print(d.items()) 

class_data = {
    "s001": {"name": "Ali",   "marks": [85, 90, 78], "dept": "CS"},
    "s002": {"name": "Sana",  "marks": [92, 88, 95], "dept": "CS"},
    "s003": {"name": "Usman", "marks": [70, 65, 72], "dept": "EE"},
}

print(class_data["s001"]["name"])
print(class_data["s001"]["dept"])
print(class_data["s001"]["marks"][0])