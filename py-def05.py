#โปรมแกรตัดเกรด A B C D F
def cut_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'
#รับค่าคะแนนจากผู้ใช้
score = int(input("กรุณากรอกคะแนน: "))
#เรียกใช้ฟังก์ชันและแสดงผลลัพธ์
grade = cut_grade(score)
print("เกรดของคุณคือ:", grade)