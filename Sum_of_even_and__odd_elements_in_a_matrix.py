r,c=map(int,input().split())
m=[list(map(int, input().split()))[:c:] for i in range(r)]
s1=0
s2=0
for j in m:
    for e in j:
        if e%2==0:
            s1+=e
        else:
            s2+=e
print(s1, s2)