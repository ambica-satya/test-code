s1=input()
s2=input()
ch=s2[len(s2)-1]
count=0
for i in range(len(s1)):
    if s1[i]==ch:
        count=count+1
print(count)
