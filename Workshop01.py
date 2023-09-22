#1. จงเขียนโปรแกรมPython ค านวณหาราคาขายสินค้า โดยรับชื อสินค้า และราคาสินค้า(ต้นทุน) ทางแป้นพิมพ์
#แล้วคำนวณหาราคาขายของสินค้า โดยราคาขายสินค้าจะคิดเพิ มจากราคาสินค้า (ต้นทุน) ร้อยละ 10
#สูตร ราคาขายสินค้า  =  ราคาสินค้า(ต้นทุน)  + (ราคาสินค้า(ต้นทุน) * 10 / 100)

def inputData( ) :
    name = input('ชื่อสินค้า : ')
    price = float(input('ราคาสินค้า(ต้นทุน) : '))
    return name,price
def calselprice (price) :
    saleprice = (price+(price*10/100))
    return saleprice
def showproductsale(name, price , saleprice) :
    print(f'ชื่อสินค้า {name}')
    print(f'ราคาสินค้า {price:.2f} บาท')
    print(f'ราคาขาย {saleprice:.2f} บาท')

print('-----------------------------')
print('------**Product Sale**-------')
print('-----------------------------')
name, price = inputData( )
pricesale = calselprice( price )
print('-----------------------------')
showproductsale( name, price, pricesale)
print('-----------------------------')