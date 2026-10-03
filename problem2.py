import json

student = {
    "name": "Rahim",
    "age": 20,
    "department": "CSE",
}

# Convert the dictionary into a JSON-formatted string and print it.
student_json = json.dumps(student)

print(student_json)
