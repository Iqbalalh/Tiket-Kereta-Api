import random
import colorama
from colorama import Fore

nama = str (input("Masukkan Nama Anda : "))
print("")

def TUJUAN():
    tujuan = ["1. Bekri","2. Kota Bumi", "3. Baturaja", "4. Palembang"]
    print('Pilih Destinasi : ')
    for i in tujuan:
        print(i)
    try:
        print('')
        x = int(input("Masukkan Pilihan : "))
        if x == 1:
            tujuan = 1
        elif x == 2:
            tujuan = 2
        elif x == 3:
            tujuan = 3
        elif x == 4:
            tujuan = 4
        else:
            TUJUAN()
    
    except :
        print('Silakan pilih 1 - 3')
        TUJUAN()
    
    return tujuan

while True:
    print('Silakan pilih 1 - 3')
    tuju = TUJUAN()
    if tuju == 1 or tuju == 2 or tuju == 3 or tuju == 4:
        break

print("")


def KELAS():
    kelas = ["1. KA Seminung", '2. KA Kualastabas']
    print('Pilih Kelas : ')
    for i in kelas:
        print(i)
    try:
        print('')
        x = int(input("Masukkan Pilihan : "))
        if x == 1:
            kelas = 1
        elif x == 2:
            kelas = 2
        else:
            print('Kelas yang anda pilih tidak tersedia')
            KELAS()
    
    except :
        print('Silahkan pilih 1 atau 2')
        KELAS()
            
    return kelas

while True:
    print('Silahkan pilih 1 atau 2')
    kls = KELAS()
    if kls == 1 or kls == 2:
        break

tiket = int(input("Masukkan Jumlah Tiket : "))
batita = int(input("Masukkan jumlah penumpang kurang dari 3 tahun : "))
print(Fore.RED + "Keterangan : Batita tetap akan mendapatkan tiket, tetapi tidak perlu membayar")

if tuju==1:
    if kls == 1:
           jam = "9.20"
    elif kls == 2:
            jam= "11.10"
elif tuju == 2:
    if kls == 1:
           jam = "13.30"
    elif kls == 2:
            jam = "15.30"
elif tuju == 3:
    if kls == 1:
           jam = "17.00"
    elif kls == 2:
            jam = "19.00"
elif tuju == 4:
    if kls == 1:
            jam = "21.00"
    else:
            jam = "21.00"

if tuju == 1:
    destination = 'Labuhan Ratu - Bekri'
elif tuju == 2:
    destination = 'Labuhan Ratu - Kotabumi'
elif tuju == 3:
    destination = 'Labuhan Ratu - Baturaja'
else:
    destination = 'Labuhan Ratu - Palembang'

if kls == 1:
    clas = "KA Seminung"
else:
    clas = "KA Kualastabas"
    
if destination == 'Labuhan Ratu - Bekri' and clas == "KA Seminung":
    harga = 10_000
elif destination == 'Labuhan Ratu - Kota Bumi' and clas == "KA Seminung":
    harga = 10_000
elif destination == 'Labuhan Ratu - Baturaja' and clas == "KA Kualastabas":
    harga = 60_000
elif destination == 'Labuhan Ratu - Palembang' and clas == "KA Kualastabas":
    harga = 180_000
else:
    harga = 30_000

    
print(Fore.GREEN + "------------------------------------------------")
print("PT. Kereta API Indonesia - Stasiun Labuhan Ratu")
print("Kode Pemesanan Tiket : ", random.randint(1000,9999))
print("Nama Pemesan         : ", nama.upper())
print("Destinasi Tujuan     : ", destination)
print("Jam Keberangkatan    : ", jam, 'WIB')
print('Kelas KAI            : ', clas)
print('Harga Tiket          :  Rp.',f'{harga:,}')
print('Jumlah Tiket         : ', tiket)
print('Admin                : ', '30%')
print('Total Harga          :  Rp.',f'{(tiket) * (harga + (harga*(3/10))):,}' )
print('--------------------------------------------------')
