# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:56:01 2023

@author: ACER DUMANLİVA27
"""

""" SUMMER HOLIDAY REPEAT"""


sayi = 10

deger = "4546313114"

name = "Livanur Nagihan"

soyName = "Duman"

floatSayi = 27.0

telefonNumarası = 5452245588

okuduguBolum = "Bilgisayar Mühendisliği"

name2 = name[14:15]

print(type(sayi))
print(type(floatSayi))
print(type(name))
print(okuduguBolum)
print(float(telefonNumarası))

print(name[14:15])
print(len(name))
print(name2)
name2 = name[len(name)-1:len(name)]
print(name2)
print(name.upper())
print(name.lower())
print(name.replace("a","e"))

bilgi = "Livanur;Nagihan;Duman;27;Gaziantep" .strip() 
print(bilgi.split())
print("Adı = " + bilgi.split(";")[0])

name = input("Lütfen adınızı giriniz:")

print("EXAMPLE:")
print("KM KAÇ MİL EDER?")

donusumOranı = 0.62137946
km = int(input("Kaç km?"))
mil = km * donusumOranı
print(str(km) + " Km =  " + str(mil) + " eder")

sehirler = ["Gaziantep","Hatay","Malatya","Kahramanmaraş"]
print(sehirler[0])
sehirler.append("Urfa")
sehirler.remove("Malatya")
print(sehirler)

print("TrafikIsiklariDemo")

lights = [">>red<<",">>yellow<<",">>green<<"]
currentlights = lights[1]

print(currentlights)

if currentlights == ">>red<<":
    print("STOP!")
elif currentlights == ">>yellow<<":
    print("READY!")
else:
    print("GO!")
    
    
print("POZİTİF Mİ NEGATİF Mİ?")

a = int(input("Bir a saysısı giriniz:"))

if a < 0:
    print("Sayı:NEGATİF!")
elif a > 0:
    print("Sayı:POZİTİF!")
    

print("EN BÜYÜK SAYI HANGİSİ?")

x = 20
y = 18
z = 3

if (x>y) and (x>z) :
    print(x)
elif(y>x) and (y>z):
    print(y)
else:
    print(z)
    


name = ["Liva","Efe","Asel","Ayaz"]
for nam in name:
    if nam == "Efe":
        continue
    elif nam == "Ayaz":
        break
    print("Şifre = " + nam + " = " + nam[0:2] )
    

sayac = 1
sum = 10

while sayac <= 10:
    sum = sum + sayac
    sayac = sayac + 1
    
print(sum)


for a in range(28):
    print(a)


    

#STAR DEMO


sayi = int(input("Lütfen sayı giriniz:"))

star = ""

for a in range(1,sayi+1):
    star = star + "*"
    print(star)
    
#ASAL SAYI HESAPLAMA

sayi1 = int(input("Lütfen sayı giriniz:"))



for x in range(2,sayi1):
    if(sayi1 % x ) == 0:
        print("Üzgünüz!Girilen sayı asal sayı değil!!!")
        break
        print("TEBRİKLER! ASAL SAYI!")
        
        
#1 İLE 30 ARASINDAKİ SAYILARI EKRANA YAZDIRMA

for i in range(1,30,2):
    print(i)
    
#1'DEN KULLANICININ GİRDİĞİ SAYIYA KADAR YAZDIRMA

number = int(input("Lütfen sayı giriniz:"))
for q in range(1,number+1):
    print(q)
    
  
#EXAMPLE

for y in range(3,42,5):
    print(y)
    


#FAKTORİYEL HESAPLAMA

    
number = int (input("Lütfen faktöriyelini bulmak istediğiniz sayıyı giriniz...\n"))
factorial = 1
i=1
if number >= 0:
  while i <= number:
      factorial*=i
      i+=1
  print("Girdiğiniz sayının faktöriyeli:",factorial)
else:
  print ("Negatif sayıların faktöriyeli olmaz!")
  
  
#MATRİS TOPLAMA

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[10,11,12],[13,14,15],[16,17,18]]
sonuc = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(a)):
    for j in range(len(b)):
        sonuc[i][j] = a[i][j] + b[i][j]
        
print(sonuc)

class Matematik():
    def __init__(self,sayi1,sayi2):
        print("Basit çalışmamıza hoşgeldiniz")
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        
    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def carp(self):
        return self.sayi1 * self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2
    
mat = Matematik(1,99)
print("Toplam =  " + str(mat.topla())) 

mat2 = Matematik(1000,10)
print("Sonuc = " + str(mat2.bol()))

mat3 = Matematik(9,9)
print("Sonuc = " + str(mat3.carp()))

class Person():
    def __init__(self,name,lastName,number):
        self.name = name
        self.lastName = lastName
        self.number = number
        
person = Person("Livanur Nagihan","Duman",2727)
print("Bilgiler = " + str(person.name))
print("Bilgiler = " + str(person.number))
print("Bilgiler = " + str(person.lastName))

class worker(Person):
    def __init__(self,salary):
        self.salary = salary
        
class customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
liva = worker(50000)
efe = customer(46434346464)
print("Bilgiler = " + str(liva.salary))
print("Bilgiler = " + str(efe.creditCardNumber))

#%%
class HesapMakinesi():
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
        print("**Hesap Makinesi Yazılım Programına Hoşgeldiniz***")
        
    def topla1(self):
        return self.number1 + self.number2
        
    def cikar1(self):
        return self.number1 - self.number2
        
    def carp1(self):
        return self.number1 * self.number2
        
    def bol1(self):
        return self.number1 / self.number2
        
    def ucgeninAlani(self):
        int(input("Lütfen üçgenin yüksekliğini giriniz:"))
        int(input("Lütfen üçgenin taban kenarını giriniz:"))
        return (self.number1 * self.number2) / 2

    def silindirinHacmi(self):
        int(input("Lütfen silindirin yüksekliğini giriniz:"))
        int(input("Lütfen silindirin yarıçapını giriniz:"))
        return (self.number1 * self.number1)*self.number2 * 3
    
    def kureninHacmi(self):
        int(input("Lütfen kürenin yarıçapını giriniz"))
        return 4 * (self.number1*self.number1*self.number1)
    
hesap = HesapMakinesi(8,9)
print("Silindirin Hacmi = " + str(hesap.silindirinHacmi()))
print("Üçgenin Alanı = " + str(hesap.ucgeninAlani()))
print("Kürenin Hacmi = " + str(hesap.kureninHacmi()))








  



   
    
    
        
    
















