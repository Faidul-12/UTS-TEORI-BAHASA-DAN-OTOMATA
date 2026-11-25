# LAPORAN PROYEK
## Simulasi NFA, DFA, dan Konversi NFA ke DFA Menggunakan Python

### Identitas Kelompok

| Keterangan | Informasi |
|---|---|
| Mata kuliah | Teori Bahasa dan Otomata |
| Dosen pengampu | Ibu Sita |
| Anggota kelompok | Faidul; Muh Arya Anggara; Iqram Hasan; Ikram Maulana |
| Program | Python, berkas `automata.py` |

## Abstrak

Laporan ini menjelaskan program Python untuk menyimulasikan *Nondeterministic Finite Automaton* (NFA), menyimulasikan *Deterministic Finite Automaton* (DFA), dan mengonversi NFA menjadi DFA. Contoh automata mengikuti materi kuliah dengan alfabet `{0, 1}`, state awal `q0`, dan state final `q2`. Konversi menggunakan metode *subset construction*, termasuk pembentukan state kosong sebagai *dead state*. Program menampilkan tabel transisi hasil konversi dan menyediakan menu untuk menguji input pada NFA, DFA, atau keduanya. Pada contoh ini, bahasa yang diterima adalah string yang diawali `0` dan memiliki setidaknya satu simbol `1` setelahnya, yaitu `0+1(0|1)*`.

**Kata kunci:** NFA, DFA, subset construction, automata berhingga, Python.

## 1. Pendahuluan

### 1.1 Latar belakang

Automata berhingga digunakan untuk memodelkan proses membaca simbol dan mengenali string dalam suatu bahasa. NFA dan DFA sama-sama memiliki state, alfabet, state awal, state final, dan fungsi transisi. NFA dapat menyimpan beberapa kemungkinan state sekaligus, sedangkan DFA memiliki tepat satu state aktif setelah membaca setiap simbol.

Salah satu cara untuk mengubah NFA menjadi DFA adalah *subset construction*. Setiap state DFA mewakili satu himpunan state NFA. Program dalam proyek ini dibuat agar cara kerja NFA, DFA, dan proses konversinya dapat diamati melalui langkah simulasi serta tabel transisi.

### 1.2 Rumusan masalah

1. Bagaimana menyimulasikan NFA untuk menentukan apakah suatu string diterima?
2. Bagaimana menyimulasikan DFA untuk input yang sama?
3. Bagaimana membentuk DFA dari NFA menggunakan *subset construction*?
4. Bagaimana memeriksa bahwa NFA dan DFA hasil konversi memberi hasil penerimaan yang sama?

### 1.3 Tujuan

1. Menjelaskan karakteristik dasar NFA dan DFA.
2. Membuat program Python untuk menyimulasikan NFA dan DFA.
3. Mengimplementasikan konversi NFA ke DFA menggunakan *subset construction*.
4. Menampilkan tabel transisi dan membandingkan hasil simulasi kedua automata.

### 1.4 Ruang lingkup

1. Program menggunakan contoh utama pada materi kuliah dengan alfabet `{0, 1}`.
2. Input diproses sebagai string yang setiap simbolnya satu karakter.
3. Definisi automata contoh sudah ditentukan di dalam kode program.
4. Program tidak mendukung transisi epsilon (`ε`). Contoh utama pada materi juga tidak menggunakan transisi epsilon.
5. Program belum menyediakan fitur untuk memasukkan definisi automata baru melalui menu.

## 2. Landasan Teori

### 2.1 Alfabet, string, dan bahasa

Alfabet adalah himpunan simbol yang dapat dibaca oleh automata. Pada proyek ini, alfabetnya adalah `Σ = {0, 1}`. String adalah urutan simbol dari alfabet, misalnya `01`, `001`, dan `101`. Bahasa adalah himpunan string yang diterima oleh automata.

### 2.2 NFA

NFA (*Nondeterministic Finite Automaton*) memiliki fungsi transisi yang menghasilkan himpunan state tujuan. Untuk satu state dan satu simbol, jumlah tujuan dapat nol, satu, atau lebih dari satu. String diterima jika setelah seluruh simbol dibaca setidaknya ada satu jalur yang berakhir di state final.

Secara formal, NFA ditulis sebagai `M = (Q, Σ, δ, q0, F)`, dengan `Q` himpunan state, `Σ` alfabet, `δ: Q × Σ → P(Q)` fungsi transisi, `q0` state awal, `F` himpunan state final, dan `P(Q)` himpunan kuasa dari `Q`.

### 2.3 DFA

