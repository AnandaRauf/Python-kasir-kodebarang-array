print("---------------------------------------------\n")

nameprogram = "Online Store Computer"

print("---------------------------------------------\n")

print("List product Online Store Computer :\n")
print("\nKategori \t\tKode Barang \tDeskripsi \t\t\tHarga($)")
print("Kasus \t\t\tA1 \t\tKompak \t\t\t\t$75.00")
print("Kasus \t\t\tA2 \t\tMenara \t\t\t\t$150.00")
print("RAM \t\t\tB1  \t\t8 GB \t\t\t\t$79.99")
print("RAM \t\t\tB2 \t\t16 GB \t\t\t\t$149.99")
print("RAM \t\t\tB3 \t\t32 GB \t\t\t\t$299.99")
print("Drive Hard Disk Utama \tC1 \t\tHDD 1TB \t\t\t$49.99")
print("Drive Hard Disk Utama \tC2 \t\tHDD 2TB \t\t\t$89.99")
print("Drive Hard Disk Utama \tC3 \t\tHDD 4TB \t\t\t$129.99")
print("Solid State Drive \tD1 \t\tSSD 240 GB \t\t\t$59.99")
print("Solid State Drive \tD2 \t\tSSD 480 GB \t\t\t$119.99")
print("Drive Hard Disk Kedua \tE1 \t\tHDD 1TB \t\t\t$49.99")
print("Drive Hard Disk Kedua \tE2 \t\tHDD 2TB \t\t\t$89.99")
print("Drive Hard Disk Kedua \tE3 \t\tHDD 4TB \t\t\t$129.99")
print("Drive Optik \t\tF1 \t\tPemutar DVD/Blu-Ray \t\t$50.00")
print("Drive Optik \t\tF2 \t\tPenulis Ulang DVD/Blue-Ray \t$100.00")
print("Sistem Operasi \t\tG1 \t\tVersi Standar \t\t\t$100.00")
print("Sistem Operasi \t\tG2 \t\tVersi Profesional \t\t$175.00")

#Tugas 1
class Menu():
    def menu():
        print("\nMenu Online Store Computer:\n")
        print
        cat = ["Kasus"],["RAM"],["Drive Hard Disk Utama"],["Solid State Drive"],["Drive Hard Disk Kedua"],["Drive Optik"],["Sistem Operasi"]
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        

        print("1.Kategori,Kode barang,Deskripsi,Harga :",cat[0],kodebarang[0],desc[0],harga[0])
        print()
        print("2.Kategori,Kode barang,Deskripsi,Harga :",cat[0],kodebarang[1],desc[1],harga[1])
        print("3.Kategori,Kode barang,Deskripsi,Harga :",cat[1],kodebarang[2],desc[2],harga[2])
        print("4.Kategori,Kode barang,Deskripsi,Harga :",cat[1],kodebarang[3],desc[3],harga[3])
        print("5.Kategori,Kode barang,Deskripsi,Harga :",cat[1],kodebarang[4],desc[4],harga[4])
        print("6.Kategori,Kode barang,Deskripsi,Harga :",cat[2],kodebarang[5],desc[5],harga[5])
        print("7.Kategori,Kode barang,Deskripsi,Harga :",cat[2],kodebarang[6],desc[6],harga[6])
        print("8.Kategori,Kode barang,Deskripsi,Harga :",cat[2],kodebarang[7],desc[7],harga[7])
        print("9.Kategori,Kode barang,Deskripsi,Harga :",cat[3],kodebarang[8],desc[8],harga[8])
        print("10.Kategori,Kode barang,Deskripsi,Harga :",cat[3],kodebarang[9],desc[9],harga[9])
        print("11.Kategori,Kode barang,Deskripsi,Harga :",cat[4],kodebarang[10],desc[5],harga[10])
        print("12.Kategori,Kode barang,Deskripsi,Harga :",cat[4],kodebarang[11],desc[6],harga[11])
        print("13.Kategori,Kode barang,Deskripsi,Harga :",cat[4],kodebarang[12],desc[7],harga[12])
        print("14.Kategori,Kode barang,Deskripsi,Harga :",cat[5],kodebarang[13],desc[10],harga[13])
        print("15.Kategori,Kode barang,Deskripsi,Harga :",cat[5],kodebarang[14],desc[11],harga[14])
        print("16.Kategori,Kode barang,Deskripsi,Harga :",cat[6],kodebarang[15],desc[12],harga[15])
        print("17.Kategori,Kode barang,Deskripsi,Harga :",cat[6],kodebarang[16],desc[13],harga[16])
        
    # tugas 2 dan tugas 3 :
class Kasus1():
    def kasus1(self):
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[0])
        print("Deskripsi:",desc[0])
        print("Harga:",harga[0])
        hargabarang = 75.00
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
                         disc = 5 / 100
        elif jumlahbeli<=1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)

class Kasus2():
    def kasus2(self):
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[1])
        print("Deskripsi:",desc[1])
        print("Harga:",harga[1])
        hargabarang = 150.00
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli<=1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)

class RAM1():
    def ram1(self):
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[2])
        print("Deskripsi:",desc[2])
        print("Harga:",harga[2])
        hargabarang = 79.99
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli==1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)

class RAM2():
    def ram2(self):
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[3])
        print("Deskripsi:",desc[3])
        print("Harga:",harga[3])
        hargabarang = 149.99
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli==1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total) 

class RAM3():
    def ram3(self):
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[4])
        print("Deskripsi:",desc[4])
        print("Harga:",harga[4])
        hargabarang = 299.99
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli<=1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total :",total)

