m=int(input())
n=list(map(int,input().split()))
s=0
for i in range(len(n)):
    if(n[i]%2==0):
        s=i
print(s)