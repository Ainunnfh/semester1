# Fungsi Rekursif (Fungsi Lanjutan)
'''
Fungsi rekursi adalah fungsi yang memanggil dirinya sendiri secara berulang.
Jadi di dalam tubuh fungsi kita memanggil fungsi itu sendiri.

Base scenario = statment yang mendifinisikan titik awal
Recursive scenario = tempat terjadinya aksi rekursi dari fungsi yang ada di base

Teknik rekursif, implementasi dari algoritma tipe divide and conquer.
Divide = membagi/memecah persoalan secara terus menerus ke dalam bentuk yang lebih kecil.
Conquer = memecahkan persoalan yang sudah diperkecil hingga mencapai ukuran dimana ia dapat dapat dipecahkan sendiri (base scenario).
Combine = menggabungkan pemecahan/solusi dari seluruh persoalan kecil hingga menjadi solusi untuk persoalan awal.

'''
print(5*"-", "RECURSIVE FUNCTION", 5*"-", "\n")

def fungsiRekursif(n):
    # Base scenario atau bagian basis
    if n < 0:
        return 10
    elif n % 2 == 1: 
        # Recursive scenario atau bagian rekursif
        return fungsiRekursif(n-1) + n 
    else:
        return fungsiRekursif(n-1) + 2*n

print(fungsiRekursif(5))

'''
Peta Algoritma

Divide -> fungsiRekursif(5) = fungsiRekursif(4) + n, fungsiRekursif(n) hanya dapat dipecahkan
jika kita mengetahui fungsiRekursif(4). Langkah ini terus dilakukan hingga bentuk terkecil
yang bisa dipecahkan langsung yaitu fungsiRekursif(-1).

Conquer -> jika sudah mencapai fungsiRekursif(-1), kita sudah ada di base scenario
dan nilainya bisa langsung diberikan yaitu fungsiRekursif(-1) = 10.

Combine -> menggabungkan seluruh hasil pada tahap conquer dari fungsiRekursif(-1), fungsiRekursif(0), fungsiRekursif(1)
sampai fungsiRekursif(4).

Kalo pusing gapapa, saya juga pusing wkwk

Intinya mah fungsi rekursif tuh alurnya gini, sama aja kaya di bandara di tanyain tiketnya 
mana tapi kita lupa ada dimana, jadi kita pulang dulu buat nyari, 
kalo udah dapet baru balik lagi ke bandara, dan ngasih tiketnya sebagi outputnya.
'''

# Soal 1
def jumlahlist(isilist):
    if len(isilist) == 1:
        return isilist[0]
    else:
        return isilist[0] + jumlahlist(isilist[1:])

print(jumlahlist([2,1,3,4,7,6]))

'''
1. isilist = [2,1,3,4,7,6]
= isilist[0] + jumlahlist(isilist[1:])
= 2 + jumlahlist([1,3,4,7,6])

2. isilist = [1,3,4,7,6]
= isilist[0] + jumlahlist(isilist[1:])
= 1 + jumlahlist([3,4,7,6])

3. isilist = [3,4,7,6]
= isilist[0] + jumlahlist(isilist[1:])
= 3 + jumlahlist([4,7,6])

4. isilist = [4,7,6]
= isilist[0] + jumlahlist(isilist[1:])
= 4 + jumlahlist([7,6])

5. isilist = [7,6]
= isilist[0] + jumlahlist(isilist[1:])
= 7 + jumlahlist([6])

3. isilist = [6]
= isilist[0]
= 6

Balik ke awal
7 + jumlahlist([6]) = 7 + 6 = 13
4 + jumlahlist([7,6]) = 4 + 13 = 17
3 + jumlahlist([4,7,6]) = 3 + 17 = 20
1 + jumlahlist([3,4,7,6]) = 1 + 20 = 21
2 + jumlahlist([1,3,4,7,6]) = 2 + 21 = 23

'''

# Soal 2
def sumDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumDigits(int(n/10))

print(sumDigits(3452))
print(sumDigits(45))

'''
Tracing

sumDigits(3452)
= 3452 % 10 + sumDigits(int(3452/10))
= 2 + sumDigits(345)

sumDigits(345)
= 345 % 10 + sumDigits(int(345/10))
= 5 + sumDigits(34)

sumDigits(34)
= 34 % 10 + sumDigits(int(34/10))
= 4 + sumDigits(3)

sumDigits(3)
= 3 % 10 + sumDigits(int(3/10))
= 3 + sumDigits(0)
= 3 + 0
= 3

Balik ke awal
sumDigits(34) = 4 + sumDigits(3) = 4 + 3 = 7
sumDigits(345) = 5 + sumDigits(34) = 5 + 7 = 12
sumDigits(3452) = 2 + sumDigits(345) = 2 + 12 = 14
'''

# Tanda * di dalam parameter
def cetakParam(*var): # menggunakan *, karena jumlah input yang dimasukan user tidak pasti
    for i in var:
        print(i)
    return

cetakParam(9)
cetakParam(27, 35.6)
cetakParam(0, 57, "kuliah")