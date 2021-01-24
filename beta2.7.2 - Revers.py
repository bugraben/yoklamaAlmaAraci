import time
import datetime as dt
import numpy as np
import os

print("Buğra'nın Gelişmiş Yoklama Alma Aracı v2.7.2\n\n")





tarih = dt.datetime.now()

tarihstr = str(tarih.strftime("%m")) + str(tarih.strftime("%d"))

dosya = input("Yoklamanın kaydedileceği dosya adını yaz: ") + tarihstr + ".txt"

yoklamakayit = open(dosya,"a")

log = open("log.txt", "a")

# logyolu = (".\log\%s" %tarihstr)






duzeltici = {
    "brsu" : "bersu",
    "bsru" : "bersu",
    "berus" : "bersu",
    "bersy" : "bersu",
    "glsu" : "gülsu",
    "gülu" : "gülsu",
    "güls" : "gülsu",
    "münevveer" : "münevver",
    "mün" : "münevver",
    "mğnevver" : "münevver",
    "yiği" : "yiğit",
    "zeynep t" : "zeynep",
    }


sozluk = {
    "ahmet" : "Ahmet Burak Kumcu 131",
    "arda" : "Arda Bolat 132",
    "öykü" : "Azra Öykü Uğur 133",
    "bersu" : "Bersu Özlü 134",
    "beyza" : "Beyza Nur Balta 135",
    "canan" : "Canan Pazarbaşı 136",
    "duru" : "Duru Çamcı 137",
    "eda" : "Edanur Şensiz 138",
    "efe" : "Efe Kızılabdullah 139",
    "efekan" : "Efekan Gülcan 140",
    "elif" : "Elif Gülsüm Koç 141",
    "cavit" : "Enes Cavit Çelik 142",
    "feyza" : "Feyza Yıldız 143",
    "haktan" : "Haktan Başkal 144",
    "buğra" : "İsmail Buğra Işıkdemir 145",
    "mahmut" : "Mahmut Emre Ataç 146",
    "mehmet" : "Mehmet Çetin 147",
    "münevver" : "Münevver Fatma Yaşar 148",
    "gülsu" : "Necla Gülsu Değer 149",
    "rüya" : "Rüya Kayacan 150",
    "samet" : "Samet Çınarcıklıoğlu 151",
    "ülkü" : "Ülkü Öztürk 152",
    "yalın" : "Yalın Salcı 153",
    "yiğit" : "Yiğit Dökmeci 154",
    "yunus d" : "Yunus Emre Demiryapan 155",
    "yunus s" : "Yunus Emre Sert 156",
    "yusuf" : "Yusuf Yastı 157",
    "eylül" : "Zeynep Eylül Çiçek 158",
    "sare" : "Zeynep Sare Kahvecioğlu 159",
    "zeynep" : "Zeynep Topraktapar 160"
}


duzelticikeylist = list(duzeltici.keys())
sozlukliste = list(sozluk.values())
sozlukkeylist = list(sozluk.keys()) 





mode = input("revers? ")
ciktiliste = []
kisi = ""

while kisi != "son":
    kisi = ((input("> ")).strip(" "))
    if kisi in duzelticikeylist:
        kisi = duzeltici[kisi]
    if kisi in sozlukkeylist:
        kisi = sozluk[kisi]
        if ciktiliste.count(kisi) == 0:
            ciktiliste.append(kisi)
    elif kisi != "son":
        kisi = kisi + "\n"
        log.write(kisi)

if mode != "r":
    ciktiliste = np.setdiff1d(sozlukliste, ciktiliste)

gelmeyensayi = len(ciktiliste)

if gelmeyensayi == 0:
    yoklamakayit.write("KATILIM TAM :))")
    print("KATILIM TAM :))")

print("\n \n ---- \n")

for x in ciktiliste:
    print(x)
    x = x + "\n"
    yoklamakayit.write(x)

yoklamakayit.write("-----%s\n" % gelmeyensayi)
log.write("\n!!!\n")

time.sleep(3)

print("\n\nYoklama %s isimli dosyaya kaydedildi. İyi günler." %dosya)

time.sleep(4)