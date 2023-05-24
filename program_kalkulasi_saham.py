import locale

def notasiKeuangan(jumlah):
    locale.setlocale(locale.LC_ALL, 'id_ID')
    konversi = locale.currency(jumlah, grouping=True)
    konversi = konversi.rstrip('0').rstrip(',')
    return konversi

def transaksiBeli(harga_per_lembar, jumlah_lot):
    saham = harga_per_lembar * 100
    biaya = saham * jumlah_lot
    komisi_broker = 0.0001 * biaya
    levy = 0.00043 * biaya
    PPN = 0.11 * komisi_broker
    return int(biaya + komisi_broker + levy + PPN)

def transaksiJual(harga_per_lembar, jumlah_lot):
    saham = harga_per_lembar * 100
    biaya = saham * jumlah_lot
    komisi_broker = 0.001 * biaya
    levy = 0.00043 * biaya
    PPN = 0.11 * komisi_broker
    PPH = 0.001 *biaya
    return int(biaya -(komisi_broker + levy + PPN + PPH))

# ======================= Main Program ==================================
harga_saham = int(input("Masukan Harga Saham Per Lembar: "))
jumlah_saham = int(input("Masukan Jumlah Lot: "))
perkiraan_biaya_beli = transaksiBeli(harga_saham, jumlah_saham)
perkiraan_biaya_jual = transaksiJual(harga_saham, jumlah_saham)

print(f"""
Kalkulasi perkiraan harga jual-beli saham pada platform Ajaib
Beli = {notasiKeuangan(perkiraan_biaya_beli)}
Jual = {notasiKeuangan(perkiraan_biaya_jual)}
""")
# ========================================================================