def konvertuj(pozicia):
    x=pozicia//n
    y=pozicia%n
    return x,y

def up_right(value,index,x,y):
    if((y-2>=0) and (x+1)<n):
        if(value[index-2*n+1]==0):
            return True
    return False

def up_left(value, index,x,y):
    if((y-2>=0)and(x-1)>=0):
        if(value[index-2*n-1]==0):
            return True
    return False

def left_up(value, index,x,y):
    if((y-1>=0)and(x-2)>=0):
        if(value[index-n-2]==0):
            return True
    return False

def left_down(value, index,x,y):
    if((y+1<n)and(x-2)>=0):
        if(value[index+n-2]==0):
            return True
    return False

def right_up(value, index,x,y):
    if((y-1>=0)and(x+2)<n):
        if(value[index-n+2]==0):
            return True
    return False

def right_down(value, index,x,y):
    if((y+1<n)and(x+2<n)):
        if(value[index+n+2]==0):
            return True
    return False

def down_left(value, index,x,y):
    if((y+2<n)and(x-1>=0)):
        if(value[index+2*n-1]==0):
            return True
    return False

def down_right(value, index,x,y):
    if((y+2<n)and(x+1)<n):
        if(value[index+2*n+1]==0):
            return True
    return False
def heuristika(value,index,x,y):
    counter=0
    if(right_up(value, index, x, y)): counter+=1
    if(right_down(value, index, x, y)):counter+=1
    if(left_down(value, index, x, y)):counter+=1
    if(left_up(value, index, x, y)):counter+=1
    if(down_left(value, index, x, y)):counter+=1
    if(down_right(value, index, x, y)):counter+=1
    if(up_left(value, index, x, y)):counter+=1
    if(up_right(value, index, x, y)):counter+=1
    return counter
def add(total,value,stack):
    number=total.__len__()-1
    for i in range(number,0,-1):
        value[total[i][1]]=count+1
        pom=value.copy()
        stack.append(pom)
        value[total[i][1]]=0
def pohyb(value, n,stack):
    index=value.index(max(value))
    total=[]
    y,x=konvertuj(index)
    if(right_up(value,index,x,y)):
        new_index=index-n+2
        poz1,poz2=konvertuj(new_index)
        count= heuristika(value,new_index,poz2,poz1)
        total.append([count,new_index])
    if(right_down(value,index,x,y)):
        new_index=index+n+2
        poz1,poz2=konvertuj(new_index)
        count= heuristika(value,new_index,poz2,poz1)
        total.append([count,new_index])
    if(left_down(value,index,x,y)):
        new_index=index+n-2
        poz1,poz2=konvertuj(new_index)
        count= heuristika(value,new_index,poz2,poz1)
        total.append([count,new_index])
    if(left_up(value,index,x,y)):
        new_index=index-n-2
        poz1,poz2=konvertuj(new_index)
        count= heuristika(value,new_index,poz2,poz1)
        total.append([count,new_index])
    if(down_left(value,index,x,y)):
        new_index=index+2*n-1
        poz1,poz2=konvertuj(new_index)
        count= heuristika(value,new_index,poz2,poz1)
        total.append([count,new_index])
    if(down_right(value,index,x,y)):
        new_index=index+2*n+1
        poz1,poz2=konvertuj(new_index)
        count= heuristika(value,new_index,poz2,poz1)
        total.append([count,new_index])
    if(up_left(value,index,x,y)):
        new_index=index-2*n-1
        poz1,poz2=konvertuj(new_index)
        count= heuristika(value,new_index,poz2,poz1)
        total.append([count,new_index])
    if(up_right(value,index,x,y)):
        new_index=index-2*n+1
        poz1,poz2=konvertuj(new_index)
        count= heuristika(value,new_index,poz2,poz1)
        total.append([count,new_index])
    total.sort()
    add(total,value,stack)
    if(total==[]):
        return -1
    return total[0][1]

n=(int(input()))
pocitadlo=0
final=[]
for p in range(0,n*n):
    stack=[]
    value = [0] * n*n
    pocet=n*n
    counter=0
    count=1
    value[p]=count
    while(min(value)==0):
        counter+=1
        if counter==100000:
            print("Vysledny stav z tejto pozicie neexistuje")
            break
        new = pohyb(value, n,stack)
        if(new==-1):
               # print("neuspech ",value)
                value=stack.pop()
                count=max(value)
        else:
            count+=1
            value[new]=count
            if(min(value)!=0):
                print("Uspech ",value)
                pocitadlo+=1
                final.append(p)
    if(pocitadlo==(n*n)/2):
        print("pozicie z ktorych sa da dostat:",final)
        break