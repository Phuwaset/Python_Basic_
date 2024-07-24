# Initialize an empty dictionary
thisdict = {}

# Collect information for three students
for num in range(0, 3):
    keys = ["name", "surname", "age", "phone", "LineId", "sex"]
    student_info = {}
    
    for key in keys:
        value = input(f"{key} for Student {num}: ")
        student_info[key] = value
    
    thisdict[f"Student {num}"] = student_info

# Print the collected information
print("--------------------")

for student, info in thisdict.items():
    print(f"{student}:")
    for key, value in info.items():
        print(f"  {key} : {value}")
    print("--------------------")
