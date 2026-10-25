import math

def hitung_metode_tabel(fungsi_str, val1, val2, n_subinterval):
    """
    Menghitung pencarian akar fungsi menggunakan Metode Tabel.
    Memastikan perhitungan selalu berjalan menurun dari nilai maksimum ke minimum
    agar urutan iterasinya sama persis seperti di spreadsheet Excel.
    """
    # Selalu ambil nilai terbesar sebagai awal (a) dan terkecil sebagai akhir (b)
    a = max(float(val1), float(val2))
    b = min(float(val1), float(val2))
    
    # Step size h berjalan menurun dari a ke b: h = (b - a) / N (hasilnya negatif)
    h = (b - a) / n_subinterval
    
    # Menyiapkan namespace fungsi matematika dasar
    math_env = {
        'x': 0,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'exp': math.exp,
        'sqrt': math.sqrt,
        'log': math.log,
        'pi': math.pi,
        'e': math.e
    }
    
    def evaluasi_fungsi(x_val):
        math_env['x'] = x_val
        return eval(fungsi_str, {"__builtins__": None}, math_env)

    # 1. Menghitung titik x_i dan f(x_i) secara menurun dari nilai terbesar ke terkecil
    raw_data = []
    for i in range(n_subinterval + 1):
        x_i = a + i * h
        fx_i = evaluasi_fungsi(x_i)
        raw_data.append((i, x_i, fx_i))
        
    # 2. Menyusun data tabel lengkap
    data_tabel = []
    selang_akar = None
    akar_terbaik = None
    min_fx = float('inf')
    
    for i in range(len(raw_data)):
        idx, x_val, fx_val = raw_data[i]
        
        # Cek nilai |f(x)| terkecil untuk estimasi akar terbaik
        if abs(fx_val) < min_fx:
            min_fx = abs(fx_val)
            akar_terbaik = (x_val, fx_val)
            
        # Ambil nilai berikutnya f(x_{i+1}) jika ada
        if i < len(raw_data) - 1:
            _, x_next, fx_next = raw_data[i + 1]
            mutlak_perkalian = abs(fx_val * fx_next)
            
            # Cek perubahan tanda f(x_i) * f(x_next) <= 0
            if fx_val * fx_next <= 0:
                selang_akar = ((x_val, fx_val), (x_next, fx_next))
                iterasi_akar = idx + 1
        else:
            fx_next = None
            mutlak_perkalian = 0.0
            
        data_tabel.append((idx, x_val, fx_val, fx_next, mutlak_perkalian))

    return {
        "data_tabel": data_tabel,         
        "h": h,                           
        "selang_akar": selang_akar,       
        "akar_terbaik": akar_terbaik,    
        "iterasi_akar": iterasi_akar 
    }