# Caesar Cipher
### Deskripsi
Caesar cipher adalah teknik paling simpel yang digunakan
untuk enkripsi pesan. Untuk setiap karakter dilakukan
penggeseran sesuai dengan kuncinya.

Misalnya kita mengenkripsi pesan (plaintext) "aku hebat yes" dengan
kunci 3. Maka pesan hasil enkripsinya (ciphertext) "dnx khedw bhv".
Dan untuk kembali mendapatkan plaintextnya, mendekripsi, kita geser
karakter dengan kunci yang sama tetapi berlawanan arah.

Dalam soal ini, kamu diberikan ciphertext dari sebuat pesan yang menurut informasi
yang beredar isinya adalah deskripsi tugas keprof. Kamu diminta
untuk mendapatkan angka berapa yang digunakan
untuk enkripsi pesan tersebut.


###Input
Suatu ciphertext hasil dari enkripsi Caesar cipher,
yang penggeserannya berdasarkan kode ascii 0 s.d.127.


###Output
Bilangan bulat yang merupakan kunci untuk enkripsi dan 
dekripsi ciphertext tersebut.