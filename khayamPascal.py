from calendar import c


def khayam(n):
    
    for i in range(n) :    
        for j in range(i+1):
            c1=fact(i)
            c2=fact(i-j)
            c3=fact(j)
            f= (c1 // (c2*c3))
            print(f , end=" ")
        print()
    
def fact(c):
    
    if c==0 or c==1 :
        return 1
    else:
        b=c-1   
        while b>0 :
            c=c*b
            b=b-1
        return c
        
n=int(input("n = "))
khayam(n)


