# NAMA  : ANJAS BUDI PRASTIYO
# NIM   : 2270231017
# KELAS : P2K

print("*****TOKO SPAREPART MOTOR CB,GL,MP,TIGER*****")
print("\n")
sparepart = {
    "Shock TigerRevo Ori":1100000,
    "Shock NinjaRR/R PNP":1700000,
    "Sein Palu Kotak CB,GL":275000,
    "Ban FDR MP27  90/80":480000,
    "Ban Corsa R46 90/80":380000,
    "Oli Enduro4T Racing":55000,
    "Lampu Daymaker 5,75in":750000
}
for i in sparepart:
    print("Daftar: ", i,"\t Harga: ",sparepart[i])
print("+++Pembelian di atas Rp2.500.000 diskon 30%+++")
print("FORMAT PEMESANAN MOHON DI ISI BOS :)")
nama_pelanggan = input("Nama: ")
alamat = input("Alamat: ")
no = input("No Telfon: ")
beli = input("Nama Barang: ")
Jumlah = int(input("Jumlah Pembelian: "))
bayar = Jumlah*sparepart[beli]
if bayar > 2500000:
    diskon = bayar * 30/100
    total = bayar - diskon
else:
    total = bayar
print("\n")

print("= = = = = = = RINCIAN PESANAN SPAREPART = = = = = = =")
print("Nama Pemesan                                 :",nama_pelanggan)
print("Alamat Pemesan                               :",alamat)
print("Nomer telfon                                 :",no)
print("Sparepart yang dipilih                       :",beli)
print("Jumlah Barang                                :",Jumlah)
print("Total Pembayaran                             : Rp.",bayar)
print("Total Keseluruhan dengan diskon/tanpa diskon : Rp.",total)
import datetime as dt
hari_ini = dt.date.today()
print("Tanggal Pembelian                            :",hari_ini)
print("\n")
print("PEMBAYARAN KE REK. BNI 1174764595")
print("A/N ANJAS BUDI PRASTIYO")
print("T E R I M A  K A S I H")