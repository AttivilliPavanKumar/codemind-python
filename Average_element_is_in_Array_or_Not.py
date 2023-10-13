m=int(input())
n=list(map(int,input().split()))
s=0
for i in n:
    s=s+i
a=s//len(n)
if a in n:
    print("True")
else:
    print("False")