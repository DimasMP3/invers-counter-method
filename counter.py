#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fractions import Fraction

# ---------- pretty print ---------- #
def fmt_frac(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)

def aug_str(L, R):
    wl = [0]*len(L[0]); wr = [0]*len(R[0])
    Ls = [[fmt_frac(v) for v in row] for row in L]
    Rs = [[fmt_frac(v) for v in row] for row in R]
    for j in range(len(wl)):
        wl[j] = max(len(Ls[i][j]) for i in range(len(Ls)))
    for j in range(len(wr)):
        wr[j] = max(len(Rs[i][j]) for i in range(len(Rs)))
    lines=[]
    for i in range(len(L)):
        lpad = [Ls[i][j].rjust(wl[j]) for j in range(len(wl))]
        rpad = [Rs[i][j].rjust(wr[j]) for j in range(len(wr))]
        lines.append("[ " + "  ".join(lpad) + "  |  " + "  ".join(rpad) + " ]")
    return "\n".join(lines)

# ---------- metode kounter “slide style” ---------- #
def inverse_kounter_slide(A_in):
    """A_in: list[list[angka]] 3×3. Mengembalikan A^{-1} (list of list Fraction)."""
    n = 3
    A = [[Fraction(x).limit_denominator() for x in row] for row in A_in]
    L = [[Fraction(int(i==j),1) for j in range(n)] for i in range(n)]  # Left = I
    R = [[A[i][j] for j in range(n)] for i in range(n)]                # Right = A

    print("Mulai dari [I | A]:")
    print(aug_str(L, R))

    # --------- Fase 1: buat segitiga atas (nihilkan bawah pivot) --------- #
    for k in range(n):
        print(f"\n=== Pivot kolom {k+1} ===")

        # a) pivoting jika perlu
        p = None
        for i in range(k, n):
            if R[i][k] != 0:
                p = i; break
        if p is None:
            raise ValueError("Matriks singular (pivot kolom nol semua).")
        if p != k:
            print(f"H_swap: Tukar baris {k+1} ↔ {p+1}")
            L[k], L[p] = L[p], L[k]
            R[k], R[p] = R[p], R[k]
            print(aug_str(L, R))

        # b) SCALE: buat pivot = 1 (hanya jika ≠ 1)
        pivot = R[k][k]
        if pivot != 1:
            alpha = Fraction(1,1)/pivot
            print(f"H_{k+1}({fmt_frac(alpha)}): Skala baris {k+1} dengan {fmt_frac(alpha)} (pivot -> 1)")
            L[k] = [alpha*v for v in L[k]]
            R[k] = [alpha*v for v in R[k]]
            print(aug_str(L, R))

        # c) ELIM bawah: Ri <- Ri - a_ik * Rk (sehingga entri (i,k) = 0)
        for i in range(k+1, n):
            if R[i][k] != 0:
                beta = -R[i][k]  # karena pivot di R[k][k] = 1
                print(f"H_{i+1}{k+1}({fmt_frac(beta)}): B{i+1} <- B{i+1} + ({fmt_frac(beta)})*B{k+1}")
                L[i] = [L[i][j] + beta*L[k][j] for j in range(n)]
                R[i] = [R[i][j] + beta*R[k][j] for j in range(n)]
                print(aug_str(L, R))

    # --------- Fase 2: sapu ke atas (nihilkan di atas pivot) --------- #
    print("\n=== Penyapuan ke atas (nihilkan elemen di atas diagonal utama) ===")
    for k in range(n-1, -1, -1):  # dari kolom terakhir ke pertama
        for i in range(0, k):
            if R[i][k] != 0:
                beta = -R[i][k]  # pivot = 1
                print(f"H_{i+1}{k+1}({fmt_frac(beta)}): B{i+1} <- B{i+1} + ({fmt_frac(beta)})*B{k+1}")
                L[i] = [L[i][j] + beta*L[k][j] for j in range(n)]
                R[i] = [R[i][j] + beta*R[k][j] for j in range(n)]
                print(aug_str(L, R))

    # selesai
    print("\nSelesai: sisi kanan sudah menjadi I, sisi kiri adalah A^{-1}.")
    print("A^{-1} (pecahan) =")
    print(aug_str(L, R).split("|")[0].strip())  # cuma sisi kiri yang dicetak rapi

    print("\nA^{-1} (desimal) =")
    for row in L:
        print("[ " + "  ".join(f"{float(v): .8f}" for v in row) + " ]")

    return L

# ---------- CLI ---------- #
if __name__ == "__main__":
    print("Masukkan matriks 3x3 baris per baris (pisahkan angka dengan spasi/koma).")
    rows=[]
    for r in range(3):
        while True:
            try:
                line = input(f"Baris {r+1}: ").replace(",", " ")
                nums = [int(x) if x.strip().lstrip('+-').isdigit() else float(x) for x in line.split()]
                if len(nums)!=3: raise ValueError("Harus 3 angka per baris.")
                rows.append(nums); break
            except Exception as e:
                print("Input tidak valid:", e, "- Coba lagi.")
    inverse_kounter_slide(rows)
