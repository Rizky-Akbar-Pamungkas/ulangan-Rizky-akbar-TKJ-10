jumlah_pembeli = int(input("Masukkan jumlah pembeli tiket:"))
total = 0
for i in range(jumlah_pembeli):
    print(f"\nPembeli ke-{i + 1}:")
    
    usia = int(input("Masukkan usia:"))
    jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli:"))
       
    if usia < 12:
        harga_per_tiket = 30000
    elif 12 <= usia <= 60:
        harga_per_tiket = 50000
    else:
        harga_per_tiket = 35000

       
    total_harga_tiket = harga_per_tiket * jumlah_tiket
    total_harga = total_harga_tiket
    total = total + total_harga_tiket

    
    print(f"Harga total harga tiket pembeli{i + 1}: Rp {total_harga}")

print(f"total seluruh  harga tiket = {total}")