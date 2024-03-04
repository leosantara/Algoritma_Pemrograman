nama=input("Masukan nama lengkap Anda :")
tinggi=input("Masukan tinggi badan Anda (cm) :")
berat=input("Masukan berat badan Anda (kg) :")

print("Hallo,", nama.title() ,"!")
BMI=round(int(berat)/((int(tinggi)/100)**2),1)
print("Indeks masa tubuh (BMI) Anda adalah ", BMI)
if int(BMI<=18.5) :
    print("Anda termasuk ke dalam kategori kekurangan berat badan!")
elif int(BMI>18.5 and BMI<= 25):
    print("Anda termasuk ke dalam kategori berat badan ideal!")
elif int(BMI>25 and BMI<= 30):
    print("Anda termasuk ke dalam kategori kelebihan berat badan!")
else :
    print("Anda termasuk ke dalam kategori obesitas!")
