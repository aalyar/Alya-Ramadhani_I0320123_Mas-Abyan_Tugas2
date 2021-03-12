#menghitung luas persegi panjang
print("Luas Persegi Panjang")
p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))

luas_persegi_panjang = p * l
print("luas persegi panjang:", luas_persegi_panjang)

print("---------------")

#menghitung luas lingkaran
print("Luas Lingkaran")
r = float(input("Masukkan jari-jari: "))
phi = 3.14

luas_lingkaran = 3.14 * (r ** 2)
print("luas lingkaran:", luas_lingkaran)

print("---------------")

#menghitung luas kubus
print("Luas Kubus")
r = float(input("Masukkan rusuk: "))

luas_kubus = 6 * r * r
print("luas kubus:", luas_kubus)

print("---------------")

#menghitung nilai suhu Celcius ke Fahrenheit
print("Konversi suhu (Celcius ke Fahrenheit)")

C = float(input("Masukkan suhu (Celcius): "))
F = (9/5 * C) + 32

print ("Celcius: ", C)
print("Fahrenheit: ", F)

print("---------------")

#menghitung nilai suhu Reamur ke Kelvin
print("Konversi suhu (Reamur ke Kelvin)")

R = float(input("Masukkan suhu (Reamur): "))
K = (5/4 * R) + 273

print("Reamur: ", R)
print("Kelvin: ", K)
