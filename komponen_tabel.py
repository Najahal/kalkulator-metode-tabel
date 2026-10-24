import tkinter as tk
from tkinter import ttk, messagebox

def validasi_input(a_str, b_str, n_str):
    """
    Validasi masukan dari user:
    - Memastikan a, b, dan N berupa angka yang valid.
    - Memastikan N > 0.
    """
    try:
        a = float(a_str)
        b = float(b_str)
        N = int(n_str)
        
        if N <= 0:
            messagebox.showerror("Error Validasi", "Jumlah sub-interval (N) harus lebih besar dari 0 (N > 0)!")
            return None
            
        return a, b, N
        
    except ValueError:
        messagebox.showerror("Error Validasi", "Batas bawah, batas atas, dan N harus berupa angka yang valid!")
        return None


class KomponenTabel:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        
        # Kolom tabel: Iterasi, Nilai x, dan Nilai f(x)
        self.columns = ("Iterasi", "x", "f(x)")

        # Konfigurasi Tema Cyberpunk / Style Tabel
        style = ttk.Style()
        style.theme_use("clam")
        
        # Style Bodi Tabel (Dark Midnight Violet)
        style.configure("Treeview",
                        background="#181a24",
                        foreground="#e2e8f0",
                        fieldbackground="#181a24",
                        rowheight=26,
                        font=("Segoe UI", 9))
        
        # Style Header Tabel (Deep Violet & Neon Cyan Text)
        style.configure("Treeview.Heading",
                        background="#2a1b40",
                        foreground="#00f5ff",
                        font=("Segoe UI", 10, "bold"),
                        relief="flat")
        style.map("Treeview.Heading", background=[('active', '#3d265c')])

        # Membuat Treeview (Tabel)
        self.tree = ttk.Treeview(self.frame, columns=self.columns, show="headings", height=10)
        
        # Konfigurasi Heading (Judul Kolom)
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130, anchor=tk.CENTER)
            
        # Membuat Scrollbar Vertikal
        self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        # Menata Layout dengan Pack
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def tampilkan_data(self, data_tabel):
        """
        Memasukkan list data hasil perhitungan ke dalam ttk.Treeview.
        Format data_tabel dari logika_tabel.py: [(i, x_i, fx_i), ...]
        """
        # Bersihkan data lama terlebih dahulu setiap kali tombol hitung diklik
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Masukkan data baru baris per baris
        for row in data_tabel:
            iterasi, x_val, fx_val = row
            # Format angka agar rapi di tabel (misal 5 angka di belakang koma)
            self.tree.insert("", tk.END, values=(iterasi, f"{x_val:.5f}", f"{fx_val:.5f}"))