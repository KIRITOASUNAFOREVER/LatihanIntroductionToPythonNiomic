
def detikKeJamMenitDetik():
 print("Konversi Detik Ke Jam Menit Detik")
 detikAwal = int(input("Masukkan jumlah Detik yang Mau Dihitung : "))
 jam=detikAwal // (60*60)
 sec= detikAwal-((60*60)*jam)
 menit=sec // 60
 sec= sec - (60*menit)
 print("Hasil Konversi  : ",jam,"Jam   : ", menit,"Menit   : ",sec,"Detik")

def jamMenitDetikKeDetik():
 print("Konversi Jam Menit Detik Ke Detik")
 jam = int(input("Berapa Jam : "))
 menit = int(input("Berapa Menit : "))
 detik = int(input("Berapa Detik : "))

 jamDetik = jam * 3600
 menitDetik = menit * 60

 totalDetik = jamDetik + menitDetik + detik

 print("Hasil Konversi : ",totalDetik,"Detik")


def Menu():
 print("1. Konversi Jam Menit Detik Ke Detik")
 print("2. Konversi Detik Ke Jam Menit Detik")

Menu()
pilihan = int(input("Masukkan Pilihan Anda [1/2]: "))

if pilihan ==1:
 jamMenitDetikKeDetik()
elif pilihan ==2:
 detikKeJamMenitDetik()