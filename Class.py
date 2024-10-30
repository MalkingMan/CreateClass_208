class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi Panjang(Panjang: {self.panjang}, Lebar: {self.lebar})"

# Input dari pengguna
try:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))

    # Membuat objek PersegiPanjang
    persegi = PersegiPanjang(panjang, lebar)

    # Menampilkan hasil
    print(persegi)
    print(f"Keliling: {persegi.hitung_keliling()}")
    print(f"Luas: {persegi.hitung_luas()}")

except ValueError:
    print("Masukkan angka yang valid.")
