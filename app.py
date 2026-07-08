import json

with open("students.json", "r") as file:
    students = json.load(file)

topper = max(students, key=lambda x: x["marks"])

print("Topper:", topper["name"])
print("Marks:", topper["marks"])
