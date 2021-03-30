import time
import datetime as dt
import numpy as np
import os

# selam

# ben buğra

# bu da gelişmiş yoklama alma aracım 

print("Buğra'nın Gelişmiş Yoklama Alma Aracı v2.6.2\n\n")   

# ( •_•)
# ( •_•)>⌐■-■
# (⌐■_■)


#---------------------------------


# önce program için elzem olan tarih ve dosya erişim girdilerini tanımlayalım

tarih = dt.datetime.now()

tarihstr = str(tarih.strftime("%m")) + str(tarih.strftime("%d"))

dosya = input("Yoklamanın kaydedileceği dosya adını yaz: ") + tarihstr + ".txt"

yoklamakayit = open(dosya,"a")

log = open("log.txt", "a")





# şimdi yoklamayı alabilmesi için programımıza referans sınıf listesi tanımlıyoruz

sozluk = {
    "ahmet" : "Ahmet Berke Kumcuoğlu",
    "arda" : "Arda Alemdar",
    "öykü" : "Afife Öykü İpekçi",
    "bersu" : "Bersu Nil Özden",
    "beyza" : "Beyza Jale Oduncu",
    "canan" : "Canan Beypazarlı",
    "duru" : "Duru Candan",
    "eda" : "Eda Şenses",
    "efe" : "Efe Abdullahoğlu",
    "efekan" : "Efekan Gülden",
    "elif" : "Elif Koçhisarlı1",
    "cavit" : "Cavit Efe Çelikten",
    "feyza" : "Feyza Nur Çiftçi",
    "haktan" : "Haktan Başbuğ",
    "sef" : "sef",
    "mahmut" : "Mahmut Yakup Aracı",
    "mehmet" : "Mehmet Cevizci",
    "münevver" : "Münevver Aydın",
    "gülsüm" : "Gülsüm Değerli",
    "rüya" : "Rüya Kayaoğlu",
    "samet" : "Ali Samet Gözgören",
    "ülkü" : "Ülkü Gül Özden",
    "yalın" : "Yalın Ahmet Savcı",
    "kemal" : "Kemal Dökmeciler",
    "yunus" : "Yunus Demirdöven",
    "emre" : "Emre Serter",
    "yusuf" : "Yusuf Yüncü",
    "eylül" : "Eylül Defterdar",
    "sare" : "Sare Kahvecigil",
    "zeynep" : "Zeynep Topraktarlar"
}

# bu harika program elbette bir hata tolerans mekanizması içeriyor. mekanizmanın çalışması için hata düzeltme girdilerine ihtiyacımız var

duzeltici = {
    "brsu" : "bersu",
    "bsru" : "bersu",
    "berus" : "bersu",
    "bersy" : "bersu",
    "glsu" : "gülsum",
    "gülu" : "gulsum",
    "guls" : "gulsum",
    "munevveer" : "munevver",
    "mun" : "munevver",
    "mgnevver" : "munevver",
    "yigi" : "yigit",
    "zeynep t" : "zeynep",
    "yigit": "yigit",
    }


duzelticikeylist = list(duzeltici.keys())
sozlukliste = list(sozluk.values())
sozlukkeylist = list(sozluk.keys()) 



# işte asıl olayın *döndüğü* yer! 

gelenliste = []
kisi = ""

while kisi != "son":
    kisi = ((input("> ")).strip(" "))
    if kisi in duzelticikeylist:
        kisi = duzeltici[kisi]
    if kisi in sozlukkeylist:
        kisi = sozluk[kisi]
        if gelenliste.count(kisi) == 0:
            gelenliste.append(kisi)
    elif kisi != "son":
        kisi = kisi + "\n"
        log.write(kisi)



# ve son olarak çıktının üretilip kullanıcıya sunulması. yalnızca arkana yaslan

ciktiliste = np.setdiff1d(sozlukliste, gelenliste)

gelmeyensayi = len(ciktiliste)

if gelmeyensayi == 0:
    strTam= "KATILIM TAM" + "\n"
    print("\n" + strTam)
    yoklamakayit.write(strTam) 

print("\n \n ---- \n")

for x in ciktiliste:
    print(x)
    x = x + "\n"
    yoklamakayit.write(x)

yoklamakayit.write("-----%s\n" % gelmeyensayi)
log.write("\n!!!\n")

# ──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌ 
# ───▄▄██▌█      ~~ BEEP BEEP ~~
# ▄▄▄▌▐██▌█  ~~ YOKLAMA TESLİMATI ~~
# ███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌ 
# ▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀

time.sleep(3)

print("\n\nYoklama %s isimli dosyaya kaydedildi. İyi günler." %dosya)

time.sleep(4)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# destekleri için tüm kuş severler derneğine teşekkürler <3

# teşekkürler gülsu (ဖ‿ဖ)人(စ‿စ )

# yazı boyunca adı geçen kişi ve kurumların gerçek kişi ve kurumlarla kesinlikle hiçbir alakası yoktur!
