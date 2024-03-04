kata=str(input("Input :"))
print("Output :")
satusatu = len(kata)
for huruf in range (satusatu) :
    for word in range (huruf+1):
        print(kata[word],end="")
    print()

#print("\n")
        
for huruf in range (satusatu, 0, -1) :
    for word2 in range (huruf):
        print(kata[word2],end="")
    print()
        

        
