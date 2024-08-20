def terbilang(angka):
    if angka < 2000:
        return "╰（‵□′）╯"

    if len(str(angka)) > 4:
        return '( ˘︹˘ )'


    kata_angka = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan", "Sepuluh", "Sebelas", "Dua Belas", "Tiga Belas", "Empat Belas", "Lima Belas", "Enam Belas", "Tujuh Belas", "Delapan Belas", "Sembilan Belas"]
    kata_puluhan = ["", "", "Dua Puluh", "Tiga Puluh", "Empat Puluh", "Lima Puluh", "Enam Puluh", "Tujuh Puluh", "Delapan Puluh", "Sembilan Puluh"]

    ribu = angka // 1000
    sisa_ribu = angka % 1000
    ratus = sisa_ribu // 100
    sisa_ratus = sisa_ribu % 100
    puluh = sisa_ratus // 10
    satuan = sisa_ratus % 10

    hasil = ""
    
    if ribu == 1:
        hasil += "Seribu "
    else:
        hasil += kata_angka[ribu] + " Ribu "

    if ratus == 1:
        hasil += "Seratus "
    elif ratus > 1:
        hasil += kata_angka[ratus] + " Ratus "

    if sisa_ratus < 20:
        hasil += kata_angka[sisa_ratus]
    else:
        hasil += kata_puluhan[puluh] + " " + kata_angka[satuan]

    return hasil.strip()

if __name__ == '__main__':
    x = 2234
    print(f'{x}: {terbilang(x)}')

    x = 8500
    print(f'{x}: {terbilang(x)}')

    x = 7777
    print(f'{x}: {terbilang(x)}')


    x = 1337
    print(f'{x}: {terbilang(x)}')

x = 11111
print(f'{x}: {terbilang(x)}')
