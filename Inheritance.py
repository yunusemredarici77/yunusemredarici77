#INHERITENCE(kalıtım)  , bir nesne olusturdugumuzda bu nesneden yeni altnesne olusturmamızı saglamaya yarar
#bizim calısan sınıfımızda calısanlarımız developer altclassı ekliyoruz.
 
class calisan(): # ÖNEMLİ!! ,  eger calısan sınıfına yeni altsınıflar ekleyeceksek(developer sınıfı gibi,ozaman calısan classına parantez() ekliyoruz. 
    katsayı = 5
    zam_orani = 1.05
    personel_say = 0
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
        calisan.personel_say = calisan.personel_say + 1    #personel sayısı olusturmus oldugumuz nesnelerden bagımsız olacaktır 
    def tamad(self):
        return "adı : {}   soyad : {}".format(self.ad,self.soyad)
    def arttir(self):
        self.maas=(self.maas*self.zam_orani) #burayı zam_orani degiskeniyle yazmak istersek 
        
class developer(calisan): #developer sınıfı calısan sınıfından türettik.Yani developer sınıfı calısan sınıfının altclassıdır.  
    pass
                
personel1 = calisan("ismail","bulut",1121)
personel2 = calisan("kerim","bakir",1950)
"""dev1 = developer("mehmet","senel",2750,"python")  """#biz bu gelistiriciye 3 özellikten(ad,soyad,maas) baska extradan farklı bir özellik (programlama dili) ekliyoruz
#bu yuzden developer classında degisiklik yapmamız lazım
#print(dev1.tamad()) 

class developer(calisan):
    def __init__(self,ad,soyad,maas,p_dili):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
        calisan.per_say = calisan.personel_say + 1
        self.p_dili = p_dili
personel1 = calisan("ismail","bulut",1121)
personel2 = calisan("kerim","bakir",1950)        
dev1 = developer("mehmet","senel",2750,"python")
print(dev1.p_dili)        
        
#zaten bu özellikler vardı , şimdi kısaltma yapalım     
        
class developer(calisan):
    def __init__(self,ad,soyad,maas,p_dili):
        #calisan.__init__(self,ad,soyad,maas) #developerın özelliklerini verirken calısan classını kullanmıs olduk
        super().__init__(ad,soyad,maas) #calısan classı aslında developer classının super(parent) classıdır, birden fazla inheritance yaptıgımızda bu kullanım işimize yarar
        self.p_dili = p_dili
        self.zam_orani = 1.25

class manager(calisan):
    def __init__(self,ad,soyad,maas,calisanlar = None):    #ilk baska bu yöneticinin hic calısanı olmayabilir.Oyuzden biz None a eşitliyoruz. 
        super().__init__(ad,soyad,maas)
        if calisanlar is None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar
    def calisan_liste(self):
        for eleman in self.calisanlar:
            print(eleman.tamad())
    def eleman_ekle(self,eleman):
        self.calisanlar.append(eleman)
    def eleman_cikar(self,eleman):
        self.calisanlar.remove(eleman)        


             
personel1 = calisan("erhan","bulut",1121)
personel2 = calisan("kerim","bakir",1950)        
dev1 = developer("mehmet","senel",2750,"python")
print(dev1.tamad(),dev1.p_dili,dev1.maas)
dev1.arttir()
print(dev1.maas)  
dev2 = developer("sadi","seker",3250,"java")
print(dev2.tamad(),dev2.p_dili,dev2.maas)
dev2.arttir()
print(dev2.maas)              

manager1 = manager("ismail","solmaz",6500,[dev1,dev2,personel1])
manager1.calisan_liste()
print("****")
manager1.eleman_ekle(personel2)
manager1.calisan_liste()
print("****")
manager1.eleman_cikar(dev2)
manager1.calisan_liste()



#şimdi bir nesnenin bır sınıfa ait olup olmadıgını veya bir alt sınıfın bır ust sınıfa ait olup olmadıgını gösteren fonksiyonlar var şimdi onları görücez
print(isinstance(personel2,calisan))  #personel2 sınıfı calisan classına ait mi ? .True cevabı verir
print(isinstance(personel2,manager)) #false
#simdi altclass mı deil mi onu görcez
print(issubclass(manager,calisan)) #true
print(issubclass(developer,calisan))

 
                  
        
        
        
        
     

















   