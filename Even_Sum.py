n=int(input())
n=map(int,input().split())
s=0
for i in n:
    if(i%2==0):
        s=s+i
print(s)