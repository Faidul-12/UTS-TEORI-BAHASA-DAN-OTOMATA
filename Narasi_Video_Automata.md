# Naskah Narasi Video Program NFA, DFA, dan Konversi NFA ke DFA

**Anggota kelompok:** Faidul, Muh Arya Anggara, Iqram Hasan, dan Ikram Maulana  
**Perkiraan durasi:** 5–6 menit  
**Program:** `automata.py`

Petunjuk dalam tanda kurung siku adalah arahan visual dan tidak perlu dibacakan.

## 1. Pembukaan dan pengantar — Faidul

**[Tampilkan judul video dan nama anggota kelompok.]**

**Faidul:**

“Assalamu’alaikum warahmatullahi wabarakatuh.

Halo semuanya. Kami dari kelompok yang beranggotakan Faidul, Muh Arya Anggara, Iqram Hasan, dan Ikram Maulana. Dalam video ini, kami akan menjelaskan program Python untuk simulasi NFA, simulasi DFA, dan konversi NFA ke DFA.

Program kami mengikuti contoh utama pada materi Teori Bahasa dan Otomata. Alfabet yang digunakan adalah `0` dan `1`. Proses konversinya menggunakan metode *subset construction*, yaitu metode yang menjadikan himpunan state NFA sebagai state DFA.”

## 2. Definisi dan transisi NFA — Muh Arya Anggara

**[Tampilkan diagram atau tabel transisi NFA pada PPT.]**

**Muh Arya Anggara:**

“NFA adalah *Nondeterministic Finite Automaton*. Untuk satu state dan satu simbol, NFA dapat memiliki beberapa state tujuan, satu tujuan, atau bahkan tidak memiliki tujuan.

NFA pada contoh ini memiliki state `q0`, `q1`, dan `q2`. State awalnya adalah `q0`, dan state finalnya adalah `q2`. Jika membaca `0` dari `q0`, mesin dapat berpindah ke `q0` dan `q1` sekaligus. Jika membaca `1` dari `q0`, tidak ada transisi. Dari `q1`, input `1` membawa mesin ke `q1` dan `q2`. State `q2` tetap menjadi `q2` saat membaca `0` maupun `1`.

Karena itu, simulasi NFA melacak sekumpulan state yang mungkin aktif. Contohnya, string `001` diterima. Setelah membaca dua simbol `0`, state aktifnya `{q0, q1}`. Setelah membaca `1`, state aktifnya menjadi `{q1, q2}`. Karena himpunan itu memuat state final `q2`, string diterima.”

## 3. Konversi NFA ke DFA — Iqram Hasan

**[Tampilkan tabel hasil konversi yang dicetak program.]**

**Iqram Hasan:**

“DFA adalah *Deterministic Finite Automaton*. Pada DFA, untuk setiap state dan simbol input, hanya ada satu state tujuan. Jadi, simulasi DFA cukup melacak satu state pada setiap langkah.

Program mengonversi NFA ke DFA dengan metode *subset construction*. State awal DFA mewakili `{q0}`. Dari `{q0}`, input `0` menghasilkan `{q0, q1}`, sedangkan input `1` menghasilkan himpunan kosong. Himpunan kosong tetap dimasukkan sebagai state DFA dan menjadi *dead state*, karena semua transisinya kembali ke himpunan kosong.

Program memberi nama state DFA `S0` sampai `S4`. Pemetaan terhadap nama di PPT adalah: `S0` sama dengan A, `S1` sama dengan B, `S3` sama dengan C, `S2` sama dengan D, dan `S4` sama dengan E. State DFA menjadi final jika himpunannya memuat state final NFA, yaitu `q2`. Maka state finalnya adalah `S3` dan `S4`.”

## 4. Demo program dan penutup — Ikram Maulana

**[Tampilkan terminal. Jalankan `python automata.py` dari folder program.]**

**Ikram Maulana:**

“Sekarang kita lihat demonya. Saat program dijalankan, definisi NFA dan tabel transisi DFA hasil konversi ditampilkan. Setelah itu, tersedia menu simulasi NFA, simulasi DFA, perbandingan hasil, dan pilihan untuk keluar.

Kita pilih menu `3` untuk membandingkan NFA dan DFA, lalu masukkan `001`. Program menunjukkan bahwa keduanya menerima string tersebut. Sekarang kita coba `101`. Keduanya menolak, karena dari state awal `q0` tidak ada transisi untuk input `1`, sehingga mesin masuk ke himpunan kosong.

Dari demo ini, kita melihat bahwa NFA melacak beberapa kemungkinan state, sedangkan DFA melacak satu state. Konversi dengan *subset construction* membuat DFA yang hasil penerimaannya sama dengan NFA untuk contoh yang digunakan.

Demikian penjelasan program NFA, DFA, dan konversi NFA ke DFA dari kelompok kami. Terima kasih telah menyaksikan video ini.

Wassalamu’alaikum warahmatullahi wabarakatuh.”

**[Akhiri program dengan memilih menu `0`, lalu tampilkan kembali judul atau nama anggota kelompok.]**

## Pembagian bagian

| Anggota | Bagian |
|---|---|
| Faidul | Pembukaan dan pengantar program |
| Muh Arya Anggara | Pengertian serta transisi NFA |
| Iqram Hasan | Pengertian DFA dan proses konversi |
| Ikram Maulana | Demo program dan penutup |
