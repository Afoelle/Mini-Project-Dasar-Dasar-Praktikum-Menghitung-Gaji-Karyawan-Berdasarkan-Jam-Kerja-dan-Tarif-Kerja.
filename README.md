# Mini-Project-Dasar-Dasar-Praktikum-Menghitung-Gaji-Karyawan-Berdasarkan-Jam-Kerja-dan-Tarif-Kerja.

Flowchart:

![Flow Chart drawio](https://github.com/user-attachments/assets/6689ce84-bbda-469a-b850-41be356140e6)

Penjelasan:
1. Baris 1-3: Untuk memunculkan judul dengan print
2. Baris 5-8: Untuk registrasi akun menggunakan input agar bisa memasukan tulisan
3. baris 10-19: Untuk menu login menggunakan input agar bisa memasukan tulisan, memakai perulangan while True, pengkondisian if != (bukan sama dengan), dan or agar jika salah satu diantara akun atau nim tidak sesuai dengan yang kalian masukan pada menu registrasi maka akan kembali ke menu login, dan jika sesuai maka saya memakai else dan akan muncul tulisan "login berhasil" serta break untuk menghentikan looping
4. Baris 21-23: Memakai while True untuk melakukan perulangan, serta, menggunakan input untuk memasukan tarif kerja/jam dan jam kerja
5. Baris 24-26: Untuk menghitung rumus dan memasukannya ke dalam variabel, rumusnya yaitu gaji = Tarif x Jam, Bonus = Gaji x 0,1 karena 0,1 = 10%, dan Total = Bonus + Gaji
6. Baris 27-30: Untuk mengeluarkan hasil dari tarif, jam kerja, dan gaji
7. Baris 31-34: Memakai if untuk memberi kondisi menentukan apakah jam kerja karyawan lebih dari 160 jam. Jika lebih, tambahkan bonus sebesar 10% dari total gaji. Sedangkan jika tidak mencapai lebih dari 160 jam, maka tidak mendapatkan bonus, serta menggunakan print untuk mengeluarkan bonus dan total gaji
8. Baris 35-37: Membuat list pada baris 35 dan untuk mengeluarkannya vertikal menggunakan for dan menggunakan input untuk memasukan pilihan
9. Baris 39-40: Menggunakan if == (sama dengan) untuk memasukan pilihan spesifik dan menggunakan continue program diulang ke input tarif kerja
10. Baris 41-43: Menggunakan elif karena sudah ada if untuk memasukan pilihan spesifik dan menggunakan break untuk mengakhiri looping dan mengakhiri program
11. baris 44-45: Menggunakan else agar jika input yang dimasukan tidak ada di pilihan akan keluar tulisan "Input Yang Anda Masukan Salah Silahkan Coba Lagi"
