from random import randrange;

#game management, finding items in a list or checking the nether portal

def find2(lis,xD):
    x=0
    for i in lis:
        if xD==i:
            return x
        x+=1
    return -1

def find3(lis,xD):
    x=0
    y=0
    for i in lis:
        y=0
        for j in i:
            if xD==j:
                return [x,y]
            y+=1
        x+=1
    return [-1,-1]

def top(lis):
    kon=[]
    konu=[]
    if len(lis)<5:
        for i in range(len(lis)):
            kon.append(0)
            konu.append(-1)
    else:
        kon=[0,0,0,0,0]
        konu=[-1,-1,-1,-1,-1]
    x=0
    for i in range(len(lis)):
        for j in range(len(kon)):
            if lis[i]>=kon[j]:
                if j==0:
                    kon[0]=lis[i]
                    konu[0]=i
                    continue
                a=kon[j]
                b=konu[j]
                kon[j]=lis[i]
                konu[j]=i
                kon[j-1]=a
                konu[j-1]=b
    return [kon,konu]

def f_ores(tab,n,name,x,y,mx):
    if n<=0:
        return tab
    n-=1
    if tab[x][y]=='p':
        return tab
    tab[x][y]=name
    m=randrange(0,n//3+1)
    if y>1:
        tab=f_ores(tab,m,name,x,y-1,mx)
    if n-m==0:
        return tab
    z=randrange(0,(n-m)//2+1)
    if x!=mx-1:
        tab=f_ores(tab,z,name,x+1,y,mx)
    if x!=0:
        tab=f_ores(tab,n-m-z,name,x-1,y,mx)
    return tab

def prt_ch(tab,x,y,sit,ktd,dim):
    #sit: 1=up, -1=down, 2=left, -2=right
    #dim: [min_x, min_y, mx_x, mx_y]
    #ktd: 0=down, 1=left, 2=right
    if tab[x][y]=='o':
        dim[3]=max(y,dim[3])
        if ktd==0:
            if sit==2:
                if tab[x+1][y+1]=='o': dim[2]=x+1; dim=prt_ch(tab,x+1,y+1,-1,2,dim)
                else: dim=prt_ch(tab,x+1,y,2,0,dim)
            if sit==-2:
                if tab[x-1][y+1]=='o': dim[0]=x-1; dim=prt_ch(tab,x-1,y+1,-1,1,dim)
                else: dim=prt_ch(tab,x-1,y,-2,0,dim)
        if ktd==1:
            if sit==1:
                if tab[x+1][y-1]=='o': dim[1]=y-1; dim=prt_ch(tab,x+1,y-1,2,0,dim)
                else: dim=prt_ch(tab,x,y-1,1,1,dim)
            if sit==-1:
                dim=prt_ch(tab,x,y+1,-1,1,dim)
        if ktd==2:
            if sit==1:
                if tab[x-1][y-1]=='o': dim=prt_ch(tab,x-1,y-1,-2,0,dim); dim[1]=y-1
                else: dim=prt_ch(tab,x,y-1,1,2,dim)
            if sit==-1:
                dim=prt_ch(tab,x,y+1,-1,2,dim)
    return dim
