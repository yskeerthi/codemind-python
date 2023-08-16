import math 
def prime(n):
    if(n==1):
        return -1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return -1
    return 1;
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0 and prime(i)==-1):
        c+=1
print(c)

