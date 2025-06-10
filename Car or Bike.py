t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if x<y:
        print("Bike")
    elif x==y:
        print("Same")
    else:
        print("Car")
