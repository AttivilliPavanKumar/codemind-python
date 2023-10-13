m=int(input())
n=list(map(int,input().split()))
p=int(input())
c=0
for i in n:
    if i==p:
        c+=1
print(c)