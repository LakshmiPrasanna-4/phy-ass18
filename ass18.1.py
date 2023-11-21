# Write a program to print duplicate count of the list.

n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,n):
    count=0
    c=0
    for j in range(0,n):
        if l[i]==l[j]:
            count=count+1
    if count>1:
       c=c+1
print(c)
      

