#6. จงเขียนโปรแกรมPython ของโปรแกรมค านวณอัตราดอกเบี้ยเงินกู้ โดยรับชื อผู้กู้ และจ านวนเงินกู้ทางแป้นพิมพ์ 
#และแสดงผลอัตราดอกเบี้ยเงินกู้ที ค านวณได้ทางหน้าจอ ทั้งนี้อัตราดอกเบี้ยคิดจากยอดเงินกู้ 
#หากเงินกู้ตั้งแต่ 1000บาทขึ้นไป คิดอัตราดอกเบี้ยที ร้อยละ 2.5 ของเงินกู้ หากไม่ถึงคิดอัตราดอกเบี้ยที ร้อยละ 5.5 ของเงินกู้
#1.รับค่าข้อมูลผู้กู้ยืมทางแป้นพิมพ์ 2.คำนวณอัตราดอกเบี้ย 3.แสดงผลการคำนวณทางหน้าจอ 4.แสดงชื่อโปรแกรมทางหน้าจอ

def inputData( ) :
    name = input('โปรป้อนชื่อของคุณ : ')
    loan = int(input('โปรดใส่ยอดเงินที่ต้องการจะกู้ : '))
    return name,loan

def calInterestRate(loan) :
    if loan >= 1000 :
        InterestRate=loan+loan*2.5/100
    else :
        InterestRate=loan+loan*5.5/100
    return InterestRate

def showInterestRate ( ) :
    print(f'ชื่อของผู้กู้คือ {name}')
    print(f'ยอดเงินกู้ {load:.2f} บาท')
    print(f'อัตราดอกเบี้ยเงินกู้ของคุณ {InterestRate} บาท')
    print('**------------------------------------------**')

def showProgramName( ) :
    print('**------------------------------------------**')
    print('**----------โปรแกรมคำนวณอัตราดอกเบี้ย----------**')
    print('**------------------------------------------**')

name,load=inputData( )
InterestRate=calInterestRate(load)
showProgramName( )
showInterestRate( )