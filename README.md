# kalkulator-metode-tabel
Tugas UTS Praktikum Komputasi Numerik - Kelompok 9

## 1. Deskripsi Program

Kalkulator Metode Tabel merupakan aplikasi berbasis Python yang dirancang untuk mencari pendekatan akar suatu persamaan menggunakan Metode Tabel. Aplikasi ini menggunakan Tkinter sebagai antarmuka grafis (GUI) agar pengguna lebih mudah memasukkan fungsi matematika, menentukan interval, dan melihat hasil perhitungan.

Metode Tabel digunakan untuk memperkirakan lokasi akar persamaan dengan menghitung nilai fungsi pada sejumlah titik dalam interval tertentu.

## 2. Metode Perhitungan

Metode Tabel dilakukan dengan membagi interval [a, b] menjadi N bagian yang sama panjang.

Rumus panjang langkah:

**h = (b - a) / N**

Rumus titik perhitungan:

**xᵢ = a + i × h**

Keterangan:
- a = batas bawah interval
- b = batas atas interval
- N = jumlah pembagian interval
- h = panjang langkah
- i = indeks titik perhitungan, mulai dari 0 sampai N
- xᵢ = titik yang dihitung
- f(xᵢ) = nilai fungsi pada titik xᵢ

Nilai fungsi dihitung pada setiap titik untuk mencari kemungkinan lokasi akar. Jika nilai fungsi sama dengan nol, titik tersebut merupakan akar. Jika terdapat perubahan tanda antara dua titik berurutan dan fungsi kontinu, maka terdapat setidaknya satu akar di antara kedua titik tersebut.

## 3. Fitur yang Direncanakan

Aplikasi dikembangkan dengan fitur berikut:

- Input fungsi matematika f(x).
- Input batas bawah (a) dan batas atas (b).
- Input jumlah pembagian interval (N).
- Perhitungan nilai x dan f(x) menggunakan Metode Tabel.
- Tampilan hasil perhitungan dalam bentuk tabel.
- Penentuan interval yang berpotensi mengandung akar.
- Validasi input untuk mengurangi kesalahan masukan.

## 4. Teknologi yang Digunakan

- **Python:** Bahasa pemrograman utama.
- **Tkinter:** Pembuatan antarmuka aplikasi.
- **ttk.Treeview:** Menampilkan hasil perhitungan dalam bentuk tabel.
- **Git dan GitHub:** Pengelolaan kode dan kolaborasi kelompok.

## 5. Struktur Project

Struktur file yang direncanakan:

```text
kalkulator-metode-tabel/
├── main.py
├── logika_tabel.py
├── komponen_tabel.py
├── pengujian.py
├── README.md
└── .gitignore
```

Keterangan:
- `main.py` : Program utama dan integrasi GUI.
- `logika_tabel.py` : Perhitungan Metode Tabel.
- `komponen_tabel.py` : Tampilan tabel dan validasi input.
- `pengujian.py` : Pengujian fungsi perhitungan.
- `README.md` : Dokumentasi project.
- `.gitignore` : Mengabaikan file yang tidak perlu disimpan di GitHub.

## 6. Cara Menjalankan Program

Setelah seluruh modul selesai dan digabungkan, aplikasi dapat dijalankan dengan langkah berikut:

1. Pastikan Python sudah terinstal.
2. Clone repository melalui GitHub.
3. Buka folder project menggunakan VS Code.
4. Buka terminal pada folder project.
5. Jalankan perintah:

```bash
python main.py
```

6. Masukkan fungsi matematika dan parameter yang diperlukan.
7. Jalankan perhitungan melalui antarmuka aplikasi.
8. Periksa hasil perhitungan yang ditampilkan.

## 7. Rencana Pengujian

Pengujian dilakukan untuk memeriksa ketepatan hasil perhitungan Metode Tabel menggunakan beberapa fungsi matematika.

Contoh kasus pengujian:

| No. | Fungsi | Interval | N | Akar yang Diharapkan |
|---|---|---|---|---|
| 1 | f(x) = x² - 4 | [0, 4] | 8 | 2 |
| 2 | f(x) = x² - 9 | [0, 6] | 12 | 3 |
| 3 | f(x) = x³ - 8 | [0, 4] | 8 | 2 |

Selain itu, pengujian direncanakan untuk memeriksa penanganan input yang tidak valid, seperti jumlah pembagian N kurang dari atau sama dengan nol.

Pengujian akan diimplementasikan melalui file `pengujian.py` setelah modul perhitungan tersedia.

## 8. Anggota Kelompok

**Kelompok 9 - Praktikum Komputasi Numerik**

1. **Najahal Khaira** — Project Leader & Integrator GUI  
   Bertanggung jawab membuat repository, mengembangkan tampilan utama, dan menggabungkan seluruh modul program.

2. **Lukmanul Hakim Karva** — Backend / Logika Matematika  
   Bertanggung jawab membuat fungsi perhitungan Metode Tabel dan menghasilkan data perhitungan.

3. **Kyandaru Annisa Putri** — Frontend Tabel & Validasi Input  
   Bertanggung jawab membuat tampilan tabel hasil perhitungan dan validasi input pengguna.

4. **Shifa Azzuhra** — Testing & Dokumentasi  
   Bertanggung jawab melakukan pengujian fungsi matematika serta menyusun dokumentasi program dalam README.md.

## 9. Tujuan Project

Project ini dibuat untuk menerapkan materi Metode Tabel pada mata kuliah Praktikum Komputasi Numerik. Melalui aplikasi ini, proses pendekatan akar persamaan diharapkan menjadi lebih mudah dipahami karena hasil perhitungan dapat ditampilkan secara terstruktur.