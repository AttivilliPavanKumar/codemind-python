a=int(input())
b=int(input())
for i in range(a,b+1):
    j=i
    c=0
    d=0
    while j!=0:
        r=j%10
        if r!=0 and i%r==0:
            d+=1
        j//=10
        c+=1
    if c==d:
        print(i, end=' ')