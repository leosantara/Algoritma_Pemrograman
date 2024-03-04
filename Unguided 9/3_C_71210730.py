#menghitung jumlah penggunaan sak semen dalam proses pembangunan rumah

#alas atas_1= a_1
#alas atas_1= 5
a_1=5
#tinggi atap_1= t_1
#tinggi atap_1=2
t_1=2
#tinggi tembok_1=s_1
#tinggi tembok_1=6
s_1=6

luas_1=(0.5*a_1*t_1)+(s_1**2)
sak_semen_1=luas_1/5
print("a. Test case 1: ")
print("masukan alas atap : ", a_1)
print("Masukan tinggi atap :", t_1)
print("Masukan tinggi tembok:",s_1)
print("rumah tersebut membutuhkan", sak_semen_1, "sak semen")

#alas atas_2= a_2
#alas atas_2= 8
a_2=8
#tinggi atap_2= t_2
#tinggi atap_2=10
t_2=10
#tinggi tembok_2=s_2
#tinggi tembok_2=16
s_2=16

luas_2=(0.5*a_2*t_2)+(s_2**2)
sak_semen_2=luas_2/5
print("a. Test case 2: ")
print("masukan alas atap : ", a_2)
print("Masukan tinggi atap :", t_2)
print("Masukan tinggi tembok:",s_2)
print("rumah tersebut membutuhkan", sak_semen_2, "sak semen")
