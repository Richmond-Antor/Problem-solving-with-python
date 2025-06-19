# cook your dish here
t=int(input())
for _ in range (t):
    p,q,r,s=map(int , input().split())
    
    if q>(p+r+s) or r>(q+p+s) or s>(q+r+p) or p>(q+r+s):
        print("yes")
    else:
        print("No")
