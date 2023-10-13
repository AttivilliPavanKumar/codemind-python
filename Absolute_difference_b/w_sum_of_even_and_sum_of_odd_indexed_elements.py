m=int(input())
n=list(map(int,input().split()))
s1=0
for i in range(len(n)):
    if(i%2==0):
        s1=s1+n[i]
s2=0
for i in range(len(n)):
    if(i%2!=0):
        s2=s2+n[i]
print(abs(s2-s1))