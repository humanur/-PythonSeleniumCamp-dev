ogrenciListesi = []

#listeye öğrenci ekle

def yeniOgrenciEkle():
  ad = input("Öğrenci adını giriniz: ")
  soyad = input("Öğrenci soyadını giriniz: ")
  adSoyad = ad + " " + soyad
  ogrenciListesi.append(adSoyad)
yeniOgrenciEkle()
print(ogrenciListesi)

#listeden öğrenci kaldır

def ogrenciSil():
  ad = input("Öğrenci adını giriniz: ")
  soyad = input("Öğrenci soyadını giriniz: ")
  adSoyad = ad + " " + soyad
  ogrenciListesi.remove(adSoyad)
ogrenciSil()
print(ogrenciListesi)

#Listeye birden fazla öğrenci ekle

def cokluOgrenciEkleme():
    sayi = int(input("Eklenecek öğrenci sayısı: "))
    
    for i in range(sayi):
        ogrenciEkle()
cokluOgrenciEkleme()
print(ogrenciListesi)

#Listeden birden fazla öğrenci sil

def cokluOgrenciSilme():
    i=0
    silinecekOgrenciSayisi = int(input("Silinecek öğrenci sayısı: "))
    while(i<=silinecekOgrenciSayisi):
        i=i+1
        silinenOgrenciNumarasi = int(input("Öğrenci numarasını gir: "))
        ogrenciListesi.remove(ogrenciListesi[silinenOgrenciNumarasi])
cokluOgrenciSilme()
print(ogrenciListesi)

#Listedeki tüm öğrencileri tek tek ekrana yazdır

def ogrenciListele():
    for i in range(len(ogrenciListesi)):
        print(students[i])
ogrenciListele()

#Öğrenci numarasını öğren

def ogrenciNumarasi():
    arananOgrenci = input("Öğrenci adı-soyadı: ")
    for i in range(len(ogrenciListesi)):
      if ogrenciListesi[i] == arananOgrenci: 
        print(i)
ogrenciNumarasi()

