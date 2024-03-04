import os
import datetime
from prettytable import PrettyTable

def cls():
    os.system('cls')
cls()

class Laporan:
    def __init__(self, id_laporan, pelapor, judul_laporan, isi_laporan, tanggal_laporan):
        self.id_laporan = id_laporan
        self.pelapor = pelapor
        self.judul_laporan = judul_laporan
        self.isi_laporan = isi_laporan
        self.tanggal_laporan = tanggal_laporan
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.id_last = 0

    def is_empty(self):
        return self.head is None

    def create_pretty_table(self):
        table = PrettyTable()
        table.field_names = ["ID", "Pelapor", "Judul Laporan", "Isi Laporan", "Tanggal Laporan"]

        current_node = self.head
        while current_node:
            table.add_row([current_node.id_laporan, current_node.pelapor, current_node.judul_laporan, current_node.isi_laporan, current_node.tanggal_laporan])
            current_node = current_node.next

        table.title = "Laporan Table"
        return table

    def create_laporan_head(self, id_laporan, pelapor, judul_laporan, isi_laporan, tanggal_laporan):
        if id_laporan is None:
            id_laporan = self.id_last + 1
            self.id_last += 1

        new_node = Laporan(id_laporan, pelapor, judul_laporan, isi_laporan, tanggal_laporan)
        new_node.next = self.head
        self.head = new_node

    def create_laporan_tail(self, id_laporan, pelapor, judul_laporan, isi_laporan, tanggal_laporan):
        if id_laporan is None:
            id_laporan = self.id_last + 1
            self.id_last += 1

        new_node = Laporan(id_laporan, pelapor, judul_laporan, isi_laporan, tanggal_laporan)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def create_laporan_between(self, id_laporan, pelapor, judul_laporan, isi_laporan, tanggal_laporan, posisi):
        if id_laporan is None:
            id_laporan = self.id_last + 1
            self.id_last += 1

        posisi = int(posisi)

        if posisi == 0:
            self.create_laporan_head(id_laporan, pelapor, judul_laporan, isi_laporan, tanggal_laporan)
            return

        current_node = self.head
        for x in range(posisi - 1):
            if not current_node:
                print("Input Tidak Valid")
                return
            current_node = current_node.next

        new_node = Laporan(id_laporan, pelapor, judul_laporan, isi_laporan, tanggal_laporan)
        new_node.next = current_node.next
        current_node.next = new_node

    def laporan_detail(self, id_laporan):
        current_node = self.head
        while current_node:
            if current_node.id_laporan == id_laporan:
                return current_node
            current_node = current_node.next
        return None

    def read_laporan(self):
        table = self.create_pretty_table()
        print(table)

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

    def delete_head(self):
        if self.head:
            self.head = self.head.next
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

    def delete_tail(self):
        if self.head:
            if not self.head.next:
                self.head = None
            else:
                current_node = self.head
                while current_node.next.next:
                    current_node = current_node.next
                current_node.next = None
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

    def delete_between(self, posisi):
        posisi = int(posisi)
        if posisi == 0:
            self.delete_head()
            return

        current_node = self.head
        previous_node = None
        for x in range(posisi):
            if not current_node:
                print("Posisi melebihi panjang Linked List")
                return
            previous_node = current_node
            current_node = current_node.next

        if current_node:
            previous_node.next = current_node.next
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

tgl_lapor = datetime.date.today()
laporan = SingleLinkedList()

def input_laporan():
    input_id = None
    input_nama_pelapor = input("Masukkan Nama Pelapor : ")
    input_judul_laporan = input("Masukkan Judul Laporan : ")
    input_isi_laporan = input("Masukkan isi Laporan : ")
    input_tanggal_laporan = tgl_lapor

    cls()
    print("Pilih Tempat Menambahkan Laporan:")
    print("1. Di Awal (head)")
    print("2. Di Tengah")
    print("3. Di Akhir (tail)")

    pilihan_tempat = input("Pilih tempat penambahan (1-3): ")

    if pilihan_tempat == '1':
        laporan.create_laporan_head(input_id, input_nama_pelapor, input_judul_laporan, input_isi_laporan, input_tanggal_laporan)
        cls()
        print("""
    +---------------------------+
    |    Laporan Ditambahkan    |
    +---------------------------+
""")
    elif pilihan_tempat == '2':
        laporan.read_laporan()
        after_id = input("Input Laporan Setelah ID : ")
        laporan.create_laporan_between(None, input_nama_pelapor, input_judul_laporan, input_isi_laporan, input_tanggal_laporan, after_id)
        cls()
        print("""
+---------------------------+
|    Laporan Ditambahkan    |
+---------------------------+
""")
    elif pilihan_tempat == '3':
        laporan.create_laporan_tail(input_id, input_nama_pelapor, input_judul_laporan, input_isi_laporan, input_tanggal_laporan)
        cls()
        print("""
+---------------------------+
|    Laporan Ditambahkan    |
+---------------------------+
""")
    else:
        print("""
+---------------------------+
|    Pilihan Tidak Valid    |
+---------------------------+
""")

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
        input_laporan()
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
            id_laporan = input("Masukkan ID Laporan yang akan dihapus (tekan Enter untuk kembali): ")
            cls()

            if not id_laporan:
                break

            id_laporan = int(id_laporan)

            if laporan.laporan_detail(id_laporan):
                print("1. Hapus di awal (head)")
                print("2. Hapus di tengah-tengah")
                print("3. Hapus di akhir (tail)")

                pilihan_hapus = input("Pilih tempat penghapusan (1-3): ")

                if pilihan_hapus == '1':
                    laporan.delete_head()
                elif pilihan_hapus == '2':
                    laporan.read_laporan()
                    posisi_hapus = input("Masukkan posisi yang akan dihapus: ")
                    laporan.delete_between(int(posisi_hapus))
                elif pilihan_hapus == '3':
                    laporan.delete_tail()
                else:
                    print("Pilihan tidak valid.")
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