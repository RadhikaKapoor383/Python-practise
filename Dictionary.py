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