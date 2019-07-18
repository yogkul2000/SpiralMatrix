r=int(input())
c=int(input())
m=[[int(input()) for i in range(c)]for j in range(r)]
a=0
b=0
while(a<r and b<c):
    for i in range (b,c):
        print(m[a][i],end=" ") 
    a+=1
    for i in range (a,r):
        print(m[i][c-1],end=" ")
    c-=1
    if(a<r):
        for i in range(c-1,(b-1),-1):
            print(m[r-1][i],end=" ")
        r=r-1    
    if(b<c):
        for i in range(r-1,(a-1),-1):
            print(m[i][b],end=" ")
        b=b+1    
      
