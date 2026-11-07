import random

print("=== Game Tebak Angka ===")
print("Saya memilih angka antara 1 sampai 100. Coba tebak!")

angka_rahasia = random.randint(1, 100)
percobaan = 0
maksimal = 7

while percobaan < maksimal:
    tebakan = int(input(f"\nPercobaan ke-{percobaan + 1} dari {maksimal}. Tebakan Anda: "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print(f"Benar! Angkanya {angka_rahasia}. Anda berhasil dalam {percobaan} percobaan.")
        break
else:
    print(f"\nKesempatan habis. Angka rahasianya adalah {angka_rahasia}.")