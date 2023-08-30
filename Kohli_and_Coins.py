a=int(input())
if(a%10==10):
    print(a//10)
elif((a%10)%5==0):
    print((a//10)+(a%10)//5)
else:
    print("-1")