import unittest
from logika_tabel import hitung_metode_tabel


class TestMetodeTabel(unittest.TestCase):
    """Pengujian otomatis (unit testing) untuk fungsi di logika_tabel.py"""

    def test_panjang_langkah(self):
        # Memastikan perhitungan step size h = (b - a) / N sudah benar
        hasil = hitung_metode_tabel("x**2 - 4", 0, 4, 4)
        self.assertAlmostEqual(hasil["h"], 1.0)

    def test_jumlah_data_tabel(self):
        # Memastikan jumlah baris data tabel sesuai (N + 1 baris)
        hasil = hitung_metode_tabel("x**2 - 4", 0, 4, 4)
        self.assertEqual(len(hasil["data_tabel"]), 5)

    def test_nilai_fungsi(self):
        # Memastikan evaluasi f(x) pada titik x tertentu akurat
        hasil = hitung_metode_tabel("x**2 - 4", 0, 4, 4)
        baris_ke_2 = hasil["data_tabel"][2]
        self.assertEqual((baris_ke_2[0], baris_ke_2[1], baris_ke_2[2]), (2, 2.0, 0.0))

    def test_estimasi_akar(self):
        # Memastikan pencarian nilai akar dengan |f(x)| terkecil sudah pas
        hasil = hitung_metode_tabel("x**2 - 4", 0, 4, 4)
        self.assertAlmostEqual(hasil["akar_terbaik"][0], 2.0)

    def test_selang_akar(self):
        # Memastikan deteksi perubahan tanda f(x) (selang akar) berhasil
        hasil = hitung_metode_tabel("x**2 - 4", 0, 4, 4)
        self.assertIsNotNone(hasil["selang_akar"])

    def test_fungsi_kubik(self):
        # Pengujian fungsi polinomial derajat 3 (kubik)
        hasil = hitung_metode_tabel("x**3 - 8", 0, 4, 4)
        self.assertAlmostEqual(hasil["akar_terbaik"][0], 2.0)

    def test_fungsi_trigonometri(self):
        # Pengujian fungsi non-linear trigonometri sin(x)
        hasil = hitung_metode_tabel("sin(x)", 3, 4, 10)
        self.assertAlmostEqual(
            hasil["akar_terbaik"][0],
            3.14,
            delta=0.1
        )


if __name__ == "__main__":
    # Jalankan seluruh skenario pengujian otomatis
    unittest.main()