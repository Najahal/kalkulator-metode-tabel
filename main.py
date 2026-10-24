import tkinter as tk
from tkinter import messagebox
from logika_tabel import hitung_metode_tabel
from komponen_tabel import KomponenTabel, validasi_input


class AplikasiKalkulatorTabel:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Metode Tabel")
        self.root.geometry("580x650")
        self.root.resizable(False, False)

        # Palet Warna Cyberpunk Neon
        self.BG_MAIN = "#0f111a"        # Dark Midnight
        self.BG_CARD = "#181a24"        # Dark Violet Card
        self.COLOR_CYAN = "#00f5ff"      # Cyan Neon
        self.COLOR_PINK = "#ff007f"      # Pink Magenta
        self.COLOR_YELLOW = "#ffe600"    # Kuning Electric
        self.TEXT_LIGHT = "#cbd5e1"     # Light Slate Teks
        self.ENTRY_BG = "#232635"       # Input Box
        
        self.root.configure(bg=self.BG_MAIN)

        # Frame Input Data
        self.frame_input = tk.Frame(self.root, bg=self.BG_CARD, padx=15, pady=12, highlightthickness=1, highlightbackground="#312e81")
        self.frame_input.pack(side=tk.TOP, fill="x", padx=15, pady=10)

        # Input Fungsi f(x)
        tk.Label(self.frame_input, text="Fungsi f(x):", font=("Segoe UI", 10, "bold"), bg=self.BG_CARD, fg=self.COLOR_CYAN).grid(row=0, column=0, sticky="w", pady=4)
        self.entry_fungsi = tk.Entry(self.frame_input, width=30, font=("Segoe UI", 10), bg=self.ENTRY_BG, fg="white", insertbackground="white", relief="flat")
        self.entry_fungsi.insert(0, "x**3 - x - 7")
        self.entry_fungsi.grid(row=0, column=1, pady=4, ipady=3)

        # Input Batas Bawah (b)
        tk.Label(self.frame_input, text="Batas Bawah (b):", font=("Segoe UI", 10), bg=self.BG_CARD, fg=self.TEXT_LIGHT).grid(row=1, column=0, sticky="w", pady=4)
        self.entry_b = tk.Entry(self.frame_input, width=30, font=("Segoe UI", 10), bg=self.ENTRY_BG, fg="white", insertbackground="white", relief="flat")
        self.entry_b.insert(0, "2")
        self.entry_b.grid(row=1, column=1, pady=4, ipady=3)

        # Input Batas Atas (a)
        tk.Label(self.frame_input, text="Batas Atas (a):", font=("Segoe UI", 10), bg=self.BG_CARD, fg=self.TEXT_LIGHT).grid(row=2, column=0, sticky="w", pady=4)
        self.entry_a = tk.Entry(self.frame_input, width=30, font=("Segoe UI", 10), bg=self.ENTRY_BG, fg="white", insertbackground="white", relief="flat")
        self.entry_a.insert(0, "3")
        self.entry_a.grid(row=2, column=1, pady=4, ipady=3)

        # Input Jumlah Sub-interval (N)
        tk.Label(self.frame_input, text="Jumlah Sub-interval (N):", font=("Segoe UI", 10), bg=self.BG_CARD, fg=self.TEXT_LIGHT).grid(row=3, column=0, sticky="w", pady=4)
        self.entry_n = tk.Entry(self.frame_input, width=30, font=("Segoe UI", 10), bg=self.ENTRY_BG, fg="white", insertbackground="white", relief="flat")
        self.entry_n.insert(0, "10")
        self.entry_n.grid(row=3, column=1, pady=4, ipady=3)

        # Tombol Hitung Akar
        self.btn_hitung = tk.Button(
            self.frame_input,
            text="⚡ HITUNG AKAR ⚡",
            bg=self.COLOR_PINK,
            activebackground="#d10068",
            fg="white",
            activeforeground="white",
            font=("Segoe UI", 10, "bold"),
            padx=15,
            pady=6,
            bd=0,
            cursor="hand2",
            command=self.proses_hitung
        )
        self.btn_hitung.grid(row=4, column=0, columnspan=2, pady=10)

        # Frame Container Tabel (Komponen dari Kyandaru)
        self.frame_tabel = tk.Frame(self.root, bg=self.BG_MAIN, padx=15)
        self.frame_tabel.pack(side=tk.TOP, fill="both", expand=True)

        # Menginisialisasi komponen tabel
        self.tabel = KomponenTabel(self.frame_tabel)

        # Frame Ringkasan Hasil
        self.frame_hasil = tk.Frame(self.root, bg=self.BG_CARD, padx=15, pady=12, highlightthickness=1, highlightbackground="#312e81")
        self.frame_hasil.pack(side=tk.BOTTOM, fill="x", padx=15, pady=10)

        self.label_hasil = tk.Label(
            self.frame_hasil, 
            text="Masukkan data lalu klik HITUNG AKAR", 
            font=("Segoe UI", 10, "bold"), 
            bg=self.BG_CARD,
            fg=self.COLOR_YELLOW,
            justify="center"
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

            self.label_hasil.config(text=teks_hasil, fg=self.COLOR_YELLOW)

        except Exception as e:
            messagebox.showerror("Error Matematika", f"Gagal mengevaluasi fungsi f(x):\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiKalkulatorTabel(root)
    root.mainloop()