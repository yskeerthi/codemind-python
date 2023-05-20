def main(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum+=i
    return sum
a=int(input())
b=int(input())
if main(a)==b and main(b)==a:
    print("Amicable")
else:
    print("Not Amicable")