#Menghitung jumlah kata tertentu yang muncul dalam sebuah kalimat
kalimat1='ibu membeli sayur di ibu tukang sayur'
kalimat2='kami suka rumnpi kami mau rumpi tapi sekarang kami merumpi'

print("a. Test case 1:")
print("Masukan kalimat: ", kalimat1)
print("Masukan kata untuk dihitung: ibu")
print("ada", kalimat1.count('ibu'), "buah kata ibu")

print("a. Test case 2:")
print("Masukan kalimat: ", kalimat2)
print("Masukan kata untuk dihitung: kami")
print("ada", kalimat2.count('kami'), "buah kata kami")
