#2. จงเขียนโปรแกรมPython ของโปรแกรมคำนวณหาค่าเฉลียของคะแนนจากการสอบ 3 ครั้ง โดยรับค่า รหัสนักเรียน ชือนักเรียน 
#และคะแนนสอบแต่ละครั้งรวม 3 ครั้งทางแป้นพิมพ์ แล้วแสดงผลค่าเฉลี ยที ค านวณได้ทางหน้าจอ

#1 รับข้อมูลนักนักเรียน 2 คำนวณหาค่าเฉลี่ยคะเเนน 3 แสดงผล 4 แสดงชื่อโปรเเกรม

def inputData( ) :
    name = ('ชื่อนักศึกษา : ')
    idstuden = input('รหัสนักศึกษา : ')
    grade1 = float(input('คะเเนนสอบครั้งแรก : '))
    grade2 = float(input('คะเเนนสอบครั้งที่สอง : '))
    grade3 = float(input('คะเเนนสอบครั้งสุดท้าย : '))
    return name,idstuden,grade1,grade2,grade3
def calaveragegrade (grade1,grade2,grade3) :
    averagegrade = (grade1+grade2+grade3)/3
    return averagegrade
def showcalaveragegrade () :
    print(f'ชื่อนักศึกษา {name} ')
    print(f'รหัสนักศึกษา {name} ')
    print(f'คะเเนนเฉลี่ยสะสมนักศึกษา {averagegrade} ')
def Showprogramname() :
    print('---**Programname**---')

print('-------------------------------')
Showprogramname( )
print('-------------------------------')
name,idstuden,grade1,grade2,grade3 = inputData( )
print('-------------------------------')
averagegrade=calaveragegrade(grade1,grade2,grade3)
showcalaveragegrade( )
print('-------------------------------')