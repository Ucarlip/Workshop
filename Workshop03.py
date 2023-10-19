#จงเขียนโปรแกรมPython ของโปรแกรมคำนวณภาษี ณ ที จ่ายของสินค้า โดยรับชื่อสินค้า
#และราคาสินค้า ทางแป้นพิมพ์และแสดงผลภาษีที คำนวณได้ทางหน้าจอ ทั้งนี้ภาษีคิดที ร้อยละ 7 ของราคาสินค้า

# 1รับข้อมูล 2 คำนวณภาษีสินค้า 3 เเสดงผลภาษีของสินค้า 4 ชื่อโปรเเกรม

def inputData() :
    name = input('ชื่อสินค้า : ')
    price = float(input('ราคาสินค้า : '))
    return name,price
def caltax(price) :
    tax = price+(price*7/100)
    return tax
def showtax() :
    print(f'ชื่อสินค้า {name}')
    print(f'ราคาสิ้นค้า(ต้นทุน) {price:.2f} บาท')
    print(f'ภาษีสินค้า {tax:.2f} บาท')
def Showprogram() :
    print('---***คำนวนภาษีสินค้า***---')

print('-----------------------------')
Showprogram( )
print('-----------------------------')
name,price = inputData( )
print('-----------------------------')
tax = caltax(price)
print('-----------------------------')
showtax()

