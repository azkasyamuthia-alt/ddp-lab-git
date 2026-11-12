def hitung_cara(indeks, jenis_berkas):
    # TODO 1:
    # Tangani kondisi ketika seluruh berkas telah berhasil diunggah.
    if indeks >= len(jenis_berkas):
        return 1

    # TODO 2:
    # Hitung banyak cara jika berkas saat ini diunggah sendirian.
    jumlah_cara = hitung_cara(indeks + 1, jenis_berkas)

    # TODO 3:
    # Jika memungkinkan, tambahkan kemungkinan mengunggah
    # dua berkas bersebelahan dengan jenis yang sama.
    if indeks + 1 < len(jenis_berkas) and jenis_berkas[indeks] == jenis_berkas[indeks + 1]:
        jumlah_cara += hitung_cara(indeks + 2, jenis_berkas)

    # TODO 4:
    # Kembalikan jumlah seluruh cara yang valid.
    return jumlah_cara


print("=== SISTEM PENGUNGGAHAN BERKAS PROYEK ===")
n = int(input("Masukkan jumlah berkas: "))
jenis_berkas = input("Masukkan jenis berkas: ")

hasil = hitung_cara(0, jenis_berkas)

print("\n=== HASIL ANALISIS ===")
print(
    f"Untuk {n} berkas proyek, terdapat {hasil} "
    "cara pengunggahan yang valid."
)