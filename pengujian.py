import unittest


class TestMetodeTabel(unittest.TestCase):

    def test_fungsi_kuadrat_pertama(self):
        x = 2
        hasil = x**2 - 4
        self.assertEqual(hasil, 0)

    def test_fungsi_kuadrat_kedua(self):
        x = 3
        hasil = x**2 - 9
        self.assertEqual(hasil, 0)

    def test_fungsi_kubik(self):
        x = 2
        hasil = x**3 - 8
        self.assertEqual(hasil, 0)


if __name__ == "__main__":
    unittest.main()