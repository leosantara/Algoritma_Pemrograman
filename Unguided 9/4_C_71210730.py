#Menghitung jumlah suku ke-99 dari barisan aritmatika 3, 7, 11, ...
#a=bilangan pertama
#b=beda suku dengan suku setelah atau sebelumnya
#n=suku ke berapa

a=3
b=4
n=99

#cari menggunakan rumus sn
sn=(n/2)*(2*a+(n-1)*b)
print("Menghitung jumlah suku ke-99 dari barisan aritmatika 3, 7, 11, ...")
print("saya akan mencari menggunakan rumus sn")
print("Jumlah suku ke-99 adalah ", sn)
