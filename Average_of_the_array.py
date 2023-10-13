m=int(input())
n=list(map(int,input().split()))
s=0
for i in n:
    s=s+i
a=0
a= s/len(n)
print(f"{a:.2f}")