def urutan_pasang(lib):
    """
    Mengembalikan list library yang perlu dipasang agar lib
    dapat dipasang, sesuai urutan pemasangannya.

    Variabel yang dapat digunakan:
    - terpasang  : list nama library yang sudah terpasang
    - dependensi : dictionary {nama library: list dependensinya}
                   Library tanpa dependensi tidak ada di dictionary ini.
    """
    # TODO 1:
    # Tangani kondisi ketika lib sudah terpasang.
    if lib in terpasang:
        return []

    # TODO 2:
    # Kumpulkan urutan pemasangan dari setiap dependensi lib,
    # sesuai urutan dependensi yang tertulis.
    hasil = []
    for d in dependensi.get(lib, []):
        hasil.extand(urutan_pasang(d))

    # TODO 3:
    # Tambahkan lib sendiri ke urutan pemasangan.
    # Ingat, lib baru boleh dipasang setelah semua dependensinya terpasang.
    hasil.append(lib)

    # TODO 4:
    # Kembalikan urutan pemasangan yang sudah lengkap.
    return hasil


# ===== Program utama =====
target = input()
terpasang = input().split()
dependensi = {}

# TODO 5:
# Baca M, lalu simpan M baris data dependensi ke dictionary dependensi.
# Kata pertama tiap baris menjadi key, sisanya menjadi value.
m = int(input())
for _ in range(m):
    baris = input().split()
    if baris:
        lib_utama = baris[0]
        daftar_dep = baris[1:]
        dependensi[lib_utama] = daftar_dep



# TODO 6:
# Panggil urutan_pasang(target), buang library yang muncul lebih dari sekali
# tanpa mengubah urutan, lalu cetak sesuai format output.
hasil = urutan_pasang(target)
hasil = []
for item in daftar_mentah:
    if item not in hasil:
        hasil.append(item)

print(f"Urutan pemasangan: {', '.join(hasil)}")