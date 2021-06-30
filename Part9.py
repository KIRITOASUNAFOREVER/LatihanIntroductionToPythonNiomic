import Part8

list1 = []

jumlah = int(input("Masukkan Jumlah Angka yang akan diinput : "))

for i in range(1, jumlah + 1):
    angka = int(input("Masukkan Angka : "))
    list1.append(angka)

print("Angka Terbesar Adalah :",Part8.highestNumber(list1))