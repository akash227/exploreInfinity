#Equi-pair
N=raw_input()
#Converts the string to list
r=list(N.split(' '))
r=map(int,r)
t=len(r)
i=1
k=0

if t>4:
    while i<t:
        j=i+2
        while j<t:
            a=sum(r[0:i])
            b=sum(r[i+1:j])
            c=sum(r[j+1:t])
            if a==b and b==c:
                print "{ %d,%d }" % (i,j)
                print "{ %d,%d },{ %d,%d },{ %d,%d }" % (0,i-1,i+1,j-1,j+1,t-1)
                k=1
            j=j+1
        i=i+1
    if k != 1:
        print "Array does not contain any equi pair"
        
