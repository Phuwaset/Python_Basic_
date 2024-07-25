# Python_Basic_Sec2
 3and2.py

อธิบายโค้ด:
การประกาศฟังก์ชัน process_command:

def process_command(command_input):
ฟังก์ชันนี้รับพารามิเตอร์ command_input ซึ่งเป็นสตริงที่เราจะประมวลผล
การแปลงข้อมูล:

command_input = command_input.lower().strip()
command_input.lower() ใช้แปลงสตริงทั้งหมดให้เป็นตัวพิมพ์เล็ก
command_input.strip() ใช้ลบช่องว่างที่อยู่หน้าหรือหลังของสตริง
cmd, para = command_input.split(',')
split(',') ใช้แยกสตริงตามเครื่องหมายคอมม่า (,). ผลลัพธ์จะเป็นรายการที่มีสองส่วน: คำสั่ง (command) และพารามิเตอร์ (parameter)
cmd = cmd.strip()
ใช้ลบช่องว่างที่อาจจะเหลืออยู่รอบคำสั่ง
para = para.strip()
ใช้ลบช่องว่างที่อาจจะเหลืออยู่รอบพารามิเตอร์
การตรวจสอบคำสั่ง:

if cmd == 'on':
ตรวจสอบว่าคำสั่งเป็น 'on' หรือไม่
ถ้าใช่ จะแสดงผลลัพธ์ว่า "cmd = on" และ "Run On => <parameter>"
elif cmd == 'off':
ตรวจสอบว่าคำสั่งเป็น 'off' หรือไม่
ถ้าใช่ จะแสดงผลลัพธ์ว่า "cmd = off" และ "Run Off => <parameter>"
else:
ถ้าคำสั่งไม่ใช่ 'on' หรือ 'off' จะพิมพ์ว่า "Unknown command"
การใช้งานฟังก์ชัน:

input_str1 = input("Command (3), paramitor (2) : ")
รับข้อมูลจากผู้ใช้ (คอมมานด์และพารามิเตอร์)
process_command(input_str1)
เรียกฟังก์ชัน process_command โดยส่งข้อมูลที่รับจากผู้ใช้ไปยังฟังก์ชัน
input_str2 = input("Command (3), paramitor (2) : ")
รับข้อมูลอีกชุดหนึ่งจากผู้ใช้
process_command(input_str2)
เรียกฟังก์ชัน process_command อีกครั้งด้วยข้อมูลชุดใหม่
