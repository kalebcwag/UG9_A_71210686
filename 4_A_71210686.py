#membuat aplikasi kasir
#menghitung total harga

#variabel
hi=25000
he=6000
hr=8000

#proses
print("="*5,"MASUKKAN JUMLAH MAKANAN YANG DIPESAN","="*5)
i=int(input("IKAN BAKAR Rp 25.000,00    :"))
e=int(input("ES DOGER Rp 6.000,00       :"))
r=int(input("RUJAK CINGUR Rp 8.000,00   :"))

toti=hi*i
tote=he*e
totr=hr*r

print("="*5,"TOTAL","="*5)
print("TOTAL IKAN BAKAR     : Rp",toti)
print("TOTAL ES DOGER       : Rp",tote)
print("TOTAL RUJAK CINGUR   : Rp",totr)
print("Jumlah total biaya yang harus dibayar adalah Rp",(toti+tote+totr))
