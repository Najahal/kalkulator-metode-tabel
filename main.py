import tkinter as tk
from tkinter import messagebox

# Tunggu file dari yang lain, nanti tinggal hapus tanda '#' di bawah:
# from logika_tabel import hitung_metode_tabel
# from komponen_tabel import buat_tabel, validasi_input


class AplikasiKalkulatorTabel:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Metode Tabel - Komputasi Numerik")
        self.root.geometry("580x560")
        self.root.resizable(False, False)

        # 1. Frame Input Data
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

        # 2. Frame Container Tabel (Area tugas Kyandaru)
        self.frame_tabel = tk.Frame(self.root, padx=15)
        self.frame_tabel.pack(fill="both", expand=True)

        self.label_placeholder = tk.Label(
            self.frame_tabel, 
            text="[ Area Tabel Hasil Perhitungan ]", 
            font=("Arial", 10, "italic"), 
            fg="gray"
        )
        self.label_placeholder.pack(expand=True)

        # 3. Frame Ringkasan Hasil (Area output akhir)
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
        # Nanti diisi logika integrasi saat file anggota lain sudah selesai
        messagebox.showinfo("Status GUI", "Layout GUI Utama Berhasil Dimuat!")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiKalkulatorTabel(root)
    root.mainloop()
