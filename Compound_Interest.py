P=float(input())
R=float(input())
T=float(input())
CI=P*pow((1+R/100.00),T)-P
print(f"{CI:.2f}")