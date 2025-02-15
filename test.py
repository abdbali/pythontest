#int TAM SAYI
#float 3.14
#str Metin
#list (Liste)
#dict (sözlük)

#Veri örnekleri
sayi = 14 #int
ondaliklisayi = 3.14,5.5,0.33,4.18,5.16 #float
metin = "Merhaba Dünya!" #"Hello World!" #str
liste = [1,2,3,4] #list
sozluk = {"Ad":"Elifnur","Yaş":"Aralıkta 13 ama 12"} #dict

print("Sayı:", type(sayi))
print("Ondalık Sayı:", type(ondaliklisayi))
print("Metin:", type(metin))
print("Liste:",type(liste))
print("Sözlük:", type(sozluk))

sinif = ["Hatice","Elif","Rabia","Zeynep","İkra","Belinay","Ayşe","Azra"]
print(sinif[2]) #3.sıradaki elaman
print(sinif[5]) #liste 0,1,2,.... şekilinde 0.elemandan başlayarak ilerler.
print(sinif[4])
print(sinif[3])
print(sinif[0])
print(sinif[-1])

sinif.append("Güven") #Listenin sonuna ekler.
sinif.insert(0,"Pis Sinek")
sinif.insert(3,"Speedy Mustafa")
sinif.insert(5, "Nutella")
sinif.insert(4,"Yıldız")
print(sinif)

sinif.remove("Pis Sinek")
sinif.remove("Yıldız")
sinif.remove("Nutella")
sinif.remove("Speedy Mustafa")
print(sinif)

silinen = sinif.pop() #Son elemanı siler ve yazdırır.
print("Silinen:", silinen)
print(sinif)

sinav_sonuclari = [98,64,67,60,83,55,47,54]
sinav_sonuclari.sort() #Küçükten büyüğe sıralama.
print("Sıralanmış Sınav Sonuçları:",sinav_sonuclari)

ara = int(input("Not sorgula:"))
if ara in sinav_sonuclari:
  print("Böyle bir sonuç var!")
else:
  print("Böyle bir sınav sonucu yok!")






