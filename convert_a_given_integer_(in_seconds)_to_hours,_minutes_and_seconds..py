i=int(input())
h=i//3600
m=(i-(h*3600))//60
s=(i-(m*60)-h*3600)
print(f"H:M:S-{h}:{m}:{s}")