DFA (*Deterministic Finite Automaton*) memiliki tepat satu state tujuan untuk setiap pasangan state dan simbol. Karena hanya ada satu jalur yang diikuti, program cukup menyimpan satu state aktif. String diterima jika state setelah seluruh simbol dibaca termasuk ke dalam himpunan state final.

### 2.4 Konversi NFA ke DFA

Dalam *subset construction*, setiap state DFA mewakili himpunan state NFA. State awal DFA adalah himpunan yang hanya berisi state awal NFA. Untuk setiap simbol, program menggabungkan semua tujuan transisi dari seluruh anggota himpunan tersebut. Himpunan tujuan yang baru ditemukan menjadi state DFA baru.

Himpunan kosong `∅` juga menjadi state DFA apabila muncul. State ini disebut *dead state* dan bertransisi kembali ke dirinya sendiri untuk setiap simbol. State DFA menjadi final apabila himpunannya memuat setidaknya satu state final NFA.

## 3. Perancangan Automata

### 3.1 Definisi NFA

NFA pada program memiliki definisi berikut:

- Himpunan state: `Q = {q0, q1, q2}`
- Alfabet: `Σ = {0, 1}`
- State awal: `q0`
- Himpunan state final: `F = {q2}`

Tabel transisi NFA:

| State | Input `0` | Input `1` |
|---|---|---|
| `q0` | `{q0, q1}` | `∅` |
| `q1` | `∅` | `{q1, q2}` |
| `q2` | `{q2}` | `{q2}` |

### 3.2 Bahasa yang diterima

String yang diterima harus diawali dengan setidaknya satu `0`, kemudian memiliki setidaknya satu `1`. Setelah itu, simbol `0` maupun `1` dapat muncul. Bentuk regulernya adalah `0+1(0|1)*`.

| String | Hasil | Penjelasan |
|---|---|---|
| `01` | Diterima | Diawali `0` dan diikuti `1` |
| `011` | Diterima | Diawali `0`, lalu membaca `1` |
| `001` | Diterima | Dua `0` diikuti `1` |
| `0010` | Diterima | Diawali `0`, memiliki `1`, lalu `0` |
| `0` | Ditolak | Tidak ada `1` setelah `0` |
| `1` | Ditolak | Dari state awal tidak ada transisi untuk `1` |
| `101` | Ditolak | Simbol pertama `1` membawa mesin ke himpunan kosong |

### 3.3 Langkah konversi ke DFA

Untuk memudahkan pencocokan dengan materi, himpunan state DFA diberi nama A sampai E:

- `A = {q0}`
- `B = {q0, q1}`
- `C = {q1, q2}`
- `D = ∅`
- `E = {q2}`

Perhitungan transisi:

1. Dari `A = {q0}` dengan input `0`, tujuan adalah `{q0, q1} = B`. Dengan input `1`, tujuan adalah `∅ = D`.
2. Dari `B = {q0, q1}` dengan input `0`, gabungan tujuan adalah `{q0, q1} ∪ ∅ = B`. Dengan input `1`, gabungan tujuan adalah `∅ ∪ {q1, q2} = C`.
3. Dari `C = {q1, q2}` dengan input `0`, gabungan tujuan adalah `∅ ∪ {q2} = E`. Dengan input `1`, gabungan tujuan adalah `{q1, q2} ∪ {q2} = C`.
4. Dari `D = ∅`, kedua input tetap menuju `D`.
5. Dari `E = {q2}`, kedua input tetap menuju `E`.

Tabel transisi DFA:

| State DFA | Himpunan NFA | Input `0` | Input `1` | Status |
|---|---|---|---|---|
| A | `{q0}` | B | D | Awal |
| B | `{q0, q1}` | B | C | — |
| C | `{q1, q2}` | E | C | Final |
| D | `∅` | D | D | *Dead state* |
| E | `{q2}` | E | E | Final |

Himpunan state final DFA adalah `{C, E}` karena C dan E memuat state final NFA `q2`.

### 3.4 Pemetaan nama state pada program

Program memberi label otomatis `S0` sampai `S4`. Label tersebut memiliki pemetaan berikut:

| Label program | Label pada materi | Himpunan NFA |
|---|---|---|
| `S0` | A | `{q0}` |
| `S1` | B | `{q0, q1}` |
| `S2` | D | `∅` |
| `S3` | C | `{q1, q2}` |
| `S4` | E | `{q2}` |

Dengan demikian, state final program adalah `S3` dan `S4`.

## 4. Perancangan dan Implementasi Program

### 4.1 Perangkat

