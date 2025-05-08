student = {
    "name": "Tara",
    "age": 21,
    "course": "Python"
}
print(student["name"])  


student["age"] = 22              # Update value
student["email"] = "tara@mail.com"  # Add new key
del student["course"]            # Delete a key

for key, value in student.items():
    print(key, "->", value)
