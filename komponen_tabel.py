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
        
        # Kolom tabel disesuaikan dengan output logika_tabel.py yang baru
        self.columns = ("Iterasi", "xi", "f(xi)", "f(xi+1)", "|f(xi).f(xi+1)|")

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
                        font=("Segoe UI", 9, "bold"),
                        relief="flat")
        style.map("Treeview.Heading", background=[('active', '#3d265c')])

        # Membuat Treeview (Tabel)
        self.tree = ttk.Treeview(self.frame, columns=self.columns, show="headings", height=10)
        
        # Konfigurasi Heading & Lebar Kolom
        column_widths = {
            "Iterasi": 40,
            "xi": 100,
            "f(xi)": 120,
            "f(xi+1)": 120,
            "|f(xi).f(xi+1)|": 120
        }
        
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths.get(col, 100), anchor=tk.CENTER)
            
        # Membuat Scrollbar Vertikal
        self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        # Menata Layout dengan Pack
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def tampilkan_data(self, data_tabel):
        """
        Memasukkan list data hasil perhitungan ke dalam ttk.Treeview.
        Format data_tabel baru: [(idx, x_val, fx_val, fx_next, mutlak_perkalian), ...]
        """
        # Bersihkan data lama terlebih dahulu setiap kali tombol hitung diklik
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Masukkan data baru baris per baris
        for row in data_tabel:
            iterasi, x_val, fx_val, fx_next, mutlak_perkalian = row
            
            # Format tampilan nilai (handle None jika di baris terakhir)
            str_fx_next = f"{fx_next:.5f}" if fx_next is not None else "-"
            str_mutlak = f"{mutlak_perkalian:.5f}" if fx_next is not None else "-"
            
            self.tree.insert("", tk.END, values=(
                iterasi, 
                f"{x_val:.5f}", 
                f"{fx_val:.5f}", 
                str_fx_next, 
                str_mutlak
            ))