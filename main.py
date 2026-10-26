import tkinter as tk
from tkinter import messagebox
from logika_tabel import hitung_metode_tabel
from komponen_tabel import KomponenTabel, validasi_input


class AplikasiKalkulatorTabel:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Metode Tabel")
        self.root.geometry("980x620")
        self.root.resizable(True, True)

        # Palet Warna Cyberpunk Neon
        self.BG_MAIN = "#0f111a"        # Dark Midnight
        self.BG_CARD = "#181a24"        # Dark Violet Card
        self.COLOR_CYAN = "#00f5ff"      # Cyan Neon
        self.COLOR_PINK = "#ff007f"      # Pink Magenta
        self.COLOR_YELLOW = "#ffe600"    # Kuning Electric
        self.TEXT_LIGHT = "#cbd5e1"     # Light Slate Teks
        self.ENTRY_BG = "#232635"       # Input Box
        
        self.root.configure(bg=self.BG_MAIN)

        # Container Utama (Membagi Kolom Kiri dan Kanan)
        self.main_container = tk.Frame(self.root, bg=self.BG_MAIN)
        self.main_container.pack(fill="both", expand=True, padx=15, pady=15)

        # Pembagian sisi kiri berisi Input & Kesimpulan
        self.frame_kiri = tk.Frame(self.main_container, bg=self.BG_MAIN, width=380)
        self.frame_kiri.pack(side=tk.LEFT, fill="both", padx=(0, 10))
        self.frame_kiri.pack_propagate(False)

        # Frame Input Data
        self.frame_input = tk.Frame(self.frame_kiri, bg=self.BG_CARD, padx=15, pady=12, highlightthickness=1, highlightbackground="#312e81")
        self.frame_input.pack(side=tk.TOP, fill="x", pady=(0, 10))

        # Input Fungsi f(x)
        tk.Label(self.frame_input, text="Fungsi f(x):", font=("Segoe UI", 10, "bold"), bg=self.BG_CARD, fg=self.COLOR_CYAN).grid(row=0, column=0, sticky="w", pady=4)
        self.entry_fungsi = tk.Entry(self.frame_input, width=30, font=("Segoe UI", 10), bg=self.ENTRY_BG, fg="white", insertbackground="white", relief="flat")
        self.entry_fungsi.insert(0, "x**2+exp(-x)-2")
        self.entry_fungsi.grid(row=0, column=1, pady=4, ipady=3)

        # Input Batas Atas (a)
        tk.Label(self.frame_input, text="Batas Atas (a):", font=("Segoe UI", 10), bg=self.BG_CARD, fg=self.TEXT_LIGHT).grid(row=1, column=0, sticky="w", pady=4)
        self.entry_a = tk.Entry(self.frame_input, width=30, font=("Segoe UI", 10), bg=self.ENTRY_BG, fg="white", insertbackground="white", relief="flat")
        self.entry_a.insert(0, "1")
        self.entry_a.grid(row=1, column=1, pady=4, ipady=3)

        # Input Batas Bawah (b)
        tk.Label(self.frame_input, text="Batas Bawah (b):", font=("Segoe UI", 10), bg=self.BG_CARD, fg=self.TEXT_LIGHT).grid(row=2, column=0, sticky="w", pady=4)
        self.entry_b = tk.Entry(self.frame_input, width=30, font=("Segoe UI", 10), bg=self.ENTRY_BG, fg="white", insertbackground="white", relief="flat")
        self.entry_b.insert(0, "4")
        self.entry_b.grid(row=2, column=1, pady=4, ipady=3)

        # Input Jumlah Sub-interval (N)
        tk.Label(self.frame_input, text="Jumlah Sub-interval (N):", font=("Segoe UI", 10), bg=self.BG_CARD, fg=self.TEXT_LIGHT).grid(row=3, column=0, sticky="w", pady=4)
        self.entry_n = tk.Entry(self.frame_input, width=30, font=("Segoe UI", 10), bg=self.ENTRY_BG, fg="white", insertbackground="white", relief="flat")
        self.entry_n.insert(0, "10")
        self.entry_n.grid(row=3, column=1, pady=4, ipady=3)

        # Label untuk menampilkan nilai h
        tk.Label(self.frame_input, text="h:", font=("Segoe UI", 10), bg=self.BG_CARD, fg=self.TEXT_LIGHT).grid(row=4, column=0, sticky="w", pady=4)
        self.label_h = tk.Label(self.frame_input, text="-", font=("Segoe UI", 10, "bold"), bg=self.BG_CARD, fg=self.COLOR_YELLOW)
        self.label_h.grid(row=4, column=1, sticky="w", pady=4)

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
        self.btn_hitung.grid(row=5, column=0, columnspan=2, pady=10, sticky="we")

        ## Frame Ringkasan Hasil
        self.frame_hasil = tk.Frame(self.frame_kiri, bg=self.BG_CARD, padx=15, pady=12, highlightthickness=1, highlightbackground="#312e81")
        self.frame_hasil.pack(side=tk.TOP, fill="both", expand=True)

        self.label_hasil = tk.Label(
            self.frame_hasil, 
            text="Masukkan data lalu klik HITUNG AKAR", 
            font=("Segoe UI", 9, "bold"), 
            bg=self.BG_CARD,
            fg=self.COLOR_YELLOW,
            justify="left",
            anchor="nw",
            wraplength=340
        )
        self.label_hasil.pack(fill="both", expand=True)

        # Pembagian Sisi Kanan untuk tabel hasil
        self.frame_tabel = tk.Frame(self.main_container, bg=self.BG_MAIN)
        self.frame_tabel.pack(side=tk.RIGHT, fill="both", expand=True)

        # Inisialisasi komponen tabel
        self.tabel = KomponenTabel(self.frame_tabel)

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

            # Update nilai h di frame atas
            self.label_h.config(text=f"{hasil['h']:.5f}")

            # Tampilkan ringkasan hasil
            akar_x, fx = hasil["akar_terbaik"]
            teks_hasil = f"Estimasi Akar Terbaik: x = {akar_x:.5f} | f(x) = {fx:.5f}"

            # Kesimpulan sesuai Algoritma materi
            teks_kesimpulan = ""
            akar_ditemukan = False

            # Cek Kondisi: Bila f(xi) = 0 maka xi adalah penyelesaian
            for row in hasil["data_tabel"]:
                idx, xi, fxi, fxi_plus_1, mutlak = row
                if abs(fxi) < 1e-9:  # Mendekati 0
                    teks_kesimpulan = f"Kesimpulan:\nKarena f(xi) = 0 pada f({xi:.5f}), maka x = {xi:.5f} adalah penyelesaian\n(Penyelesaian ditemukan pada iterasi ke-{idx})"
                    akar_ditemukan = True
                    break

            # Cek Kondisi: Bila f(xi) . f(xi+1) < 0
            if not akar_ditemukan and hasil["selang_akar"]:
                (xi, fxi), (xi_plus_1, fxi_plus_1) = hasil["selang_akar"]
                iterasi_ke = hasil.get("iterasi_akar", "-")
                teks_kesimpulan = f"Kesimpulan:\nKarena f(xi) . f(xi+1) < 0 antara x={xi:.5f} dan x={xi_plus_1:.5f}:\n"
                
                # bila |f(xi)| < |f(xi+1)| maka xi adalah penyelesaian
                if abs(fxi) < abs(fxi_plus_1):
                    teks_kesimpulan += f"Karena |f(xi)| < |f(xi+1)| (|{fxi:.5f}| < |{fxi_plus_1:.5f}|), maka x = {xi:.5f} adalah penyelesaian\n(Penyelesaian ditemukan pada iterasi ke-{iterasi_ke})"
                # bila tidak maka xi+1 adalah penyelesaian
                else:
                    teks_kesimpulan += f"Karena |f(xi)| > |f(xi+1)| (|{fxi:.5f}| > |{fxi_plus_1:.5f}|), maka x = {xi_plus_1:.5f} adalah penyelesaian\n\n(Penyelesaian ditemukan pada iterasi ke-{iterasi_ke + 1})"

            elif not akar_ditemukan:
                teks_kesimpulan = "Kesimpulan:\nTidak ada penyelesaian (akar) yang ditemukan pada rentang ini."

            # Tampilkan teks kesimpulan di frame bawah
            self.label_hasil.config(text=teks_kesimpulan, fg=self.COLOR_YELLOW)

        except Exception as e:
            messagebox.showerror("Error Matematika", f"Gagal mengevaluasi fungsi f(x):\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiKalkulatorTabel(root)
    root.mainloop()