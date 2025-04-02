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
n=int(input())
while n>0:
    i=n%10
    if i%2!=0:
        print(i)
        n=n//10
    else:
        break
    