n=int(input())
res=""
while True:
    r=n//3
    x=int(n%3)
    res=res+str(x)
    n=r
    if r==0:
        break
print(res[::-1])
