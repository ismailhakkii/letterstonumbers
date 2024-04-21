from decimal import Decimal, getcontext

# Hassasiyet ayarı
getcontext().prec = 6

turkce_karakterler = {
    'i': 'İ',
    'ı': 'I'
}
harf_degerleri = {
    'A': Decimal('0.01'), 'B': Decimal('0.8'), 'C': Decimal('1.5'), 'Ç': Decimal('10'), 'D': Decimal('0.2'),
    'E': Decimal('0.05'), 'F': Decimal('5'), 'G': Decimal('25'), 'Ğ': Decimal('1'), 'H': Decimal('15'),
    'I': Decimal('0.1'),
    'İ': Decimal('0.04'), 'J': Decimal('0'), 'K': Decimal('0.09'), 'L': Decimal('0.02'), 'M': Decimal('0.07'),
    'N': Decimal('0.03'), 'O': Decimal('0.7'), 'Ö': Decimal('2'), 'P': Decimal('50'), 'R': Decimal('0.08'),
    'S': Decimal('0.5'), 'Ş': Decimal('0.6'), 'T': Decimal('0.06'), 'U': Decimal('0.9'), 'Ü': Decimal('0.3'),
    'V': Decimal('2.5'), 'Y': Decimal('0.4'), 'Z': Decimal('20')
}
def turkce_upper(metin):
    return "".join(turkce_karakterler.get(harf, harf.upper()) for harf in metin)

def harf_degerlerini_topla(girdi):
    girdi = turkce_upper(girdi)
    return sum(harf_degerleri.get(harf, Decimal('0')) for harf in girdi)


test_girdisi = input("Lütfen bir şey yazın: ")
toplam_deger = harf_degerlerini_topla(test_girdisi)
print(toplam_deger)
