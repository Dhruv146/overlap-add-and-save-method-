def givep(f,l):
    temp=f/l
    if(f%l==0):
        P=temp+1
    else:
        P=temp+2
    return P

def returnx(l,p,f,n,mat1,method): 
    x=[[0 for row in range(0,int(n))] for col in range(0,int(p))]                                                     #mat1[]=x(n) and mat2[]=h(n)
    if(method == 2):
        z=int(0)
        a=int(0)
        s=int(0)
        lenmat1=len(mat1)
        for row in range(0,p-1):
            value=0
            y=int(n-l+1)
            for col in range(0,n):
                if(value< n-l):
                        if(a==0 and s<n-l):
                            x[row][col]=0
                            value=value+1
                            s=s+1
                        else:
                            x[row][col]= x[row-1][y]
                            value=value+1
                            a=a+1
                            y=y+1
                            s=s+1        
                elif(z<f):
                    x[row][col]=mat1[z]
                    value=value+1
                    z=z+1
                    a=a+1
                    s=s+1

    elif(method == 1):
            z=int(0)
            lenmat1=len(mat1)
            for row in range(0,p-1):
                value=0
                for col in range(0,n):
                    if(value<l):
                        if(z<lenmat1):
                            x[row][col]=mat1[z]
                            value=value+1
                            z=z+1
                        else:
                            x[row][col]=0
    return x
    
    
def findy(p,n,l,x,mat2):
    sfinal=[]
    h=len(mat2)
    run=n-h
    for z in range(1,run+1):
        mat2.append(0)
    y=[[0 for row in range(0,int(n))] for col in range(0,int(p))]
    temp=[]
    for i in range(0,p):
        for j in range(0,n):
            temp.append(x[i][j])
        sfinal=convol(temp,mat2)
        for j in range(0,n):
            y[i][j]=sfinal[j]
        del sfinal[:]
        del temp[:]
    return y
    

def inputmat(z):                                  # to take the inputs for x(n) and h(n) and adding them to list.
    mat=[]
    for v in range(1,z+1):
        q=int(input('Enter %d element : '%(v)))
        mat.append(q)
    return mat

def check_diff(mat1,mat2):
    x=len(mat1)
    h=len(mat2)
    temp=[]
    if(x>h):
        run=x-h
        for z in range(1,run+1):
            mat2.append(0)
        temp=convol(mat1,mat2)
        return mat1,mat2
    else:
         run=h-x
         for z in range(1,run+1):
            mat1.append(0)
         temp=convol(mat2,mat1)
         return mat2,mat1
         

def convol(large,small):
    lenlarge=len(large)
    templist=[0]*lenlarge
    temp=0
    yn=[]
    convol=[[0 for row in range(0,lenlarge)] for col in range(0,lenlarge)]
    for r in range(0,lenlarge):
        if(r>0):
            first=large[0]
            last=large[lenlarge-1]
            for q in range(0,lenlarge):
                if(q>0 & q<lenlarge):
                    templist[q]=large[q-1]
                    convol[r][q]=templist[q]
                else:
                    templist[0]=last
                    convol[r][q]=templist[q]
            for p in range(0,lenlarge):
                large[p]=templist[p]
        else:
            for p in range(0,lenlarge):
                convol[r][p]=large[p]
    yn=matmul(convol,small)
    return yn

def matmul(convol1,small):
    final=[]
    lenlarge=len(convol1)
    for i in range(0,lenlarge):
        total=0
        for j in range(0,lenlarge):
            total2=convol1[j][i]*small[j]
            total=total+total2
        final.append(total)
    return final

def giveans(yn,n,p,l,method):
    ans=[]
    var=0
    temp=[]
    if(method == 2):
        for i in range(0,p):
            for j in range(0,n):
                if(j>=n-l):
                        var=yn[i][j]
                        ans.append(var)
        a=len(ans)
        
    elif(method == 1):
    
        for i in range(0,p):
            for j in range(0,n):
                if(j<l):
                    if not temp:
                        var=yn[i][j]
                        ans.append(var)
                    else:
                        var=yn[i][j]
                        var=var+temp[0]
                        ans.append(var)
                        del temp[0]
                else:
                    temp.append(yn[i][j])
        a=len(ans)

    del ans[a-1]
    del ans[a-2]
    ans.pop(-1)    
    return ans

def printvalue(p,n,mat,var):
    printit=[]
    values=1
    for i in range(0,p):
        print('%s%d : '%(var,values))
        for j in range(0,n):
            printit.append(mat[i][j])
        print(printit)
        del printit[:]
        values+=1



def main():
    print('\n'*5)
    mat1=[]
    large=[]
    small=[]
    x=[]
    yn=[]
    ans=[]

    f=int(input('Enter the length of the x(n) matrix : '))
    mat1=inputmat(f)                                            # making x(n)=[1,2,3,4] as list 
    m=int(input('Enter the length of the h(n) matrix : '))
    mat2=inputmat(m)                                              # making h(n)=[7,8,9] as list    
    l=int(input('Enter the value of l : '))
    
    print("1. overlap add method ")
    print("2. overlap save method ")
    method=int(input("Compute using : "))
    n=l+m-1                                               # n= size of x1(, , , , ,) 
    p=int(givep(f,l))                             # p= size of x1(n),x2(n)...xn(n)
    print('The value of p is : %d '%(p))
    print('The value of n is : %d '%(n))
    print('\nx(n) : ')
    print(mat1)
    print ('h(n) : ')
    print(mat2)
    x=returnx(l,p,f,n,mat1,method)
    print('\nThe Different values of X(inputs) : ')
    variable='X'
    printvalue(p,n,x,variable)
    variable='Y'
    yn=findy(p,n,l,x,mat2)
    print('\nThe Different values of Y(Output) : ')
    printvalue(p,n,yn,variable)
    ans=giveans(yn,n,p,l,method)

    if(method==1):    
        print('\n Final answer of overlap add method :\n ')
    elif(method==2):
        print('\n Final answer of overlap save method :\n ')
    print(ans)
    


if __name__=="__main__":
    main()