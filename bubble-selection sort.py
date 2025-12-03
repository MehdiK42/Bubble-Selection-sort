import time

# Dosyadaki sayıları oku
dosya = open("sayılar.txt", "r")
veri = dosya.read()
dosya.close()

# Metindeki sayıları listeye çevir
veri = veri.split()
sayilar = []
for x in veri:
    sayilar.append(int(x))

# Bubble Sort
liste1 = sayilar.copy()
bubble_adim = 0

basla = time.time()
for dış_döngü in range(len(liste1)):
    for iç_döngü in range(len(liste1)-1):
        bubble_adim = bubble_adim + 1
        if liste1[iç_döngü] > liste1[iç_döngü+1]:
            temp = liste1[iç_döngü]
            liste1[iç_döngü] = liste1[iç_döngü+1]
            liste1[iç_döngü+1] = temp
bitis = time.time()
bubble_sure = bitis - basla

# Selection Sort
liste2 = sayilar.copy()
selection_adim = 0

basla = time.time()
for dış_döngü in range(len(liste2)):
    en_kucuk = dış_döngü
    for iç_döngü in range(dış_döngü+1, len(liste2)):
        selection_adim = selection_adim + 1
        if liste2[iç_döngü] < liste2[en_kucuk]:
            en_kucuk = iç_döngü
    temp = liste2[dış_döngü]
    liste2[dış_döngü] = liste2[en_kucuk]
    liste2[en_kucuk] = temp
bitis = time.time()
selection_sure = bitis - basla

# Sonuçları rapor dosyasına yaz
rapor = open("rapor.txt", "w")

rapor.write("Orijinal liste: " + str(sayilar) + "\n\n")

rapor.write("BUBBLE SORT:\n")
rapor.write("Sıralı liste: " + str(liste1) + "\n")
rapor.write("Adım sayısı: " + str(bubble_adim) + "\n")
rapor.write("Süre: " + str(bubble_sure) + "\n\n")

rapor.write("SELECTION SORT:\n")
rapor.write("Sıralı liste: " + str(liste2) + "\n")
rapor.write("Adım sayısı: " + str(selection_adim) + "\n")
rapor.write("Süre: " + str(selection_sure) + "\n\n")

rapor.close()
