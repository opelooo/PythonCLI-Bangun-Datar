'''
Mathys Jorge Alberino Seilatu- 205314174
'''
import math

#menu pertama untuk pilih bangun mana yang mau dicari keliling atau luasnya
pilih = input("""
Pilih Menu:
a.	Segitiga Sama Kaki
b.	Persegi Panjang
c.	Lingkaran
d.	Jajar Genjang
e.	Trapesium Sama Kaki
>""")

pilih1 = ""

#function Keliling bangun
def KelilingSSK(): 
    a = int(input("Alas: ")) 
    k = int(input("Panjang Kaki: "))
    return "Keliling Segitiga: {}".format(a+k)
def KelilingPP(): 
    p = int(input("Panjang: "))
    l = int(input("Lebar: "))
    return "Keliling Persegi Panjang: {}".format(2(p+l))
def KelilingL(): 
    r = int(input("Jari-Jari: "))
    return "Keliling Lingkaran: {}".format(2*math.pi*r)
def KelilingJG(): 
    s1 = int(input("Sisi 1: ")) 
    s2 = int(input("Sisi 2: "))
    return "Keliling Jajar Genjang: {}".format(2*(s1+s2))
def KelilingT(): 
    s1 = int(input("Sisi 1: ")) 
    s2 = int(input("Sisis 2: "))
    return "Keliling Trapesium: {}".format(2*(s1+s2))

#function Luas bangun
def LuasSSK(): 
    a = int(input("Alas: ")) 
    t = int(input("Tinggi: "))
    return "Luas Segitiga: {}".format(0.5*a*t)
def LuasPP(): 
    p = int(input("Panjang: ")) 
    l = int(input("Lebar: "))
    return "Luas Persegi Panjang: {}".format(p*l)
def LuasL(): 
    r = int(input("Jari-Jari: "))
    return "Luas Lingkaran: {}".format(math.pi*r*r)
def LuasJG(): 
    a = int(input("Alas: "))
    t = int(input("Tinggi: "))
    return "Luas Jajar Genjang: {}".format(a*t)
def LuasT(): 
    s1 = int(input("Sisi 1: "))
    s2 = int(input("Sisi 2: "))
    t = int(input("Tinggi: "))
    return "Luas Trapesium: {}".format(((s1+s2)*t)/2)

def menu(pilih):
    bisa_pilih = "ABCDE"
    bangun = ["Segitiga Sama Kaki", "Persegi Panjang",
              "Lingkaran", "Jajar Genjang", "Trapesium Sama Kaki"]
    Int = 0
    for x in bisa_pilih:
        if pilih == x:
            #menu kedua untuk pilih luas atau keliling bangun
            pilih1 = input("Pilih Menu:\n1.  Luas {}\n2.  Keliling {}\n>".format(bangun[Int], bangun[Int]))
        Int += 1
    #saya gamau buat banyak if jadi pake ini aja
    #ganti dari if statement adalah tipe data dictionary yang nantinya dieksekusi di print
    syarat = {(pilih1 == "1" and pilih == "A") : LuasSSK, (pilih1 == "1" and pilih == "B") : LuasPP, 
              (pilih1 == "1" and pilih == "C") : LuasL, (pilih1 == "1" and pilih == "D") : LuasJG, 
              (pilih1 == "1" and pilih == "E") : LuasT, (pilih1 == "2" and pilih == "A") : KelilingSSK, 
              (pilih1 == "2" and pilih == "B") : KelilingPP, (pilih1 == "2" and pilih == "C") : KelilingL, 
              (pilih1 == "2" and pilih == "D") : KelilingJG, (pilih1 == "2" and pilih == "E") : KelilingT}
    #memanggil dict yang bernilai True lalu mengeksekusinya di sini bukan di variable syarat
    print(syarat[True]())
        

menu(pilih)
