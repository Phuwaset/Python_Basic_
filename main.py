# # Initialize an empty dictionary
# thisdict = {}

# # Collect information for three students
# for num in range(0, 3):
#     keys = ["name", "surname", "age", "phone", "LineId", "sex"]
#     student_info = {}
    
#     for key in keys:
#         value = input(f"{key} for Student {num}: ")
#         student_info[key] = value
    
#     thisdict[f"Student {num}"] = student_info

# # Print the collected information
# print("--------------------")

# for student, info in thisdict.items():
#     print(f"{student}:")
#     for key, value in info.items():
#         print(f"  {key} : {value}")
#     print("--------------------")


# -------------------------------------------------------------------------------------------


# Code  อาจารย์ Array and Dictionary

x = [{} , {} , {}]

for i in range(3):
    x[i].update({
        "name": input("name: "),
        "surname": input("surname: "),
        "age": input("age: "),
        "phone": input("phone: "),
        "lineID": input("Line ID: "),
        "sex": input("sex: ")
    })

print("------")
for i in range(3):
    print(f"Student name: {x[i]['name']}, Surname: {x[i]['surname']}, Age: {x[i]['age']}, Phone: {x[i]['phone']}, Line ID: {x[i]['lineID']}, Sex: {x[i]['sex']}")


# # Code  By Phuwaset ย่อโดยใช้โค้ดสั้นลงและกระชับขึ้นได้โดยใช้ฟังก์ชัน zip และการวนลูปผ่านรายการของคีย์ เพื่ออัปเดตข้อมูลในแต่ละ dictionary ใน x:
# fields = ["name", "surname", "age", "phone", "lineID", "sex"]
# x = [{} for _ in range(3)]

# for i in range(3):
#     for field in fields:
#         x[i][field] = input(f"{field}: ")

# print("------")
# for student in x:
#     print(", ".join(f"{key.capitalize()}: {value}" for key, value in student.items()))
