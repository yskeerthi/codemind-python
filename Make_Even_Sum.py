n=int(input())
a=list(map(int,input().split()))
c=0
c1=0
for i in a:
    if i%2==0:
        c+=1
    else:
        c1+=1
if c%2==0 and c1%2==0:
    print("1")
else:
    print("0")