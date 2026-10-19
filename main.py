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
