n=int(input())
r=0
while n>0:
    rem=n%10
    r=r*10+rem
    n//=10
print(r)