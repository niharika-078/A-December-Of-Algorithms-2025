c=0
i=1
n=int(input("Enter limit number:"))
for i in range(1,n):
    if (i*i)<=n:
        print(i*i)
        c+=1
print("Total count:", c)
