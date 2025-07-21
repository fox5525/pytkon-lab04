#ฟังก์ชันที่มีการคำนวณ
#2025+543=2568
#โปรแกรมแปลงปี ค.ศ เป็น พ.ศ และ พ.ศ เป็น ค.ศ
def convert_toBE(year):
    print(f"ปี ค.ศ {year} เป็นปี พ.ศ {year + 543}")
def convert_toCE(year):
    print(f"ปี พ.ศ {year} เป็นปี ค.ศ {year - 543}")
#เรียกใช้ฟังก์ชัน
convert_toBE(2000)
convert_toCE(2568)
