import random
n=0
while True:
    n+=1
    i=random.randint(1,10)
    print(f"siz {i}-sonini o'yladingiz!!")
    javob=input("togri bo'lsa (T) ni bosing, kichikroq bo'lsa (-), kattaroq bo'lsa (+) ni bosing!: ")
    if javob.lower()=='t':
        print("topdim!")
        print(f"{n}-chi urunishda topdim!")
        break
    elif javob=='-':
        print("kichikroq son kiriting: ")
        continue
    elif javob=='+':
        print("kattaroq son kiriting!: ")
        continue
    