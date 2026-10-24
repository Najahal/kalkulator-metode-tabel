import unittest
import importlib.util
from pathlib import Path

# Mengambil fungsi dari file logika-tabel.py
lokasi_file = Path(__file__).with_name("logika-tabel.py")
spec = importlib.util.spec_from_file_location("logika_tabel", lokasi_file)
modul = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modul)

hitung_metode_tabel = modul.hitung_metode_tabel


class TestMetodeTabel(unittest.TestCase):

    def test_panjang_langkah(self):
        hasil = hitung_metode_tabel("x**2 - 4", 0, 4, 4)
        self.assertAlmostEqual(hasil["h"], 1.0)

    def test_jumlah_data_tabel(self):
        hasil = hitung_metode_tabel("x**2 - 4", 0, 4, 4)
        self.assertEqual(len(hasil["data_tabel"]), 5)

    def test_nilai_fungsi(self):
        hasil = hitung_metode_tabel("x**2 - 4", 0, 4, 4)
        self.assertEqual(hasil["data_tabel"][2], (2, 2.0, 0.0))

    def test_estimasi_akar(self):
        hasil = hitung_metode_tabel("x**2 - 4", 0, 4, 4)
        self.assertAlmostEqual(hasil["akar_terbaik"][0], 2.0)

    def test_selang_akar(self):
        hasil = hitung_metode_tabel("x**2 - 4", 0, 4, 4)
        self.assertIsNotNone(hasil["selang_akar"])

    def test_fungsi_kubik(self):
        hasil = hitung_metode_tabel("x**3 - 8", 0, 4, 4)
        self.assertAlmostEqual(hasil["akar_terbaik"][0], 2.0)

    def test_fungsi_trigonometri(self):
        hasil = hitung_metode_tabel("sin(x)", 3, 4, 10)
        self.assertAlmostEqual(
            hasil["akar_terbaik"][0],
            3.14,
            delta=0.1
        )


if __name__ == "__main__":
    unittest.main()