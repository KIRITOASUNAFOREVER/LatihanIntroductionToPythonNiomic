#def
print ('"WELCOME TO"')
print('program menghitung luas bangun datar')
print()
def menu():
    print('menu pilihan')
    print('1. luas persegi')
    print('2. persegi panjang')
    print('3. luas segitiga')
    print('4. luas lingkaran')
    print('5. exit')

while True:
    menu()
    pilihan = int(input('masukkan pilihan anda :'))
    if pilihan==1:
        s = float(input('diketahui sisi:'))
        luas = float(s*s)
        print ('hasil luas persegi=',luas)
        input()
    if pilihan==2:
        p = float(input('diketahui panjang:'))
        l = float(input('diketahui lebar:'))
        luas = float(p*l)
        print ('hasil luas persegi panjang:',luas)
        input()
    if pilihan==3:
        a = float(input('diketahui alas:'))
        t = float(input('diketahui tinggi:'))
        luas = float((a*t)/2)
        print ('hasil luas segitiga:',luas)
        input()
    if pilihan==4:
        r = float(input('diketahui jari-jari:'))
        luas = float(3.14*r*r)
        print('hasil luas lingkaran:',luas)
        input()
    if pilihan==5:
        def Menu():
         print ('are you sure want to exit this program?')
         print('yes')
         print('no')
         ulang1 = input()
         if ulang1 == "yes":
             exit()
         else:
            menu()
        Menu()
