uang   = int(input("Masukkan Nominal Uang : "))

penampung   = uang

seribu  = 0
limaRatus = 0
seratus = 0
limaPuluh =0
duaLima = 0

while(uang >= 1000):
    uang = uang -1000
    seribu = seribu+1

while(uang >= 500):
    uang = uang -500
    limaRatus = limaRatus+1

while(uang >= 100):
    uang = uang -100
    seratus = seratus + 1

while(uang >= 50):
    uang = uang -50
    limaPuluh = limaPuluh +1

while(uang >= 25):
    uang = uang - 25
    duaLima =duaLima +1

print("Uang Senilai Rp. ",penampung,"Setara Dengan ",seribu,"Buah Pecahan Rp.1000",limaRatus,"Buah Pecahan Rp. 500",seratus,"Buah Pecahan Rp. 100",limaPuluh,"Buah Pecahan Rp.50",duaLima,"Buah Pecahan Rp. 25")

