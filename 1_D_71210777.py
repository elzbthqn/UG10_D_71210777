hrgmkn = int(input("Harga makanan sebesar Rp "))
hrgsnck = int(input("Harga snack sebesar Rp "))
hrgmnm = int(input("Harga minuman sebesar Rp "))
uang = int(input("Uang yang anda bawa sebesar Rp "))
hrgttl = hrgmkn+hrgsnck+hrgmnm

print("Total yang harus anda bayar sebesar Rp",hrgttl)
if uang == hrgttl:
    print("Uang anda pas! Tidak ada kembalian dan Utang :D")
elif uang < hrgttl:
    print("Uang Anda kurang! Anda memiliki utang sebesar Rp",hrgttl-uang)
else: 
    print("Anda memiliki kembalian sebesar Rp",uang-hrgttl)
    