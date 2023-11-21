# Write a program to print duplicates from the list.

n=int(input())
l=[]
s=input().split()
for i in s:
    l.append(int(i))
for i in range(0,n):
    count=0
    for j in range(0,n):
        if l[i]==l[j]:
            count=count+1
    if count>1:
        print(l[i],end=' ')

