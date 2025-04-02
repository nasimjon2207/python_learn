# oilam={'dadam': 'Karimov Adhamjon', 'yoshi': '57', 'yili': '1968'}
# oilam['kasbi']='fermer'
# print(f"dadamning ismlari: {oilam['dadam']},yoshi: {oilam['yoshi']}, yili:{oilam['yili']}, kasbi: {oilam['kasbi']}")

# lugat={ 'strong': 'kuchli', 'love':'sevmoq', 'string':'tip' }
# kalit=input('so\'z kiriting?- ').lower()
# tarjima=lugat.get(kalit)
# print(tarjima)
# if tarjima==None:
#     print('bunday suz yoq')
# else:
#     print(tarjima)

# mahsulotlar={
#     'anor':5000,
#     'olma':6000,
#     'banan':45000,
#     'mandarin':25000
# }
# bozorlik=['anor', 'non', 'choy', 'olma']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot} = {mahsulotlar[mahsulot]}")
# for buyurtma in bozorlik:
#     if buyurtma not in mahsulotlar:
#         print(f"{buyurtma} olib keling!!!")

# mahsulotlar={
#     'anor':5000,
#     'olma':6000,
#     'banan':45000,
#     'mandarin':25000
# }
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot)

# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}

# mamlakat=input('qaysi mamlakat haqida ma\'lumot kerak -- ').lower()
# poytaxt=davlatlar.get(mamlakat)
# print(f"{mamlakat.upper()}ning poytaxti {poytaxt.title()}")


# menu={
#     'osh':15000,
#     "non":4000,
#     'choy':2000,
#     'kabob':17000,
#     'manti':10000,
#     "sho'rva":4500,
#     'fast_food':45000
# }
# n=int(input('nechta taom tanlaysiz? - '))
# buyurtma=[]
# for i in range(n):
#     buyurtma.append(input(f"{i+1}-taom:").lower())
# narxi=0
# for zakas in buyurtma:
#     if zakas in menu:
#         print(f"{zakas.upper()} = {menu[zakas]} so'm")
#         narxi=narxi+menu[zakas]
#     else:
#         print(f"{zakas} - bizda bunday ovqat yo\'q")
# print('umumiy narxi = ', narxi)

