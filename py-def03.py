#ส่วนที่1 เก็บฟังก์ชันที่ใช้บ่อย
def add_numbers(a, b):
    sum = a + b
    return sum
#ส่วนที่2 ติดต่อกับผู้ใช้
num1 = int(input("กรุณากรอกตัวเลข 1: "))#ให้กรอกข้อมูลจากผแป้นพิมพ์
num2 = int(input("กรุณากรอกตัวเลข 2: "))#ให้กรอกข้อมูลจากแป้นพิมพ์
result = add_numbers(num1, num2)#global variable
print("ผลบวกของ", num1, "และ", num2, "คือ", result)