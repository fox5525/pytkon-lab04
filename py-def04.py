#โปรแกรมหาพื้นที่สามเหลี่ยม
#ส่วนที่1 เก็บฟังก์ชันที่ใช้บ่อย
def add_numbers(base, height):
    sum = base * height / 2

    return sum
#ส่วนที่2 ติดต่อกับผู้ใช้
base = float(input("กรุณากรอกฐานของสามเหลี่ยม: "))
height = float(input("กรุณากรอกความสูงของสามเหลี่ยม: "))
area = add_numbers(base, height)
print("พื้นที่ของสามเหลี่ยมคือ:", area)