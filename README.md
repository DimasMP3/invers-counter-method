# Invers Matriks 3x3 – Metode “Counter/Slide” (Langkah Demi Langkah)

Skrip `counter.py` menghitung invers matriks 3x3 menggunakan operasi baris elementer pada matriks teraugmentasi `[ I | A ]`. Seluruh proses dicetak langkah demi langkah sehingga cocok untuk pembelajaran dan verifikasi manual.

- File utama: `countermethod/counter.py`
- Fungsi inti: `inverse_kounter_slide(A_in)` di `countermethod/counter.py:26`
- CLI interaktif: blok `if __name__ == "__main__"` di `countermethod/counter.py:94`

## Fitur Utama

- Invers matriks 3x3 berbasis operasi baris elementer pada `[ I | A ]`.
- Menampilkan setiap langkah: pivoting, skala baris (membuat pivot = 1), dan eliminasi ke bawah/atas.
- Menggunakan `fractions.Fraction` agar perhitungan tetap rasional (tanpa error pembulatan) dan disajikan juga dalam desimal.
- Validasi singularitas: jika kolom pivot seluruhnya nol, melempar `ValueError` (matriks tidak inversibel).

## Prasyarat

- Python 3.8+
- Tidak ada dependensi eksternal (hanya modul standar `fractions`).

## Menjalankan (CLI Interaktif)

Jalankan skrip secara langsung dan masukkan elemen matriks 3x3 baris per baris.

```bash
python countermethod/counter.py
```

Contoh sesi:

```
Masukkan matriks 3x3 baris per baris (pisahkan angka dengan spasi/koma).
Baris 1: 2 1 0
Baris 2: 0 1 1
Baris 3: 1 0 1

Mulai dari [I | A]:
[ 1  0  0  |  2  1  0 ]
[ 0  1  0  |  0  1  1 ]
[ 0  0  1  |  1  0  1 ]

=== Pivot kolom 1 ===
H_1(1/2): Skala baris 1 dengan 1/2 (pivot -> 1)
...

Selesai: sisi kanan sudah menjadi I, sisi kiri adalah A^{-1}.
A^{-1} (pecahan) =
[ 1/2  -1/2   1/2 ]
[   0     1    -1 ]
[ -1/2  1/2   1/2 ]

A^{-1} (desimal) =
[  0.50000000  -0.50000000   0.50000000 ]
[  0.00000000   1.00000000  -1.00000000 ]
[ -0.50000000   0.50000000   0.50000000 ]
```

> Tip: Jika terminal menampilkan karakter aneh pada simbol panah/operasi, itu hanya masalah encoding tampilan. Perhitungan tetap benar.

## Menggunakan Sebagai Modul (API)

Impor dan panggil fungsi utama untuk mendapatkan hasil dalam bentuk pecahan (`Fraction`).

```python
from countermethod.counter import inverse_kounter_slide

A = [
    [2, 1, 0],
    [0, 1, 1],
    [1, 0, 1],
]
A_inv = inverse_kounter_slide(A)  # -> list[list[Fraction]]

# contoh akses angka desimal
A_inv_float = [[float(x) for x in row] for row in A_inv]
```

Ringkasan API:

- `inverse_kounter_slide(A_in: list[list[float|int]]) -> list[list[Fraction]]`: Mengembalikan matriks invers sebagai pecahan dan mencetak seluruh proses ke stdout.

## Format Output Langkah

- `[ L | R ]` adalah matriks teraugmentasi, dengan `L` di kiri dan `R` di kanan.
- Di awal: `[ I | A ]`. Sesudah selesai: `[ A^{-1} | I ]`.
- Notasi operasi yang dicetak:
  - Pivoting (tukar baris) bila diperlukan.
  - `H_k(alpha)`: skala baris ke-`k` dengan faktor `alpha` agar pivot menjadi `1`.
  - `H_ik(beta)`: baris `i` ditambah `beta * baris k` untuk men-nol-kan elemen pada kolom pivot.

## Batasan & Catatan

- Khusus matriks 3x3 (`n = 3`).
- Jika ada kolom pivot yang seluruhnya nol, fungsi akan melempar `ValueError("Matriks singular ...")`.
- Perhitungan internal memakai `Fraction`, sehingga output pecahan bersih dan hasil desimal dicetak terformat.

## Struktur Kode Terkait

- Formatter pecahan dan util cetak: `countermethod/counter.py:6`
- Fungsi utama inversi: `countermethod/counter.py:26`
- Entrypoint CLI interaktif: `countermethod/counter.py:94`

Selamat belajar dan bereksperimen!

