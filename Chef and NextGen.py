t= int(input())
for _ in range(t):
    a,b,x,y=map(int,input().split())
    if (a*b) <= (x*y):
        print("Yes")
    else:
        print("no")