class DriveHarddiskUtama1():
    def driveharddiskutama1(self):
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[5])
        print("Deskripsi:",desc[5])
        print("Harga:",harga[5])
        hargabarang = 49.99
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 10 / 100
        elif jumlahbeli<=1:
            disc = 5 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)

class DriveHarddiskUtama2():
    def driveharddiskutama2(self):
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[6])
        print("Deskripsi:",desc[6])
        print("Harga:",harga[6])
        hargabarang = 89.99
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli<=1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total) 

class DriveHarddiskUtama3():
    def driveharddiskutama3(self):
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[7])
        print("Deskripsi:",desc[7])
        print("Harga:",harga[7])
        hargabarang = 129.99
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli<=1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)

class Solid1():
    def solid1(self):
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[8])
        print("Deskripsi:",desc[8])
        print("Harga:",harga[8])
        hargabarang = 59.99
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli<=1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)
class Solid2():
    def solid2(self):
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[9])
        print("Deskripsi:",desc[9])
        print("Harga:",harga[9])
        hargabarang = 119.99
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli<=1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)

class DriveHardkedua1():
    def drivehardkedua1():
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[10])
        print("Deskripsi:",desc[5])
        print("Harga:",harga[10])
        hargabarang = 49.99
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli==1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)

class DriveHardkedua2():
    def drivehardkedua2():
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[11])
        print("Deskripsi:",desc[6])
        print("Harga:",harga[11])
        hargabarang = 89.99
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli==1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)
class DriveHardkedua3():
    def drivehardkedua3():
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[12])
        print("Deskripsi:",desc[7])
        print("Harga:",harga[12])
        hargabarang = 129.99
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli==1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)

class DriveOptik1():
    def driveoptik1():
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[13])
        print("Deskripsi:",desc[10])
        print("Harga:",harga[13])
        hargabarang = 50.00
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli==1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)

class DriveOptik2():
    def driveoptik2():
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[14])
        print("Deskripsi:",desc[11])
        print("Harga:",harga[14])
        hargabarang = 100.00
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli<=1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)


class SistemOperasi1():
    def sistemoperasi1():
        kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
        desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
        harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
        print("Kode barang:",kodebarang[15])
        print("Deskripsi:",desc[12])
        print("Harga:",harga[15])
        hargabarang = 100.00
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli<=1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)

class SistemOperasi2():
    kodebarang = ["A1"],["A2"],["B1"],["B2"],["B3"],["C1"],["C2"],["C3"],["D1"],["D2"],["E1"],["E2"],["E3"],["F1"],["F2"],["G1"],["G2"]     
    desc = ["Kompak"],["Menara"],["8 GB"],["16 GB"],["32 GB"],["HDD 1TB"],["HDD 2TB"],["HDD 4TB"],["SSD 240 GB"],["SSD 480 GB"],["Pemutar DVD/Blu-Ray"],["Penulis Ulang DVD/Blue-Ray"],["Versi Standar"],["Versi Profesional"]
    harga = ["$75.00"],["$150.00"],["$79.99"],["$149.99"],["$299.99"],["$49.99"],["$89.99"],["$129.99"],["$59.99"],["$119.99"],["$49.99"],["$89.99"],["$129.99"],["$50.00"],["$100.00"],["$100.00"],["$175.00"]
    def sistemoperasi2():
        print("Kode barang:",kodebarang[16])
        print("Deskripsi:",desc[13])
        print("Harga:",harga[16])
        hargabarang = 175.00
        jumlahbeli = int(input("Masukan jumlah beli:"))
        if jumlahbeli>=2:
           disc = 5 / 100
        elif jumlahbeli==1:
            disc = 10 /10
        total = hargabarang * jumlahbeli * disc
        print("Total semua sudah termasuk diskon :",total)

Menu.menu()
pilih = int(input("Pilih yang akan mau dibeli:"))
ks1 = Kasus1()
ks2 = Kasus2()
ra1 = RAM1()
ra2 = RAM2()
ra3 = RAM3()
dhu1 = DriveHarddiskUtama1()
dhu2 = DriveHarddiskUtama2()
dhu3 = DriveHarddiskUtama3()
sl1 = Solid1()
sl2 = Solid2()
dhk1 = DriveHardkedua1()
dhk2 = DriveHardkedua2()
dhk3 = DriveHardkedua3()
do1 = DriveOptik1()
do2 = DriveOptik2()
so1 = SistemOperasi1()
so2 = SistemOperasi2()

if pilih==1:
            ks1.kasus1()
elif pilih==2:
    ks2.kasus2()
elif pilih==3:
    ra1.ram1()
elif pilih==4:
    ra2.ram2()
elif pilih==5:
    ra3.ram3()
elif pilih==6:
    dhu1.driveharddiskutama1()
elif pilih==7:
    dhu2.driveharddiskutama2()
elif pilih==8:
    dhu3.driveharddiskutama3()
elif pilih==9:
    sl1.solid1()
elif pilih==10:
    sl2.solid2()
elif pilih==11:
    dhk1.drivehardkedua1()
elif pilih==12:
    dhk2.drivehardkedua2()
elif pilih==13:
    dhk3.drivehardkedua3()
elif pilih==14:
    dol1 = driveoptik1()
elif pilih==15:
    dol2 = driveoptik2()
elif pilih==16:
    sol1.sistemoperasi1()
elif pilih==17:
    sol2.sistemoperasi2()
else:
    exit()
    
    
    

        


    
