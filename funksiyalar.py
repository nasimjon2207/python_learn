# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 09:31:30 2025

@author: hp
"""

# def salom_ber():
#     print('Assalomu aleykum')

# def salom_ber(ism):
#     print(f"Assalomu aleykum, hurmatli {ism.title()}")

# def salom_ber(ism):
#     """Ism kiritib yozing"""
#     print(f"Assalomu aleykum {ism.title()} aka")

# def malumot(ism, yoshi):
#     """yoshi va ismini kiriting yilini aniqlab beradi"""
#     print(f"{ism.title()}" " " f"{2025-yoshi}-yilda tug'ulgan")

# def son(sonk):
#     """sonkiriting kvadratini topib beraman"""
#     print(f"{sonk**2}")


# def son(juft):
#     """son kiriting juftligini aniqlab beraman"""
#     if juft%2 == 0:
#         print(f"{juft} sonimiz juft")
#     else:
#         print('toq')

# def son(x,y):
#     """son kiriting kvadratini chiqarib beraman"""
#     print(f"{x**y}")

# def son(x):
#     """son kiriting qoldiqsiz bo'linishini topib beraman"""
#     for y in range(2,11):
#         if x%y==0:
#             print(f"{x} soni {y} ga bo'linadi ")

# def tuliq(ism, familiya):
#     """tuliq ismni qaytaruvchi funksiya"""
#     tuliqism=f"{ism} {familiya}"
#     return tuliqism
# talaba1=tuliq('nasimjon', 'xudayberdiyev')
# talaba2=tuliq('abdulbosit', 'sotiboldiyev')
# print(f"darsga kelmagan talabalar: {talaba1.title()} , {talaba2.upper()}")

# def fullname(name,surname, otaname=""):
#     """tuliq ism familiya qaytaradigan funksiya"""
#     if otaname:
#         print(f"{name.title()} {surname.title()} {otaname.title()}")
#     else:
#         print(f"{name} {surname}")


# def avto_info(company,model,rangi,yili,karobka,narxi=None):
#     """avtomobil haqida ma'lumot qayataradigan funksiya"""
#     avto={'company':company,
#           'model':model,
#           'rangi':rangi,
#           'yili':yili,
#           'karobka':karobka,
#           'narxi':narxi}
#     return avto
# avto1=avto_info('GM', 'damas', 'oq', 2021, 'mexanika',7000)
# avto2=avto_info('GM', 'cobalt', 'oq', 2025, 'avtomat')
# avtolar=[avto1,avto2]
# for avt in avtolar:
#     if avt['narxi']:
#         narxi=avt['narxi']
#     else:
#         narxi='nomalum'
#     print(f"{avt['rangi']} {avt['model']} {avt['narxi']} $")



# def oraliq(min,max):
#     son=[]
#     while min <= max:
#         son.append(min)
#         min+=1
#     return son
# print(oraliq(0,10))
# print(oraliq(0,30))


# def avto_info(company,model,rangi,karobka,yili,narxi):
#     avto={'company':company,
#           'model':model,
#           'rangi':rangi,
#           'karobka':karobka,
#           'yili':yili,
#           'narxi':narxi}
#     return avto
# print("avtolar ruyxatini tahkillashtiramiz!!")
# avtolar=[]
# while True:
#     print("quyidagi ma'lumotlarni kiriting! ")
#     company=input("ishlab chiqaruvchi: ")
#     model=input("avto modeli: ")
#     rangi=input("rangi: ")
#     karobka=input("mexanika yoki avtomat: ")
#     yili=input("yili: ")
#     narxi=input("narxi: ")
    
    
#     avtolar.append(avto_info(company, model, rangi, karobka, yili, narxi))
#     javob=input("yana avto qo'shmoqchimisiz yes/no: ")
#     if javob=='no':
#         break


# def bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=input(f"Talaba {ism.title()}ning bahosini qo'ying? : ")
#         baholar[ism]=baho
#     return baholar
# talabalar=['ali', 'vali','salim','halim']
# baholar=bahola(talabalar)
# print(baholar)

# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()   

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)


# def summ(*sonlar):
#     """istalgancha son kiritiladi!!! """
#     suma=0
#     for son in sonlar:
#         suma+=son
#     return suma
# print(summ(1,2,3,4,5))

# def suma(*son):
#     return sum(son)
# print(suma(1,2,3,4,5))

# def kupaytma(*kop):
#     kupa=1
#     for kup in kop:
#         kupa=kupa*kup
#     return kupa
# print(kupaytma(2,3,4,5,6))

# def talaba_info(ism, familiya, **kwargs):
#     kwargs['ism']=ism
#     kwargs['familiya']=familiya
#     return kwargs

# talaba = talaba_info('olim','olimov',nickname='jack tulak',fakultet='IT',yonalish='AT')

# print(talaba)

# import random
# son=random.randint(0, 17)
# print(son)

# import math
# p=lambda pi,r: 2*pi*r
# print(p(math.pi,10))
# product=lambda x,y:pow(x,y)
# print(product(2,6))

# def daraja(n):
#     return lambda x:x**n
# kvadrat=daraja(2)
# kub=daraja(3)
# print(kvadrat(2),kub(2))
















