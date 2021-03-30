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
    "glsu" : "gulsu",
    "gulu" : "gulsu",
    "guls" : "gulsu",
    "munevveer" : "munevver",
    "yigi" : "yigit",
    "zeynep" : "zeynep",
    }


sozluk = {
    "ahmet" : "Ahmet",
    "arda" : "Arda",
    "bersu" : "Bersu",
    "beyza" : "Beyza",
    "canan" : "Canan",
    "cavit" : "Cavit",
    "demiryapan" : "Demiryapan",
    "duru" : "Duru",
    "eda" : "Eda",
    "efe" : "Efe",
    "efekan" : "Efekan",
    "elif" : "Elif",
    "eylül" : "Eylul",
    "feyza" : "Feyza",
    "gulsu" : "Gulsu",
    "haktan" : "Haktan",
    "mahmut" : "Mahmut",
    "mehmet" : "Mehmet",
    "munevver" : "Munevver",
    "oyku" : "Oyku",
    "ruya" : "Ruya",
    "samet" : "Samet",
    "sare" : "Sare",
    "sert" : "Sert",
    "Ulku" : "Ulku",
    "yalın" : "Yalın",
    "yigit" : "Yigit",
    "yusuf" : "Yusuf",
    "zeynep" : "Zeynep"
    "sef" : "sef",
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
