T=int(input())
for t in range(T):
    x,y,z=map(int,input().split())
    a=list(range(1,x+1))
    if x<=3:
        print(x*y)
    if x>3:
        temp=x*y
        for i in a:
            if i%3==0:
                temp+=z
        if a[-1]%3==0:
            temp-=z 
        print(temp)
                    
            
                
            
        
    
        