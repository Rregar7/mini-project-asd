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
        table.field_names = ["Posisi", "ID", "Pelapor", "Judul Laporan", "Isi Laporan", "Tanggal Laporan"]
        
        posisi_node = 1
        current_node = self.head
        while current_node:
            table.add_row([posisi_node, current_node.id_laporan, current_node.pelapor, current_node.judul_laporan, current_node.isi_laporan, current_node.tanggal_laporan])
            current_node = current_node.next
            posisi_node += 1

        table.title = "Laporan Table"
        return table

# WORKING SPACE ===============================================
    
    def merge_sort_asc_judul_laporan(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left = data[:mid]
            right = data[mid:]

            self.merge_sort_asc_judul_laporan(left)
            self.merge_sort_asc_judul_laporan(right)

            i = j = k = 0

            def value_judul_laporan(laporan):
                return laporan[2]

            while i < len(left) and j < len(right):
                if value_judul_laporan(left[i]) < value_judul_laporan(right[j]):
                    data[k] = left[i]
                    i += 1
                else:
                    data[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                data[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                data[k] = right[j]
                j += 1
                k += 1
    
    def merge_sort_desc_judul_laporan(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left = data[:mid]
            right = data[mid:]

            self.merge_sort_desc_judul_laporan(left)
            self.merge_sort_desc_judul_laporan(right)

            i = j = k = 0

            def value_judul_laporan(laporan):
                return laporan[2]

            while i < len(left) and j < len(right):
                if value_judul_laporan(left[i]) > value_judul_laporan(right[j]):
                    data[k] = left[i]
                    i += 1
                else:
                    data[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                data[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                data[k] = right[j]
                j += 1
                k += 1

    def merge_sort_asc_pelapor(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left = data[:mid]
            right = data[mid:]

            self.merge_sort_asc_pelapor(left)
            self.merge_sort_asc_pelapor(right)

            i = j = k = 0

            def value_nama_pelapor(laporan):
                return laporan[1]

            while i < len(left) and j < len(right):
                if value_nama_pelapor(left[i]) < value_nama_pelapor(right[j]):
                    data[k] = left[i]
                    i += 1
                else:
                    data[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                data[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                data[k] = right[j]
                j += 1
                k += 1

    def merge_sort_desc_pelapor(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left = data[:mid]
            right = data[mid:]

            self.merge_sort_asc_pelapor(left)
            self.merge_sort_asc_pelapor(right)

            i = j = k = 0

            def value_nama_pelapor(laporan):
                return laporan[1]

            while i < len(left) and j < len(right):
                if value_nama_pelapor(left[i]) > value_nama_pelapor(right[j]):
                    data[k] = left[i]
                    i += 1
                else:
                    data[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                data[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                data[k] = right[j]
                j += 1
                k += 1

    def update_sorted_data(self, sorted_data):
        current_node = self.head
        for i in range(len(sorted_data)):
            current_node.pelapor = sorted_data[i][1]
            current_node.judul_laporan = sorted_data[i][2]
            current_node.isi_laporan = sorted_data[i][3]
            current_node.tanggal_laporan = sorted_data[i][4]
            current_node = current_node.next


# WORKING SPACE ===============================================

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
            self.create_laporan_head(
                id_laporan, pelapor, judul_laporan, isi_laporan, tanggal_laporan)
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
            print("+==========================+")
            print("|    Laporan Diperbarui    |")
            print("+==========================+")
        else:
            print("+===============================+")
            print("|    Laporan Tidak Ditemukan    |")
            print("+===============================+")

    def delete_head(self):
        if self.head:
            self.head = self.head.next
            cls()
            print("+=======================+")
            print("|    Laporan Dihapus    |")
            print("+=======================+")
        else:
            cls()
            print("+===============================+")
            print("|    Laporan Tidak Ditemukan    |")
            print("+===============================+")

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
            print("+=======================+")
            print("|    Laporan Dihapus    |")
            print("+=======================+")
        else:
            cls()
            print("+===============================+")
            print("|    Laporan Tidak Ditemukan    |")
            print("+===============================+")

    def delete_between(self, posisi):
        posisi = int(posisi)
        if posisi == 0:
            self.delete_head()
            return

        current_node = self.head
        previous_node = None
        for x in range(posisi):
            if not current_node:
                print("+===========================================+")
                print("|    Posisi melebihi panjang Linked List    |")
                print("+===========================================+")
                return
            previous_node = current_node
            current_node = current_node.next

        if current_node:
            previous_node.next = current_node.next
            cls()
            print("+=======================+")
            print("|    Laporan Dihapus    |")
            print("+=======================+")
        else:
            cls()
            print("+===============================+")
            print("|    Laporan Tidak Ditemukan    |")
            print("+===============================+")


tgl_lapor = datetime.date.today()
laporan = SingleLinkedList()


def input_laporan():
    input_id = None
    input_nama_pelapor = input("Masukkan Nama Pelapor : ")
    input_judul_laporan = input("Masukkan Judul Laporan : ")
    input_isi_laporan = input("Masukkan isi Laporan : ")
    input_tanggal_laporan = tgl_lapor

    cls()
    print("+===============================+")
    print("Pilih Tempat Menambahkan Laporan:")
    print("1. Di Awal (head)")
    print("2. Di Tengah")
    print("3. Di Akhir (tail)")
    print("+===============================+")

    pilihan_tempat = input("Pilih tempat penambahan (1-3): ")

    if pilihan_tempat == '1':
        laporan.create_laporan_head(
            input_id, input_nama_pelapor, input_judul_laporan, input_isi_laporan, input_tanggal_laporan)
        cls()
        print("+===========================+")
        print("|    Laporan Ditambahkan    |")
        print("+===========================+")
    elif pilihan_tempat == '2':
        laporan.read_laporan()
        after_id = input("Input Laporan Setelah Posisi : ")
        laporan.create_laporan_between(
            None, input_nama_pelapor, input_judul_laporan, input_isi_laporan, input_tanggal_laporan, after_id)
        cls()
        print("+===========================+")
        print("|    Laporan Ditambahkan    |")
        print("+===========================+")
    elif pilihan_tempat == '3':
        laporan.create_laporan_tail(
            input_id, input_nama_pelapor, input_judul_laporan, input_isi_laporan, input_tanggal_laporan)
        cls()
        print("+===========================+")
        print("|    Laporan Ditambahkan    |")
        print("+===========================+")
    else:
        print("+===========================+")
        print("|    Pilihan Tidak Valid    |")
        print("+===========================+")


while True:
    print("+==========================+")
    print("Menu Pengaduan Masyarakat : ")
    print("1. Tambah Laporan")
    print("2. Tampilkan Laporan")
    print("3. Update Laporan")
    print("4. Hapus Laporan")
    print("5. Keluar")
    print("+==========================+")

    pilihan = input("Pilih menu (1-5) : ")

    if pilihan == '1':
        cls()
        input_laporan()
    elif pilihan == '2':
        cls()
        laporan.read_laporan()

        print('1. Sort by Judul Laporan (Ascending)')
        print('2. Sort by Judul Laporan (Descending)')
        print('3. Sort by Pelapor (Ascending)')
        print('4. Sort by Pelapor (Descending)')
        pilihan_read = input('Pilih Jenis Sort (1-4) (Enter Untuk Keluar) : ')
        cls()

        if pilihan_read == '1':
            laporan_data = []
            current_node = laporan.head
            while current_node:
                laporan_data.append([current_node.id_laporan, current_node.pelapor, current_node.judul_laporan, current_node.isi_laporan, current_node.tanggal_laporan])
                current_node = current_node.next

            laporan.merge_sort_asc_judul_laporan(laporan_data)
            laporan.update_sorted_data(laporan_data)
            cls()
            laporan.read_laporan()

        elif pilihan_read == '2':
            laporan_data = []
            current_node = laporan.head
            while current_node:
                laporan_data.append([current_node.id_laporan, current_node.pelapor, current_node.judul_laporan, current_node.isi_laporan, current_node.tanggal_laporan])
                current_node = current_node.next

            laporan.merge_sort_desc_judul_laporan(laporan_data)
            laporan.update_sorted_data(laporan_data)
            cls()
            laporan.read_laporan()

        if pilihan_read == '3':
            laporan_data = []
            current_node = laporan.head
            while current_node:
                laporan_data.append([current_node.id_laporan, current_node.pelapor, current_node.judul_laporan, current_node.isi_laporan, current_node.tanggal_laporan])
                current_node = current_node.next

            laporan.merge_sort_asc_pelapor(laporan_data)
            laporan.update_sorted_data(laporan_data)
            cls()
            laporan.read_laporan()
        
        elif pilihan_read == '4':
            laporan_data = []
            current_node = laporan.head
            while current_node:
                laporan_data.append([current_node.id_laporan, current_node.pelapor, current_node.judul_laporan, current_node.isi_laporan, current_node.tanggal_laporan])
                current_node = current_node.next

            laporan.merge_sort_desc_pelapor(laporan_data)
            laporan.update_sorted_data(laporan_data)
            cls()
            laporan.read_laporan()
            
    elif pilihan == '3':
        cls()
        while True:
            laporan.read_laporan()
            print("+=======================================+")
            id_laporan = int(input("Masukkan ID Laporan yang akan diupdate : "))
            if laporan.laporan_detail(id_laporan):
                judul_baru = input("Masukkan Judul Baru : ")
                isi_baru = input("Masukkan Isi Baru : ")
                laporan.update_laporan(id_laporan, judul_baru, isi_baru)
                break
            else:
                cls()
                print("+==========================================+")
                print("|    Laporan Tidak Ditemukan, Coba Lagi    |")
                print("+==========================================+")

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
                print("+=======================+")
                print("1. Hapus di awal (head)")
                print("2. Hapus di tengah-tengah")
                print("3. Hapus di akhir (tail)")
                print("+=======================+")

                pilihan_hapus = input("Pilih tempat penghapusan (1-3): ")

                if pilihan_hapus == '1':
                    laporan.delete_head()
                elif pilihan_hapus == '2':
                    laporan.read_laporan()
                    print("+=================================+")
                    posisi_hapus = input("Masukkan posisi yang akan dihapus: ")
                    laporan.delete_between(int(posisi_hapus))
                elif pilihan_hapus == '3':
                    laporan.delete_tail()
                else:
                    print("+==========================================+")
                    print("|    Pilihan Tidak Ditemukan, Coba Lagi    |")
                    print("+==========================================+")
            else:
                cls()
                print("+==========================================+")
                print("|    Laporan Tidak Ditemukan, Coba Lagi    |")
                print("+==========================================+")
    elif pilihan == '5':
        cls()
        print("+==============+")
        print("|    Keluar    |")
        print("+==============+")
        break
    else:
        print("+==============================================+")
        print("|    Pilihan tidak valid, silakan coba lagi    |")
        print("+==============================================+")