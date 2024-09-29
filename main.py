print ("======================================================================")
print ("Program Menghitung Gaji Karyawan Berdasarkan Jam Kerja dan Tarif Kerja")
print ("======================================================================")

print("Registrasi Akun")
akun = input("Masukan Nama: ")
nim = input("Masukan NIM: ")
print("Akun Berhasil di Registrasi")


print("\nLogin Akun")
akun_2 = input("Masukan Nama: ")
nim_2 = input("Masukan NIM: ")

if akun_2 != akun or nim_2 != nim:
	print("\nAkun Anda Salah, Silahkan Login Kembali")
	akun_2 = input("Masukan Nama: ")
	nim_2 = input("Masukan NIM: ")

if akun_2 == akun and nim_2 == nim:
	print("Login Berhasil")
	while True:
		print ("\nApakah Anda Ingin Menghitung Gaji")
		opsi = ("1. Hitung Gaji", "2. Keluar Program")
		for x in opsi:
			print (x)
		pilih = input("Silahkan Pilih Opsi: ")
		if pilih == "1":
			Tarif = int(input("\nSilahkan Masukan Tarif Kerja Rp/Jam: "))
			Jam = int(input("Masukan Jam Kerja: "))
			Gaji = Tarif * Jam
			Bonus = Gaji * 0.1
			Total = Bonus + Gaji
			print ("\n======================================================================")
			print ("Tarif kerja anda: RP.", Tarif, "/ Jam")
			print ("Jam Kerja Anda: ", Jam, "Jam")
			print ("Gaji Anda: RP. ", Gaji)
			if Jam > 160:
				print ("Bonus Anda Sebesar: RP.", Bonus)
				print ("Total Gaji Anda Sebesar: RP.", Total)
			print ("=======================================================================")
		elif pilih == "2":	
			print("\nSampai Jumpa Lagi")
			break	
		else:
			print("Input Yang Anda Masukan Salah Silahkan Coba Lagi")

else:
	print("Command Tidak Valid")

