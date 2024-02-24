import os
import datetime
from prettytable import PrettyTable

def cls():
    os.system('cls')

class Laporan:
    def __init__(self, id_laporan, nama_pelapor, tanggal_laporan, judul_laporan, isi_laporan):
        self.id_laporan = id_laporan
        self.nama_pelapor = nama_pelapor
        self.tanggal_laporan = tanggal_laporan
        self.judul_laporan = judul_laporan
        self.isi_laporan = isi_laporan


class LaporanCrud:
    def __init__(self):
        self.laporan_list = []
        self.id_last = 0

    def tabel_laporan(self):
        if not self.laporan_list:
            print("""
+-------------------------+
|    Tidak Ada Laporan    |
+-------------------------+""")
        else:
            table = PrettyTable()
            table.field_names = ["ID", "Pengadu", "Tanggal", "Judul", "Isi Laporan"]

            for laporan in self.laporan_list:
                table.add_row([
                    laporan.id_laporan,
                    laporan.nama_pelapor,
                    laporan.tanggal_laporan,
                    laporan.judul_laporan,
                    laporan.isi_laporan
                ])

            print(table)

    def create_laporan(self, laporan):
        self.id_last += 1
        laporan.id_laporan = self.id_last
        self.laporan_list.append(laporan)
        cls()
        print("""
+---------------------------+
|    Laporan Ditambahkan    |
+---------------------------+
""")

    def read_laporan(self):
        self.tabel_laporan()

    def laporan_detail(self, id_laporan):
        for laporan in self.laporan_list:
            if laporan.id_laporan == id_laporan:
                return laporan
        return None

    def update_laporan(self, id_laporan, judul_baru, isi_baru):
        laporan = self.laporan_detail(id_laporan)
        if laporan:
            laporan.judul_laporan = judul_baru
            laporan.isi_laporan = isi_baru
            cls()
            print("""
+--------------------------+
|    Laporan Diperbarui    |
+--------------------------+
""")
        else:
            print("""
+-------------------------------+
|    Laporan Tidak Ditemukan    |
+-------------------------------+
""")

    def delete_laporan(self, id_laporan):
        laporan = self.laporan_detail(id_laporan)
        if laporan:
            self.laporan_list.remove(laporan)
            cls()
            print("""
+-----------------------+
|    Laporan Dihapus    |
+-----------------------+
""")
        else:
            cls()
            print("""
+-------------------------------+
|    Laporan Tidak Ditemukan    |
+-------------------------------+
""")


def input_laporan():
    id_laporan = None
    nama_pelapor = input("Masukkan Nama Pelapor : ")
    tanggal_laporan = datetime.date.today()
    judul_laporan = input("Masukkan Judul Laporan : ")
    isi_laporan = input("Masukkan Isi Laporan : ")

    return Laporan(id_laporan, nama_pelapor, tanggal_laporan, judul_laporan, isi_laporan)

laporan = LaporanCrud()

while True:
    print("Menu Pengaduan Masyarakat : ")
    print("1. Tambah Laporan")
    print("2. Tampilkan Laporan")
    print("3. Update Laporan")
    print("4. Hapus Laporan")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5) : ")

    if pilihan == '1':
        cls()
        laporan.create_laporan(input_laporan())
    elif pilihan == '2':
        cls()
        laporan.read_laporan()
        input('Tekan "Enter" untuk keluar')
        cls()
    elif pilihan == '3':
        cls()
        while True:
            laporan.read_laporan()
            id_laporan = int(
                input("Masukkan ID Laporan yang akan diupdate : "))
            if laporan.laporan_detail(id_laporan):
                judul_baru = input("Masukkan Judul Baru : ")
                isi_baru = input("Masukkan Isi Baru : ")
                laporan.update_laporan(id_laporan, judul_baru, isi_baru)
                break
            else:
                cls()
                print("""
+------------------------------------------+
|    Laporan Tidak Ditemukan, Coba Lagi    |
+------------------------------------------+
""")
    elif pilihan == '4':
        cls()
        while True:
            laporan.read_laporan()
            id_laporan = int(input("Masukkan ID Laporan yang akan dihapus : "))
            if laporan.laporan_detail(id_laporan):
                laporan.delete_laporan(id_laporan)
                break
            else:
                cls()
                print("""
+------------------------------------------+
|    Laporan Tidak Ditemukan, Coba Lagi    |
+------------------------------------------+
""")
    elif pilihan == '5':
        cls()
        print("""
+--------------+
|    Keluar    |
+--------------+
""")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")