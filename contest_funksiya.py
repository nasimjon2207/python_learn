
def son(son):
    birliklar = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
    onliklar=["","o'n","yigirma","o'ttiz","qirq","ellik","oltmish","yetmish","sakson","to'qson"]
    yuzliklar = ["", "bir yuz", "ikki yuz", "uch yuz", "to'rt yuz", "besh yuz", "olti yuz", "yetti yuz", "sakkiz yuz", "to'qqiz yuz"]
    if son==1000:
        return "bir yuz ming"
    yuz=son//100
    on=(son%100)//10
    bir=son%10
    natija=[]
    if yuz:
        natija.append(yuzliklar[yuz])
    if on:
        natija.append(onliklar[on])
    if bir:
        natija.append(birliklar[bir])
    if not natija:
        return "nol"
    return ' '.join(natija).strip()
x=int(input("son kiriting = "))
natija=son(x)
print(natija.strip())



