#โปรมแกรมแสดงจำนวนเฉพาะ
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#จำนวนเฉพาะ คือ จำนวนที่มีตัวหารเฉพาะแค่ 1 และตัวมันเอง
input_number = int(input("กรุณากรอกจำนวน: "))
#ตรวจสอบและแสดงผลลัพธ์
if is_prime(input_number):
    print(f"{input_number} เป็นจำนวนเฉพาะ")
else:
    print(f"{input_number} ไม่เป็นจำนวนเฉพาะ") 