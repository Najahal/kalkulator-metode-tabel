import math

def hitung_metode_tabel(fungsi_str, batas_bawah, batas_atas, n_subinterval):
    """
    Menghitung pencarian akar fungsi menggunakan Metode Tabel.
    
    Rumus step size: h = (b - a) / N
    
    Parameters:
        fungsi_str (str): String fungsi f(x), contoh: "x**3 - x - 1"
        batas_bawah (float): Batas bawah interval (a / b)
        batas_atas (float): Batas atas interval (a / b)
        n_subinterval (int): Jumlah pembagian sub-interval (N)
        
    Returns:
        dict: Berisi data tabel (list of tuple), selang akar, estimasi akar terbaik, dan pesan status.
    """
    # Menentukan nilai a dan b sebenarnya
    a = min(batas_bawah, batas_atas)
    b = max(batas_bawah, batas_atas)
    
    # Menghitung h = (b - a) / N
    h = (b - a) / n_subinterval
    
    # Menyiapkan namespace fungsi matematika dasar agar pengguna bisa pakai sin, cos, exp, sqrt, dll.
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

    data_tabel = []
    for i in range(n_subinterval + 1):
        x_i = a + i * h
        fx_i = evaluasi_fungsi(x_i)
        data_tabel.append((i, x_i, fx_i))
        
    # Mencari selang akar (perubahan tanda f(x)) dan estimasi akar terbaik (|f(x)| terkecil)
    selang_akar = None
    akar_terbaik = None
    min_fx = float('inf')
    
    for i in range(len(data_tabel)):
        idx, x_val, fx_val = data_tabel[i]
        
        # Cek nilai |f(x)| terkecil untuk estimasi akar terbaik
        if abs(fx_val) < min_fx:
            min_fx = abs(fx_val)
            akar_terbaik = (x_val, fx_val)
            
        # Cek perubahan tanda antar dua titik berurutan f(x_i) * f(x_{i+1}) <= 0
        if i < len(data_tabel) - 1:
            _, x_next, fx_next = data_tabel[i + 1]
            if fx_val * fx_next <= 0:
                selang_akar = ((x_val, fx_val), (x_next, fx_next))

    return {
        "data_tabel": data_tabel,         # Format: [(i, x, f(x)), ...]
        "h": h,                           # Step size
        "selang_akar": selang_akar,       # Format: ((x1, f(x1)), (x2, f(x2)))
        "akar_terbaik": akar_terbaik,     # Format: (x_terbaik, f(x_terbaik))
    }
