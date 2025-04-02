import random
x=random.randint(1,10)
n=20
print("1-dan 10-gacha son ichidan men o'ylagan sonni toping!")
i=0
for i in range(n):
    taxmin=int(input(f"{i+1}-urinish-sonni kiriting: "))
    i+=1
    if taxmin==x:
        print('TABRIKLAYMAN SIZ TOPDINGIZ!!!!')
        print(f"{i} ta urinishdan foydalandingiz")
        break
    elif taxmin<x:
        print("kattaroq son kiriting: ")
    else:
        print("kichikroq son kiriting: ")
        
else:
    print(f"afsus imkoniyatingiz tugadi , men o'ylagan son {x} edi")
  