number=int(input()) 
first=0
second=1
next=0
while(number>next):
	next=first+second
	first=second
	second=next
if(number-first<second-number):
    print(first)
elif(number-first==second-number):
		print(f"{first} {second}")
else:
    print(second)