- Bahasa pemrograman: Python.
- Pustaka: `collections.deque` dan `dataclasses` dari pustaka standar Python.
- Berkas program: `automata.py`.
- Program dijalankan melalui terminal.

### 4.2 Struktur program

1. `Automaton` menyimpan state, alfabet, state awal, state final, dan transisi.
2. `make_example_nfa()` membentuk NFA sesuai tabel pada laporan ini.
3. `simulate_nfa()` melacak himpunan state aktif untuk setiap simbol input.
4. `convert_nfa_to_dfa()` menjalankan *subset construction* dan membuat state kosong jika diperlukan.
5. `simulate_dfa()` menjalankan input dengan satu state aktif.
6. `print_dfa_table()` menampilkan state DFA, himpunan NFA yang diwakili, transisi, dan statusnya.
7. `main()` menampilkan automata, tabel konversi, serta menu simulasi.

### 4.3 Algoritma konversi

```text
Masukkan NFA
Bentuk state awal DFA dari {state awal NFA}
Masukkan state awal ke antrean
Selama antrean belum kosong:
    Ambil satu himpunan state NFA dari antrean
    Untuk setiap simbol alfabet:
        Gabungkan semua state tujuan NFA
        Jika himpunan tujuan belum pernah ditemukan:
            Daftarkan sebagai state DFA baru
            Masukkan ke antrean
        Catat transisi DFA
Tandai state DFA final jika himpunannya memuat state final NFA
Tampilkan tabel DFA
```

### 4.4 Cara menjalankan

1. Pastikan Python sudah tersedia.
2. Buka terminal pada folder yang berisi `automata.py`.
3. Jalankan `python automata.py`.
4. Pilih menu `1` untuk simulasi NFA, `2` untuk simulasi DFA, atau `3` untuk membandingkan hasil keduanya.
5. Masukkan string yang hanya berisi `0` dan `1`. Tekan Enter tanpa mengetik simbol untuk menguji string kosong.
6. Pilih menu `0` untuk keluar.

## 5. Contoh Simulasi

### 5.1 NFA dengan input `001`

1. Kondisi awal: `{q0}`.
2. Membaca `0`: `{q0} → {q0, q1}`.
3. Membaca `0`: dari `q0` diperoleh `{q0, q1}`, sedangkan `q1` tidak memiliki transisi pada `0`; hasil gabungan `{q0, q1}`.
4. Membaca `1`: dari `q0` tidak ada tujuan, sedangkan dari `q1` diperoleh `{q1, q2}`; hasilnya `{q1, q2}`.
5. Hasil akhir memuat `q2`, sehingga `001` diterima.

### 5.2 DFA dengan input `001`

Jalurnya adalah `S0 → S1 → S1 → S3`. Karena `S3` adalah state final, input `001` diterima.

### 5.3 Perbandingan hasil

| Input | Hasil NFA | Hasil DFA | Keterangan |
|---|---|---|---|
| `001` | Diterima | Diterima | Berakhir pada state final |
| `011` | Diterima | Diterima | Berakhir pada state final |
| `0` | Ditolak | Ditolak | Tidak mencapai state final |
| `101` | Ditolak | Ditolak | Simbol pertama menuju state kosong |

NFA dan DFA hasil konversi memberi hasil yang sama karena setiap state DFA mewakili tepat himpunan state NFA yang mungkin aktif.

## 6. Kesimpulan

Program `automata.py` mengimplementasikan simulasi NFA, simulasi DFA, dan konversi NFA ke DFA menggunakan *subset construction*. Konversi membentuk lima state DFA yang dapat dijangkau, termasuk state kosong sebagai *dead state*. State final DFA adalah himpunan yang mengandung `q2`. Berdasarkan definisi transisi pada contoh materi, bahasa yang diterima berbentuk `0+1(0|1)*`. Simulasi NFA dan DFA hasil konversi mempertahankan hasil penerimaan yang sama untuk input yang diuji.

## Daftar Pustaka

1. Materi perkuliahan Teori Bahasa dan Otomata, “Konversi NFA ke DFA”, Bab 6–7, berkas presentasi yang diberikan.
2. Hopcroft, J. E., Motwani, R., & Ullman, J. D. *Introduction to Automata Theory, Languages, and Computation*. Pearson. Rujukan yang tercantum pada materi kuliah.
3. Sipser, M. *Introduction to the Theory of Computation*. Cengage Learning. Rujukan yang tercantum pada materi kuliah.

---

**Berkas program:** `automata.py`  
**Anggota kelompok:** Faidul, Muh Arya Anggara, Iqram Hasan, dan Ikram Maulana.
