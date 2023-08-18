n=int(input())
a=0
b=1
for i in range(2,n+1):
    sum=a+b
    if n==sum:
        print(True)
        break
    a=b
    b=sum
if n!=sum:
    print(False)