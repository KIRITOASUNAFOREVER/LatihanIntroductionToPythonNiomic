def Menu():
    print("Program Penjumlahan dan Perkalian Matriks")
    print("1. Penjumlahan Matriks")
    print("2. Perkalian Matriks")

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t", matrix[i][j], end=" ")
        print("\n")

def penjumlahanMatriks():
    m = int(input("Masukkan Jumlah Baris : "))
    n = int(input("Masukkan Jumlah Kolom : "))
    array1 = [[0 for j in range(0, n)] for i in range(0, m)]
    array2 = [[0 for j in range(0, n)] for i in range(0, m)]
    hasil_matrix = [[0 for j in range(0, n)] for i in range(0, m)]
    print()
    print("Masukkan Elemen Matriks : ")
    for i in range(0, m):
        for j in range(0, n):
            array1[i][j] = int(input("Matriks1[" + str(i) + "][" + str(j) + "]: "))

    print("Hasil Matriks Pertama")
    print_matrix(array1)
    input()
    for i in range(0, m):
        for j in range(0, n):
            array2[i][j] = int(input("Matriks2[" + str(i) + "][" + str(j) + "]: "))
    print("Hasil Matriks Kedua")
    print_matrix(array2)
    input()

    for i in range(0, m):
        for j in range(0, n):
            hasil_matrix[i][j] = array1[i][j] + array2[i][j]

    print("Hasil Penjumlahan Matriks")
    print_matrix(hasil_matrix)



def perkalianMatriks():
    print("Matriks Pertama : ")
    m = int(input("Masukkan Jumlah Baris Matriks Pertama : "))
    n = int(input("Masukkan Jumlah Kolom Matriks Pertama : "))
    array1 = [[0 for j in range(0, n)] for i in range(0, m)]
    print()
    print("Masukkan Elemen Matriks Pertama : ")
    for i in range(0, m):
        for j in range(0, n):
            array1[i][j] = int(input("Matriks1[" + str(i) +"][" + str(j) + "]: "))
    print("Hasil Matriks Pertama")
    print_matrix(array1)
    input()

    print("Matriks Kedua : ")
    p = int(input("Masukkan Jumlah Baris Matriks Kedua : "))
    q = int(input("Masukkan Jumlah Kolom Matriks Kedua : "))
    array2 = [[0 for j in range(0, q)] for i in range(0, p)]
    print()
    print("Masukkan Elemen Matriks Kedua : ")
    for i in range(0, p):
        for j in range(0, q):
            array2[i][j] = int(input("Matriks2[" + str(i) +"][" + str(j) + "]: "))
    print("Hasil Matriks Kedua")
    print_matrix(array2)
    input()

    if (n != p):
        print("Tidak Bisa Melakukan Perkalian Matriks!!!, Karena Jumlah Baris Pada Matriks Pertama TIDAK SAMA dengan Jumlah Kolom Matriks Kedua")
        exit()

    result = [[0 for j in range(0, q)] for i in range(0, m)]

    for i in range(0, m):
        for j in range(0, q):
            for k in range(0, n):
                result[i][j] += array1[i][k] * array2[k][j]

    print("Hasil Perkalian Matriks")
    print_matrix(result)



while True:
    Menu()
    pilihan = int(input("Masukkan Pilihan Anda [1/2] : "))

    if pilihan==1:
        penjumlahanMatriks()
    elif pilihan==2:
        perkalianMatriks()