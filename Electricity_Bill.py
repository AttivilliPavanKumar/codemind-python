u=int(input())
if(u<200):
    b=u*1.20
    c=1.20
elif(u>=200 and u<400):
    b=u*1.40
    c=1.40
elif(u>=400 and u<600):
    b=u*1.60
    c=1.60
elif(u>=600 and u<800):
    b=u*1.80
    c=1.80
else:
    b=u*2.00
    c=2.00
sur=0
if(b>400):
    sur=(b*0.15)
tot=b+sur
print("Units Consumed: {}".format(u))
print("Cost per Unit: {:.2f}".format(c))
print("Bill: {:.2f}".format(b))
print("Surcharge: {:.2f}".format(sur))
print("Total Amount: {:.2f}".format(tot))