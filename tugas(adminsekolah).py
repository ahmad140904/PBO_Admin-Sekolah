import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='5220411277'
)
cursor = db.cursor(dictionary=True)

class Sekolah:
    def tambah_siswa(self, nis, nama_siswa, nama_kelas, alamat):
        query = "INSERT INTO kelas(NIS, Nama_Siswa, Kelas, Alamat) VALUES(%s, %s, %s, %s)"
        nilai = (nis, nama_siswa, nama_kelas, alamat)
        cursor.execute(query, nilai)
        db.commit()
        print("SISWA BERHASIL DI TAMBAHKAN")

    def tampilkan_siswa(self):
        cursor.execute("SELECT DISTINCT Kelas FROM kelas")
        kelas_list = [kelas['Kelas'] for kelas in cursor.fetchall()]

        while True:
            print("Pilih kelas:")
            for i, kelas in enumerate(kelas_list, 1):
                print(f"{i}. {kelas}")

            print(f"{len(kelas_list) + 1}. Kembali ke Menu Utama")

            pilihan_kelas = int(input("Masukkan nomor kelas: "))

            if 0 < pilihan_kelas <= len(kelas_list):
                kelas_terpilih = kelas_list[pilihan_kelas - 1]
                self.__tampilkan_siswa_kelas(kelas_terpilih)
            elif pilihan_kelas == len(kelas_list) + 1:
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def __tampilkan_siswa_kelas(self, kelas):
        cursor.execute(f"SELECT * FROM kelas WHERE Kelas = '{kelas}'")
        hasil = cursor.fetchall()

        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"|    NIS    |    Nama Siswa    | Kelas |      Alamat      |")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        for baris in hasil:
            print(f"| {baris['NIS']:<10}| {baris['Nama_Siswa']:<16} | {baris['Kelas']:<5} | {baris['Alamat']:<16} |")

        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def tampilkan_jumlah_siswa(self):
        cursor.execute("SELECT Kelas, COUNT(*) as Jumlah_Siswa FROM kelas GROUP BY Kelas")
        hasil = cursor.fetchall()

        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"| Kelas | Jumlah Siswa Keseluruhan |")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        for baris in hasil:
            print(f"| {baris['Kelas']:<5} | {baris['Jumlah_Siswa']:<24} |")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def update_alamat_siswa(self, nis):
        cursor.execute(f"SELECT * FROM kelas WHERE NIS={nis}")
        info_siswa = cursor.fetchone()
        self.__tampilkan_siswa_kelas(info_siswa['Kelas'])
        alamat_baru = input("Masukkan Alamat Siswa yang Baru: ")
        cursor.execute(f"UPDATE kelas SET Alamat='{alamat_baru}' WHERE NIS={nis}")
        db.commit()
        print("---ALAMAT BERHASIL DI UPDATE---")

    def __hapus_siswa(self, nis):
        cursor.execute(f"SELECT * FROM kelas WHERE NIS={nis}")
        info_siswa = cursor.fetchone()
        self.__tampilkan_siswa_kelas(info_siswa['Kelas'])
        cursor.execute(f"DELETE FROM kelas WHERE NIS={nis}")
        db.commit()
        print("---SISWA BERHASIL DI HAPUS---")

    def dashboard_sekolah(self):
        while True:
            print("===== DASHBOARD SMAN 1 CILACAP =====")
            print("1. Tambah Siswa")
            print("2. Tampilkan Siswa")
            print("3. Tampilkan Keseluruhan Siswa")
            print("4. Update Alamat Siswa")
            print("5. Hapus Siswa")
            print("0. Keluar")
            pilihan = int(input("Silahkan pilih menu: "))

            if pilihan == 1:
                nis = int(input("Masukkan NIS Siswa: "))
                nama_siswa = input("Masukkan Nama Siswa: ")
                nama_kelas = input("Masukkan Nama Kelas (A, B, C, D, E): ")
                alamat = input("Masukkan Alamat Siswa: ")
                self.tambah_siswa(nis, nama_siswa, nama_kelas, alamat)
            elif pilihan == 2:
                self.tampilkan_siswa()
            elif pilihan == 3:
                self.tampilkan_jumlah_siswa()
            elif pilihan == 4:
                nis = int(input("Masukkan NIS Siswa: "))
                self.update_alamat_siswa(nis)
            elif pilihan == 5:
                nis = int(input('Masukkan NIS Siswa: '))
                self.__hapus_siswa(nis)
            else:
                break

sekolah = Sekolah()

while True:
    print("1. Admin Sekolah")
    print("0. Keluar")
    pilihan_pengguna = int(input("SEMANGAT UNTUK HARI INI (tekan 1 untuk mulai) 1/0: "))

    if pilihan_pengguna == 1:
        sekolah.dashboard_sekolah()
    else:
        break
