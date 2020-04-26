#Import บางฟังก์ชันใน Module แบบต้องระบุเอาเฉพาะตัว
from numbers import factorial,fibonacci

#เรียกใช้งาน
print(factorial(5))
print(fibonacci(100))

#-------------------------------------------------


#Import บางฟังก์ชันใน Module แบบไม่ต้องระบุเอาเฉพาะตัว
from numbers import*

#เรียกใช้งาน
print(factorial(6))
print(fibonacci(200))

#-------------------------------------------------


#import และเปลี่ยนชื่อฟังก์ชัน (นามแฝง) alias
from numbers import factorial as fa, fibonacci as fi

#เรียกใช้งาน
print(fa(7))
print(fi(300))

#-------------------------------------------------


#Import ทั้งหมดทุกฟังก์ชันใน Module
import numbers


#เรียกใช้งาน
print(numbers.factorial(8))
print(numbers.fibonacci(400))
