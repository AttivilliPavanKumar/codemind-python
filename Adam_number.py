n=int(input())
s=0
f=0
sq1=n*n
while(n!=0):
    r=n%10
    n=n//10
    s=(s*10)+r
sq2=s*s
while(sq2!=0):
    t=sq2%10
    sq2=sq2//10
    f=(f*10)+t
if(f==sq1):
    print("True")
else:
    print("False")