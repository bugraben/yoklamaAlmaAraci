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
    "ahmet" : "Ahmet Berke Kumcuoğlu 131",
    "arda" : "Arda Alemdar 132",
    "öykü" : "Afife Öykü İpekçi 133",
    "bersu" : "Bersu Nil Özden 134",
    "beyza" : "Beyza Jale Oduncu 135",
    "canan" : "Canan Beypazarlı 136",
    "duru" : "Duru Camcıgil 137",
    "eda" : "Eda Şenses 138",
    "efe" : "Efe Abdullahoğlu 139",
    "efekan" : "Efekan Gülden 140",
    "elif" : "Elif Koçhisarlı 141",
    "cavit" : "Cavit Efe Çelikten 142",
    "feyza" : "Feyza Nur Çiftçi 143",
    "haktan" : "Haktan Başbuğ 144",
    "bugra" : "bugra",
    "mahmut" : "Mahmut Yakup Aracı 146",
    "mehmet" : "Mehmet Cevizci 147",
    "münevver" : "Münevver Aydın 148",
    "gülsüm" : "Gülsüm Değerli 149",
    "rüya" : "Rüya Kayaoğlu 150",
    "samet" : "Ali Samet Gözgören 151",
    "ülkü" : "Ülkü Gül Özden 152",
    "yalın" : "Yalın Ahmet Savcı 153",
    "kemal" : "Kemal Dökmeciler 154",
    "yunus" : "Yunus Demirdöven 155",
    "emre" : "Emre Serter 156",
    "yusuf" : "Yusuf Yüncü 157",
    "eylül" : "Eylül Defterdar 158",
    "sare" : "Sare Kahvecigil 159",
    "zeynep" : "Zeynep Topraktarlar 160"
}

# bu harika program elbette bir hata tolerans mekanizması içeriyor. mekanizmanın çalışması için hata düzeltme girdilerine ihtiyacımız var

duzeltici = {
    "brsu" : "bersu",
    "bsru" : "bersu",
    "berus" : "bersu",
    "bersy" : "bersu",
    "glsü" : "gülsüm",
    "gülü" : "gülsüm",
    "güls" : "gülsüm",
    "münevveer" : "münevver",
    "mün" : "münevver",
    "mğnevver" : "münevver",
    "yiği" : "kemal",
    "zeynep t" : "zeynep",
    "yiğit": "kemal",
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