n=int(input())
count=1
i=1
while True:
    x=str(i)
    if "3" in x or "4" in x or "7" in x:
        i=i+1
    else:
        i=i+1
        count=count+1
    if n==count:
        break
print(i)
