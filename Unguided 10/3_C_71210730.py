angka=input("Masukan angka:")
A="Bilangan tersebut habis dibagi 5 atau 3? Jawab : YA"
B="Apakah Bilangan tersebut juga habis dibagi 2 dan 4? Jawab : TENTU"
C="Apakah Bilangan tersebut juga habis dibagi 2 dan 4? Jawab : TIDAK"
D="Bilangan tersebut tidak habis dibagi 5 atau 3. Program dihentikan"
if int(angka)%5==0 or int(angka)%3==0 :print(A)
elif int(angka)%5!=0 or int(angka)%3!=0 : print(D), exit()
if int(angka)%2!=0 and int(angka)%4!=0 : print(C)
elif int(angka)%2==0 and int(angka)%4==0 : print(B)
else : ()






