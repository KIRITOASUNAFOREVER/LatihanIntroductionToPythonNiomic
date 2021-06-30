import math
class luas:
    def __init__(self, s,panjang,lebar,tinggi,jarijari):
        self.sisi = s
        self.panjang = panjang
        self.lebar   = lebar
        self.tinggi  = tinggi
        self.jarijari = jarijari

    def volumeKubus(self):
        print("Volume Kubus = ", self.sisi ** 3)

    def volumeBalok(self):
        print("Volume Balok = ", self.panjang*self.lebar*self.tinggi)

    def volumeTabung(self):
        print("Volume Tabung = ", math.pi*self.jarijari*self.jarijari*self.tinggi)

    def volumeKerucut(self):
        print("Volume Kerucut = ", math.pi * self.jarijari * self.jarijari * self.tinggi*1/3)

    def volumeBola(self):
        print("Volume Bola = ", math.pi * self.jarijari * self.jarijari * self.tinggi*self.jarijari*4/3)

def Menu():
    print("Program Menghitung Volume dengan Class")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Bola")

while True:
    Menu()
    pilihan = int(input("Masukkan Pilihan Anda : "))

    if pilihan==1:
        sisi = int(input("Masukkan Panjang Sisi Kubus : "))
        kubus = luas(sisi,1,1,1,1)
        kubus.volumeKubus()
        input()
    elif pilihan==2:
        panjang = int(input("Masukkan Panjang Balok : "))
        lebar   = int(input("Masukkan Lebar   Balok : "))
        tinggiBalok  = int(input("Masukkan Tinggi  Balok : "))
        balok = luas(1,panjang,lebar,tinggiBalok,1)
        balok.volumeBalok()
        input()
    elif pilihan==3:
        jarijari = int(input("Masukkan Panjang Jari-Jari Tabung : "))
        tinggiTabung  = int(input("Masukkan Tinggi Tabung : "))
        Tabung = luas(1, 1, 1, tinggiTabung,jarijari)
        Tabung.volumeTabung()
        input()
    elif pilihan==4:
        jarijari = int(input("Masukkan Panjang Jari-Jari Kerucut : "))
        tinggiKerucut  = int(input("Masukkan Tinggi Kerucut : "))
        Kerucut = luas(1, 1, 1, tinggiKerucut,jarijari)
        Kerucut.volumeKerucut()
        input()
    elif pilihan==5:
        jarijari = int(input("Masukkan Panjang Jari-Jari Bola : "))
        tinggiBola  = int(input("Masukkan Tinggi Bola : "))
        Bola = luas(1, 1, 1, tinggiBola,jarijari)
        Bola.volumeBola()
        input()