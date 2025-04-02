# car0={
#     'model':'cobalt',
#     'rangi':'oq',
#     'yil':2025,
#     'narxi':100000,
#     'km':100,
#     'karobka':'avtomat'
# }

# car1={
#     'model':'damas',
#     'rangi':'oq',
#     'yil':2021,
#     'narxi':100000,
#     'km':185000,
#     'karobka':'mexanika'
# }

# car2={
#     'model':'onix',
#     'rangi':'qora',
#     'yil':2025,
#     'narxi':180000,
#     'km':10,
#     'karobka':'avtomat'
# }

# cars=[car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].upper()}-{car['rangi']}-{car['yil']}-yil-{car['narxi']}$-{car['km']}-km-{car['karobka']}")

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(f"{til.upper()} ", end='')