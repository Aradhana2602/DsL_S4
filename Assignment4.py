def TransposeSparseMatrix(sp_r):
    row=int(input("enter the no of rows :"))
    col=int(input("enter the no of cols"))
    sp=[]
    non_ze=0
    sp_r=[]
    sp_r.append([row ,col,0])
    print("Transpose of sparse matrix:")
    tra_sp=[0]*(non_ze+1)
    colt=[0]*col
    tra_sp[0]=[col,row,non_ze]
    for i in range(1,non_ze+1):
        colt[sp_r[i][1]]=colt[sp_r[i][1]]+1
    index=[1]*(col+1)    
    for i in range(1,col+1):
        index[i]=index[i-1]+colt[i-1]
    for i in range(1,non_ze+1):
        x=index[sp_r[i][1]]
        tra_sp[x]=[sp_r[i][1] ,sp_r[i][0] ,sp_r[i][2]]
        index[sp_r[i][1]]=index[sp_r[i][1]]+1
    for i in range(0 ,non_ze+1):
        print(tra_sp[i])    
 
   
def SimpleTranspose(sp_r):
    num_rows = len(sp_r)
    num_cols = len(sp_r[0])
    transposed = [[0] * num_rows for _ in range(num_cols)]
    for i in range(num_rows): 
        for j in range(num_cols):
             transposed[j][i] = sp_r[i][j]

    return transposed

 
def AddSparse(sp1,sp2):
    r1=sp1[0][0]
    c1=sp1[0][1]
    n1=sp1[0][2]+1
    r2=sp2[0][0]
    c2=sp2[0][1]
    n2=sp2[0][2]+1
    sp3=[]
 
    if(r1!=r2 or c1!=c2):
        print("Given matrix cannot be added")
        return sp3
    sp3.append([r1,c1,0])
    i=1
    j=1
    while(i<n1 and j<n2):
        if(sp1[i][0]==sp2[j][0] and sp1[i][1]==sp2[j][1]):
            sp3.append([sp1[i][0],sp1[i][1],sp1[i][2]+sp2[j][2]])
            sp3[0][2]+=1
            i+=1
            j+=1
        elif(sp1[i][0]==sp2[j][0]):
            if(sp1[i][1]<sp2[j][1]):
                sp3.append(sp1[i])
                sp3.append(sp2[j])
            else:
                sp3.append(sp2[j])
                sp3.append(sp1[i])
            i+=1
            j+=1
            sp3[0][2]+=2
 
        else:
            if(sp1[i][0]<sp2[j][0]):
                sp3.append(sp1[i])
                i+=1
            else:
                sp3.append(sp2[j])
                j+=1
            sp3[0][2]+=1
 
 
    while(i<n1):
        sp3.append(sp1[i])
        i+=1
        sp3[0][2]+=1
 
    while(j<n2):
        sp3.append(sp2[j])
        j+=1
        sp3[0][2]+=1
 
 
    return sp3
 
def insparse():
    row=int(input("enter the no of rows :"))
    col=int(input("enter the no of cols"))
    sp=[]
    non_ze=0
    sp_r=[]
    sp_r.append([row ,col,0])
 
    for i in range(row) :
        sp1=[]
        print("enter the ele. of " ,i+1 ,"th row")
        for j in range(col):
           x=int(input())
           if(x!=0):
               sp_r.append([i,j,x])
               non_ze=non_ze+1
           sp1.append(x)
        sp.append(sp1)
 
    sp_r[0][2]=non_ze
    return(sp_r)

def outsparse(sp_r):
    print("sparse matrix is :")
    for i in range (sp_r[0][2]+1):
            print(sp_r[i])

sp1=insparse()
outsparse(sp1)

sp2=insparse()
outsparse(sp2)

TransposeSparseMatrix(sp1 )
print("Simple Transpose")
print(SimpleTranspose(sp1))
 
 
print("Addidtion Sparse Matrix")
print(AddSparse(sp1 ,sp2))
