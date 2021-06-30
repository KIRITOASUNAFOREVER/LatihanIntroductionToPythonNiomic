jumlahHari =  int(input("Masukkan Jumlah Hari : "))

jumlahTahun  = 0
jumlahBulan  = 0

while(jumlahHari >= 365):
 jumlahHari = jumlahHari - 365
 jumlahTahun = jumlahTahun + 1

while(jumlahHari >= 30):
 jumlahHari = jumlahHari - 30
 jumlahBulan = jumlahBulan + 1

print(jumlahTahun,"Tahun",jumlahBulan,"Bulan",jumlahHari,"Hari")
