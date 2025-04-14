# a,b=map(int,input().split())
# if a>b:
#     print('>')
# elif a==b:
#     print('=')
# else:
#     print('<')
 
# a=int(input())
# b=int(input())
# print(a+b)

# lugat={'add':'qo\'shmoq', 'public':'umumiy', 'private':'shaxsiy', 'love':'sevgi'}
# kalit=input('so\'z kiriting tarjima qilib beraman? - ').lower()
# tarjima=lugat.get(kalit)
# print(tarjima)

# numbers=list(map(int, input().strip().split(',')))
# numbers.sort()
# m=0
# n=0
# for i in range(0,4):
#   m=m+numbers[i]
# for i in range(1,5):
#   n=n+numbers[i]
# print(m,n)

# n=int(input())
# a,b,c=map(int, input().split())
# s=a+b+c
# if s>=n:
#     print('Yes')
# else:
#     print('No')

# a,b,c=map(int, input().split())
# x=[a,b,c]
# x=sorted(x)
# if x[0]==x[2]:
#     print(1)
# elif x[0]<x[2] and x[0]<x[1]:
#     print(3)
# else:
#     print(2)

# n=int(input())
# if n%2==0:
#   print(n)
# else:
#   print(n*2)

# a,b,c=map(int,input().split())
# x=[a,b,c]
# x=sorted(x)
# print(x[2])

# n=int(input())
# print(n**2)

# a,b=map(int, input().split())
# p=2*(a+b)
# s=a*b
# if p>s:
#     print(p)
# else:
#     print(s)

# r=int(input())
# print('=')

# n=int(input())
# x=len(str(n))
# if x%2!=0:
#     print('toq')
# else:
#     print('juft')
# n=int(input())
# while n>0:
#     i=n%10
#     if i%2!=0:
#         print(i)
#         n=n//10
#     else:
#         break

# a=int(input())
# y=(10*pow(3,3)+22-9/3)*7-2022
# b=y-(a+1)
# print(int(b))


# def sonni_sozga(son):
#     birliklar = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
#     onliklar = ["", "o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]
#     yuzliklar = ["", "bir yuz", "ikki yuz", "uch yuz", "to'rt yuz", "besh yuz", "olti yuz", "yetti yuz", "sakkiz yuz", "to'qqiz yuz"]

#     if son < 0 or son > 999:
#         return "Faqat 0 dan 999 gacha bo'lgan sonlarni qo'llab-quvvatlaydi."

#     yuz = son // 100
#     on = (son % 100) // 10
#     bir = son % 10

#     natija = []

#     if yuz:
#         natija.append(yuzliklar[yuz])
#     if on:
#         natija.append(onliklar[on])
#     if bir:
#         natija.append(birliklar[bir])
#     if not natija:  # agar 0 bo‘lsa
#         return "nol"

#     return ' '.join(natija)


# # Misol uchun:
# son = 999
# print(f"{son} -> {sonni_sozga(son)}")


# a,b=map(int, input().split())
# print(abs(a-(b+1)))

# n=input()
# if len(n)==7 and n[0]=="A":
#     n=int(n[6])%2
#     print(n)

# n,m=map(int, input().split())
# print((n*m)//2)

# a,b=map(int, input().split())
# print(b,a)

# a=int(input())
# if a==1:
#     print(6)
# elif a==2:
#     print(5)
# elif a==3:
#     print(4)
# if a==6:
#     print(1)
# elif a==5:
#     print(2)
# elif a==4:
#     print(3)

# n=int(input())
# r=[int(x) for x in str(n)]
# print(r)
# son=int(input())
# for ra in str(son):
#     print(ra)        

# n=int(input())
# toq=all(int(r)%2!=0 for r in str(n))
# uz_toq=len(str(n))%2!=0
# if toq and uz_toq:
#     print("YES")
# else:
#     print("NO")


# t,T=map(int, input().split())
# x=t+T
# if x==24:
#     print(0)
# elif x>24:
#     print(x-24)
# else:
#     print(x)

# t, T = map(int, input().split())
# print((t + T) % 24)

# a,b=map(int, input().split())
# print(((b-a)+1)*10)

# n=int(input())
# print(int(n//10))

n=int(input())
d=n*(n-3)//2
print(int(d))