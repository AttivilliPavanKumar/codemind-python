r,c=map(int,input().split())
m=[list(map(int,input().split()))[:c:] for i in range(r)]
s=0
for i in range(0,r):
    s+=sum(m[i])
print(s)