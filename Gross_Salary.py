b=int(input())
if(b<=10000):
    da=b*0.8
    hra=b*0.2
    t=b+da+hra
    print(f"{t:.2f}")
elif(b<=20000):
    da=b*0.9
    hra=b*0.25
    t=b+da+hra
    print(f"{t:.2f}")
elif(b>20000):
    da=b*0.95
    hra=b*0.3
    t=b+da+hra
    print(f"{t:.2f}")