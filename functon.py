#การสร้างฟังก์ชั่นแบบไม่มีการ return value
def hello():
    print("Hello k")

#การสร้างฟังก์ชั่นแบบไม่มีการ return value
def hello2(name):
    print(f"Hello {name}")

#การสร้างฟังก์ชั่นแบบมีการ return value
def area(width,heigh):
    total = width*heigh
    return total


#เรียกใช้งานฟังก์ชั้น hello()
hello()

#เรียกใช้งานฟังก์ชั้น hello2()
hello2("Samit")

#เรียกใช้งานฟังก์ชั้น area()
area(5,8)
print(area)
print(area(5,8))
print("พื้นที่ทั้งหมด",area(5,8))

#ฟังก์ชั้นแบบมีค่าเริ่มต้น
def show_info(name="",salary=0.00,lang="not define"):
    print(f"Name : {name}")
    print(f"Salary : {salary}")
    print(f"Language : {lang}")


#เรียกใช้งานฟังก์ชัน show_info()
show_info()
print()
show_info('Samit',12000,'PHP')



