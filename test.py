print("Hello World")
# Program sederhana: perkenalan dan kalkulator

print("=== Program Perkenalan ===")

nama = input("Siapa nama Anda? ")
umur = int(input("Berapa umur Anda? "))

print(f"Halo, {nama}! Tahun depan umur Anda {umur + 1} tahun.")

print("\n=== Kalkulator Sederhana ===")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print(f"Penjumlahan : {angka1} + {angka2} = {angka1 + angka2}")
print(f"Pengurangan : {angka1} - {angka2} = {angka1 - angka2}")
print(f"Perkalian   : {angka1} x {angka2} = {angka1 * angka2}")

if angka2 != 0:
    print(f"Pembagian   : {angka1} / {angka2} = {angka1 / angka2}")
else:
    print("Pembagian   : tidak bisa dibagi dengan nol")