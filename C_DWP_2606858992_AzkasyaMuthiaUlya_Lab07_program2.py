class BerkasProyek:
    def __init__(self, nama, jenis, ukuran):
        # TODO 1:
        # Simpan nama, jenis, dan ukuran sebagai atribut objek.
        self.nama = nama
        self.jenis = jenis
        self.ukuran = ukuran

    def hitung_ukuran_mb(self):
        # TODO 2:
        # Hitung dan kembalikan ukuran berkas dalam MB.
        return self.ukuran / 1024.0

    def tampilkan_info(self):
        # TODO 3:
        # Cetak seluruh informasi berkas proyek sesuai format.
        ukuran_mb = self.hitung_ukuran_mb()
        print("=== RINCIAN BERKAS PROYEK ===")
        print(f"Nama berkas: {self.nama}")
        print(f"Jenis berkas: {self.jenis}")
        print(f"Ukuran berkas: {self.ukuran} KB")
        print(f"Ukuran berkas: {ukuran_mb:.2f} MB")



print("=== INFORMASI BERKAS PROYEK ===")
nama = input("Masukkan nama berkas: ")
jenis = input("Masukkan jenis berkas (P/D): ")
ukuran = int(input("Masukkan ukuran berkas (KB): "))

# TODO 4:
# Buat objek BerkasProyek dan tampilkan informasinya.
berkas_proyek = BerkasProyek(nama, jenis, ukuran)
berkas_proyek.tampilkan_info()