# import random
# def son_top(x):
#     tasodifiy=random.randint(1,x)
#     print(f"Men 1 dan {x} gacha son o'yladim, topa olasizmi qanday son o'yladim!")
#     while True:
#         taxmin=int(input(" = "))
#         if taxmin>tasodifiy:
#             print(f"{taxmin} dan kichikroq son kiriting!")
#         elif taxmin<tasodifiy:
#             print(f"{taxmin} dan kattaroq son kiriting!")
#         else:
#             break
#     print('tabriklayman topdingiz')

import random
def son_top(x):
    print(f"Endi siz 1-dan {x}-gacha son o'ylang men topaman!")
    input("son o'ylagan bo'lsangiz istalgan tugmani bosing!")
    past,yuqori=1,x
    urunish=0
    while True:
        urunish+=1
        tasodifiy=random.randint(past,yuqori)
        print(f"siz {tasodifiy}-sonini o'yladingiz!")
        x=input("To'g'ri (T), kichikroq(-), kattaroq son bo'lsa (+) ni bosing!: ")
        if x.lower()=='t':
            break
        elif x=='-':
            yuqori=tasodifiy-1
            continue
        elif x=='+':
            past=tasodifiy+1
            continue
        else:
            break
    print(f"{urunish}-ta urunishda topdim!")