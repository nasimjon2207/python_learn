
import random
import math
def son_top_kv(x):
    tasodifiy=random.randint(1,x)
    tasodifiy=tasodifiy**2
    print(f"Men 1-dan {x}-gacha natural sonning kvadratini o'yladim, topa olasizmi qanday son o'yladim!!!")
    i=0
    while True:
        i+=1
        def kvadratmi(n):
            ildiz=math.sqrt(n)
            return ildiz.is_integer()
        taxmin=int(input("? = "))
        if kvadratmi(taxmin):
            if taxmin>tasodifiy:
                print(f"{int(math.sqrt(taxmin))}-ning kvadratidan kichikroq son o'yladim!")
            elif taxmin<tasodifiy:
                print(f"{int(math.sqrt(taxmin))}-kvadratidan kattaroq son o'yladim!")
            else:
                break
        else:
             print(f"1-dan {x}-gacha NATURAL sonni kvadratini kiriting!")   
        
    print(f"'Tabriklayman' {int(math.sqrt(taxmin))}-sonining kvadratini o'ylagan edim,  {i}-chi urunishda topdingiz!")
    
    print('--------------------------------------')
    
   
# import random
# def son_top(x):
    
    print(f"Endi siz 1-dan {x}-gacha natural sonining kvadratini o'ylang men topaman!")
    input("son o'ylagan bo'lsangiz istalgan tugmani bosing!")
    past,yuqori=1,x
    urunish=0
    while True:
        urunish+=1
        tasodifiy=random.randint(past,yuqori)
        tasodifiy=pow(tasodifiy, 2)
        print(f"siz {int(math.sqrt(tasodifiy))}-sonning kvadratini o'yladingiz!")
        x=input("To'g'ri (T), kichikroq(-), kattaroq son bo'lsa (+) ni bosing!: ")
        if x.lower()=='t':
            break
        elif x=='-':
            yuqori=math.sqrt(tasodifiy)-1
            continue
        elif x=='+':
            past=math.sqrt(tasodifiy)+1
            continue
        else:
            break
    
    if i>urunish:
        print(f"Siz {i}-ta urunishda topdingiz! Men esa {urunish}-ta  urunishda topdim!")
        print(" Va MEN Yutdim!")
    elif i==urunish:
        print(f" siz {i}-ta urunishda topdingiz! Men ham {urunish}-ta  urunishda topdim!")
        print(" DURRANG!")
    else:
        print(f" siz {i}-ta urunishda topdingiz! Men esa {urunish}-ta  urunishda topdim!")
        print(" Va SIZ Yutdingiz!")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
