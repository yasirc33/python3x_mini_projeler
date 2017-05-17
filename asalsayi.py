# Girilen değerler arasındaki sayıların hangilerinin asal sayı olduğunu bulma

deger = input("Kaça kadar ki asal sayıları arıyorsunuz? : ")
asal = []

for i in range(2, int(deger)):
    flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = True
            break
    if not flag:
        asal.append(i)

for i in asal:
    print (i)

print ("0 -",deger," arasında toplam",len(asal)," tane asal sayı vardır.")


@ysrclk
