import random

desen=["Karo","Maça","Sinek","Kupa"]
rakam=list(range(1,14))

print("""

************************************
şans oyunlarına hoşgeldin

1. zar atmak
2. iskambil kağıdı seçmek
3. çıkış
************************************

""")

while True:
    secim=input("Seçiminiz: ")

    if secim=="3":
        print("Programı kullandığımız için teşekkürler...")
        break
    elif secim=="1":
        zar=random.randint(1,6)
        print("Zarı attım. Sonuç:",zar)
    elif secim=="2":
        renk=desen[random.randint(0,3)]
        sayi=rakam[random.randint(0,13)]
        if sayi==11:
            print("Kartı seçtim. Sonuç:",renk," Vale" )
        elif sayi==12:
            print("Kartı seçtim. Sonuç:", renk, " Kız")
        elif sayi==13:
            print("Kartı seçtim. Sonuç:", renk, " Papaz")
        elif sayi==1:
            print("Kartı seçtim. Sonuç:", renk, " As")
        else:
            print("Kartı seçtim. Sonuç:", renk,sayi)

    else:
        print("Hatalı giriş, tekrar deneyin!")
