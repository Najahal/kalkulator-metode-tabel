import tkinter as tk
from tkinter import messagebox
from logika_tabel import hitung_metode_tabel
from komponen_tabel import KomponenTabel, validasi_input


class AplikasiKalkulatorTabel:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Metode Tabel - Komputasi Numerik")
        self.root.geometry("580x600")
        self.root.resizable(False, False)

        # Frame Input Data
        self.frame_input = tk.Frame(self.root, padx=15, pady=15)
        self.frame_input.pack(fill="x")

        # Input Fungsi f(x)
        tk.Label(self.frame_input, text="Fungsi f(x):", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.entry_fungsi = tk.Entry(self.frame_input, width=32, font=("Arial", 10))
        self.entry_fungsi.insert(0, "x**3 - x - 1")
        self.entry_fungsi.grid(row=0, column=1, pady=5)

        # Input Batas Bawah (b)
        tk.Label(self.frame_input, text="Batas Bawah (b):", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.entry_b = tk.Entry(self.frame_input, width=32, font=("Arial", 10))
        self.entry_b.insert(0, "1")
        self.entry_b.grid(row=1, column=1, pady=5)

        # Input Batas Atas (a)
        tk.Label(self.frame_input, text="Batas Atas (a):", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.entry_a = tk.Entry(self.frame_input, width=32, font=("Arial", 10))
        self.entry_a.insert(0, "2")
        self.entry_a.grid(row=2, column=1, pady=5)

        # Input Jumlah Sub-interval (N)
        tk.Label(self.frame_input, text="Jumlah Sub-interval (N):", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
        self.entry_n = tk.Entry(self.frame_input, width=32, font=("Arial", 10))
        self.entry_n.insert(0, "10")
        self.entry_n.grid(row=3, column=1, pady=5)

        # Tombol Hitung Akar
        self.btn_hitung = tk.Button(
            self.frame_input,
            text="Hitung Akar",
            bg="#2b5c8f",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5,
            command=self.proses_hitung
        )
        self.btn_hitung.grid(row=4, column=0, columnspan=2, pady=12)

        # Frame Container Tabel (Komponen dari Kyandaru)
        self.frame_tabel = tk.Frame(self.root, padx=15)
        self.frame_tabel.pack(fill="both", expand=True)

        # Menginisialisasi komponen tabel
        self.tabel = KomponenTabel(self.frame_tabel)

        # Frame Ringkasan Hasil (Area output akhir)
        self.frame_hasil = tk.Frame(self.root, padx=15, pady=15)
        self.frame_hasil.pack(fill="x")

        self.label_hasil = tk.Label(
            self.frame_hasil, 
            text="Masukkan data lalu klik Hitung Akar", 
            font=("Arial", 10, "bold"), 
            fg="#444444"
        )
        self.label_hasil.pack()

    def proses_hitung(self):
        fungsi_str = self.entry_fungsi.get().strip()
        b_str = self.entry_b.get().strip()
        a_str = self.entry_a.get().strip()
        n_str = self.entry_n.get().strip()

        if not fungsi_str:
            messagebox.showerror("Error Input", "Fungsi f(x) tidak boleh kosong!")
            return

        # Validasi input dari komponen_tabel.py
        valid_data = validasi_input(a_str, b_str, n_str)
        if valid_data is None:
            return

        a_val, b_val, n_val = valid_data

        try:
            # Perhitungan dari logika_tabel.py
            hasil = hitung_metode_tabel(fungsi_str, b_val, a_val, n_val)

            # Render data ke tabel Treeview
            self.tabel.tampilkan_data(hasil["data_tabel"])

            # Tampilkan ringkasan hasil
            akar_x, fx = hasil["akar_terbaik"]
            teks_hasil = f"Estimasi Akar Terbaik: x = {akar_x:.5f} | f(x) = {fx:.5f}"

            if hasil["selang_akar"]:
                (x1, _), (x2, _) = hasil["selang_akar"]
                teks_hasil += f"\nAkar berada di selang [{x1:.5f}, {x2:.5f}]"
            else:
                teks_hasil += "\n(Tidak ada perubahan tanda f(x) / selang akar tidak ditemukan)"

            self.label_hasil.config(text=teks_hasil, fg="#2b5c8f")

        except Exception as e:
            messagebox.showerror("Error Matematika", f"Gagal mengevaluasi fungsi f(x):\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiKalkulatorTabel(root)
    root.mainloop()