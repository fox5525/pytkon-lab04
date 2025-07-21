#menu driven program
def main_menu():
    print("=== เมนูหลัก ===")
    print("1.หาพื้นที่สี่เหลี่ยม")
    print("2.หาพื้นที่สามเหลี่ยม")
    print("3.หาพื้นที่สี่เหลี่ยมผืนผ้า ")
    print("4.หาพื้นที่ขนมเปียกปูนเหลี่ยม ")
    print("5.หาพื้นที่สีคางหมูเหลี่ยม ")
    choice = input("กรุณาเลือกเมนู (1-5): ")
    calculate_area(choice)

def calculate_area(choice):
    if choice == '1':
        length = float(input("กรุณากรอกความยาวของสี่เหลี่ยม: "))
        width = float(input("กรุณากรอกความกว้างของสี่เหลี่ยม: "))
        area = length * width
        print(f"พื้นที่ของสี่เหลี่ยมคือ: {area}")
    elif choice == '2':
        base = float(input("กรุณากรอกฐานของสามเหลี่ยม: "))
        height = float(input("กรุณากรอกความสูงของสามเหลี่ยม: "))
        area = 0.5 * base * height
        print(f"พื้นที่ของสามเหลี่ยมคือ: {area}")
    elif choice == '3':
        length = float(input("กรุณากรอกความยาวของสี่เหลี่ยมผืนผ้า: "))
        width = float(input("กรุณากรอกความกว้างของสี่เหลี่ยมผืนผ้า: "))
        area = length * width
        print(f"พื้นที่ของสี่เหลี่ยมผืนผ้าคือ: {area}")
    elif choice == '4':
        side = float(input("กรุณากรอกความยาวด้านขนมเปียกปูนเหลี่ยม: "))
        area = side ** 2
        print(f"พื้นที่ของขนมเปียกปูนเหลี่ยมคือ: {area}")
    elif choice == '5':
        base1 = float(input("กรุณากรอกฐานที่ 1 ของสีคางหมูเหลี่ยม: "))
        base2 = float(input("กรุณากรอกฐานที่ 2 ของสีคางหมูเหลี่ยม: "))
        height = float(input("กรุณากรอกความสูงของสีคางหมูเหลี่ยม: "))
        area = ((base1 + base2) / 2) * height
        print(f"พื้นที่ของสีคางหมูเหลี่ยมคือ: {area}")
    else:
        print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่")
        print("โปรแกรมจบการทำงาน")
if __name__ == "__main__":
            main_menu()
