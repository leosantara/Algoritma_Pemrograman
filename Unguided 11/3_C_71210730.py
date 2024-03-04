def ambil_dan_sisipkan ():
    kata=input("masukan kalimat:")
    huruf1=input("Masukan Index 1:",)
    huruf2=input("Masukan Index 2:",)
    index1=kata[int(huruf1)-1]
    index2=kata[int(huruf2)-1]
    jumlah=str(kata+index1+index2)
    return jumlah
print (ambil_dan_sisipkan ())



