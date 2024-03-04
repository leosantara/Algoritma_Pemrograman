print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Kalkulator Volume Bangun Ruang")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Pilih bangun ruang yang ingin dihitung volumenya:")
print("1. Limas")
print("2. Bola")
print("3. KLerucut")
Limas=1
Bola=2
Kerucut=3
bangun=input("Masukan pilihan anda :")
if bangun=='1' :
    aLim=input("Masukan panjang sisi alas limas:")
    tLim=input("Masukan tinggi limas:")
    VLim=(int(aLim)**2)*int(tLim)/3
    print("Volume limas tersebut adalah", round(float(VLim),1))
elif bangun=='2' :
    rBol=input("Masukan panjang jari-jari bola:")
    phi1=3.14
    VBol=4/3*float(phi1)*(int(rBol)**3)
    print("Volume bola tersebut adalah", round(float(VBol),1))
elif bangun=='3' :
    rKer=input("Masukan jari-jari kerucut:")
    tKer=input("Masukan tinggi kerucut:")
    phi2=3.14
    VKer=float(phi2)*(int(rKer)**2)*int(tKer)/3
    print("Volume kerucut tersebut adalah", round(float(VKer),1))
else :
    print("Pilihan anda tidak tersedia di menu kalkulator ini")
