# Local and Global Variabel
print("\nLocal and Global Variabel")

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

###
x = 'awesome'
def func():
    print(x)
func()

'''
Variabel Global adalah variabel yang bisa diakses dari semua fungsi.
Variabel lokal hanya bisa diakses di dalam fungsi tempat ia berada saja.
Variabel Build-in adalah variabel yang sudah ada di dalam Python.

Urutan pengaksesan variabel (scope) dikenal dengan sebutan 
LGB (Local, Global, dan Build-in).
'''
# membuat variabel global
bahan = "Ayam"
masak = "Goreng"

def laper():
    # ini variabel lokal
    bahan = "Ikan"
    masak = "Bakar"
    # mengakses variabel lokal
    print("Bahan: ", bahan)
    print("Masak: ", masak)


# mengakses variabel global
print("Bahan: ", bahan)
print("Masak: ", masak)

# memanggil fungsi laper()
laper()

# Perintah global
x = 5
def f():
    global x # Perintah global membuat variabel x di dalam fungsi menjadi global
    x = 10
    print(x)

print(x) # x disini masih bernilai 5
f() # x disini bernilai 10 karena x sebelumnya sudah di proses di dalam fungsi
print(x) # x disini benilai 10 karena sudah ditimpa oleh x global di dalam fungsi

# Tanpa perintah global
x = 5
def f():
    x = 10
    print(x)

print(x)
f() # x disini tidak akan menimpa x sebelumnya karena bersifat local
print(x) # x disini masih 5 karena mengambil x yang diluar fungsi
