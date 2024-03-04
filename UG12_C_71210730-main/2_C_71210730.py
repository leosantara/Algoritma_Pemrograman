hari=input("Hi Momo, Silahkan Masukan hari yang ingin Anda telusuri:")
hari:[str.casefold ("senin"),str.casefold ("selasa"),str.casefold ("rabu"),str.casefold ("kamis"),str.casefold ("jumat"),str.casefold ("sabtu"),str.casefold("minggu")]
    if hari==str.lower("senin"): print("Hari senin Anda tidak ada kelas")
    elif hari== str.casefold ("selasa") :
        print("Kelas ke-2 Matematika Teknik")
        print("Kelas ke-4 Bhs Indonesia")
        print("Kelas ke-6 PKN")
    elif hari==str.casefold ("rabu") :
        print ("kelas ke-1 Riset Operasi")
        print("kelas ke-3 Sistem Operasi")
        print("kelas ke-5 Praktikum INLAN")
    elif hari==str.casefold ("kamis") :
        print("kelas ke-1 IMK")
        print("kelas ke-3 LogMat")
        print("kelas ke-4 Praktekkom")
    elif hari==str.casefold ("jumat") :
        print("kelas ke-2 Sistem Basis Data")
        print("kelas ke-4 Praktikum Sistem Basis Data")
        print("kelas ke-6 INLAN")
    elif hari==str.casefold ("sabtu"): print("Hari sabtu Anda tidak ada kelas")
    elif hari==str.casefold ("minggu"): print("Hari minggu Anda tidak ada kelas")


