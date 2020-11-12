#Function
'''
A function is a block of code which only runs when it is called
Fungsi adalah barisan kode yang sudah dibuat dan hanya berjalan ketika dipanggil

print(), input(), len() adalah built in function
function yang sudah ada di dalam python dan tinggal pake aja

Fungsi juga dapat dipanggil pada fungsi lain, bahkan bisa memanggil dirinya sendiri.
Fungsi yang memanggil dirinya sendiri, disebut fungsi rekursif.
'''
print(5*"-", "FUNCTION", 5*"-", "\n")

'''
sintaks sebuah function

def namafungsi(paramterfungi):
    isifungsi
'''

def my_funtion():       # Membuat sebuah function, diawali dengan def(definition)
    print("Hello from a funtion")

my_funtion()      # Memanggil function dan mencetak isi function

# Sebuah fungsi dapat memiliki parameter.
# Melalui parameter itu kita bisa mengirimkan nilai ke dalam fungsi


def my_funtion(name):     # nama adalah parameter
    print(name, "Raflesia")

my_funtion("Dadang")     # Dadang dimasukan ke dalam parameter
my_funtion("Mamat")     # Mamat dimasukan ke dalam parameter


# Fungsi mencetak perkalian 3 bilangan:
def jum3bil(a, b, c): # a ,b, c adalah parameter
    print(a + b + c)

jum3bil(2, 3, 4)    # 2, 3, 4 adalah nilai yang dimasukan ke dalam paramater
jum3bil(1, 2, 3)    # 1, 2, 3 adalah nilai yang dimasukan ke dalam parameter


'''
return adalah kata kunci untuk mengembalikan nilai ke dalam function
return ditulis dengan diikuti nilai atau variabel yang ingin dikembalikan
sehingga function yang tadi bernilai yang diberikan oleh return

function without return biasa disebut dengan prosedur
'''

def angka(x):
    return 5 * x    # Mengmbalikan nilai 5 * x ke dalam function angka(x) sehingga angka(x) bernilai 5 * x

angka(3)    # Memproses x sebagai 3 without print it out
print(angka(3))     # Memproses x sebagai 3 dan hasilnya dicetak


# def volume_balok():
#     panjang = float(input("Masukan panjang: "))
#     lebar = float(input("Masukan lebar: "))
#     tinggi = float(input("Masukan tinggi: "))
#     volume = panjang * lebar * tinggi
#     return volume       # Mengembalikan nilai volume ke dalam volume_balok() sehingga volume_balok() bernilai volume

# Membuat fungsi untuk angka ganji genap
def even(x):
    if x % 2 == 0:
        print("Yes")
    else:
        print("No")

even(3)

# None
def add_numbers(x, y):
    total = x + y
    return total # proses function berhenti sampai return
    print("This won't be printed") # tidak diproses function

print(add_numbers(2, 3))

'''
If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function
'''
def f(x):
    x = x + 10
    print("Di dalam: ", x)

x = 5
print(x)

x = x + 7
print(x)

f(x)
print(x)