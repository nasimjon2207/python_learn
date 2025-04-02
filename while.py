# ism=input('Ismingizni kiriting? ')
# savol=f" Assalomu aleykum {ism.title()} yoshingiz nechida? "
# yosh=input(savol)

# print('Istalgan sonning kvadratini qaytaruvchi dastur!')
# savol='istalgan son kiriting? '
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing!): "
# qiymat=''
# while qiymat !='exit':
#     qiymat=input(savol)
#     if qiymat !='exit':
#         print(float(qiymat)**2)

# savol='istalgan son kiriting? '
# savol+="(dastur stop bo'lishi uchun 'exit' deb yozing!): "
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         ishora=False
#     else:
#         print(float(qiymat)**2)

# savol='istalgan son kiriting? '
# savol+="(dasturni to'xtatish uchun 'exit' deb yzoing!): "
# while True:
#     qiymat=input(savol)
#     if qiymat.lower()=='exit':
#         break
#     else:
#         print(float(qiymat)**2)

# sonlar=list(range(1,12))
# for son in sonlar:
#     if son==5:
#         continue
#     else:
#         print(float(son)**2)

# son=0
# while son<10:
#     son+=1
#     if son%2 !=0:
#         continue
#     else:
#         print(son)

# kitob='yaxshi ko\'rgan kitobingizni kiriting?'
# kitob+="(dastur ishni tugatishi uchun 'stop' deb yozing!): "
# ishora=True
# while ishora:
#     qiymat=input(kitob)
#     if qiymat.lower()=='stop':
#         break
# print('Rahmat!!')

# ismlar=[]
# print("whould you like The best frinds's name add? ")
# n=1
# while True:
#     savol=f"{n}-chi do'stingizni ismini kiriting? - "
#     ism=input(savol)
#     ismlar.append(ism)
#     javob=input("yana do'stlaringiz bormi? ")
#     if javob.lower()=='yes':
#         n+=1
#         continue
#     else:
#         break
# for x in ismlar:
#     print(x.title())
# print("yuqoridagi insonlar sizning qiyomatli do'stlaringizdir!!")

# print("do'stlaringizni ismini va yoshini birgalikda saqlaymiz")
# dustlar={}
# ishora=True
# while ishora:
#     ism=input("do'stingizni ismini kiriting? - ")
#     yosh=input(f"{ism.upper()} ning yoshini kiriting? - ")
#     dustlar[ism]=int(yosh)
#     javob=input("yana qo'shimcha ma'lumot berasizmi(ha/yo'q): ")
#     if javob.lower()=="yo'q":
#         ishora=False
#     elif javob=='ha':
#         continue
#     else:
#         break
# for ism, yosh in dustlar.items():
#     print(f"{ism.title()} {yosh}-yoshda")

# talabalar=['Nasimjon', 'Abdulbosit', 'don','xon']
# while 'don' in talabalar:
#     talabalar.remove('don')
# for ism in talabalar:
#     print(ism)

# student=['Nasimjon', 'Abdulbosit', 'don','xon']
# baholangan={}
# while student:
#     talaba=student.pop()
#     baho=input(f"{talaba} ning bahosini kiriting? - ")
#     print(f"{talaba.title()} baholandi!!!")
#     baholangan[talaba]=baho
# print(baholangan)
    