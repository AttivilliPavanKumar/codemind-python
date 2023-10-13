m=int(input())
n=list(map(int,input().split()))
s1=0
for i in n:
    if(i%2==0):
        s1=s1+i
s2=0
for i in n:
    if(i%2!=0):
        s2=s2+i
print(abs(s2-s1))