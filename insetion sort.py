l=[]
n=int(input("enter a number:"))
for i in range(n):
    l.append(int(input("enter the data:")))
print(l)
for j in range(1,n,1):
    k=j-1
    key=l[j]
    while key<l[k] and k>=0:
        l[k+1]=l[k]
        k=k-1
    l[k+1]=key
print(l)
    
    
    
