#funkcia konvertuj - prepis jednorozmerneho pola na suradnice dvojrozmerneho pola, potrebne pre kontrolu, ci nevystupujem z pola
def konvertuj(pozicia):
    x=pozicia//n
    y=pozicia%n
    return x,y

#kontrola pohybu hore a doprava, ci neprekracujem mapu a ci je dane policko volne
def up_right(value,index,x,y):
    if((y-2>=0) and (x+1)<n):
        if(value[index-2*n+1]==0):
            return True
    return False

#kontrola pohuby hore a dolava
def up_left(value, index,x,y):
    if((y-2>=0)and(x-1)>=0):
        if(value[index-2*n-1]==0):
            return True
    return False

#kontrola pohybu vlavo a hore
def left_up(value, index,x,y):
    if((y-1>=0)and(x-2)>=0):
        if(value[index-n-2]==0):
            return True
    return False

#kontrola pohybu vlavo a dole
def left_down(value, index,x,y):
    if((y+1<n)and(x-2)>=0):
        if(value[index+n-2]==0):
            return True
    return False

#kontrola pohybu vpravo a hore
def right_up(value, index,x,y):
    if((y-1>=0)and(x+2)<n):
        if(value[index-n+2]==0):
            return True
    return False

#kontrola pohybu vpravo a hore
def right_down(value, index,x,y):
    if((y+1<n)and(x+2<n)):
        if(value[index+n+2]==0):
            return True
    return False

#kontrola pohybu dole a vlavo
def down_left(value, index,x,y):
    if((y+2<n)and(x-1>=0)):
        if(value[index+2*n-1]==0):
            return True
    return False

#kontrola pohybu dole a vpravo
def down_right(value, index,x,y):
    if((y+2<n)and(x+1)<n):
        if(value[index+2*n+1]==0):
            return True
    return False

#funkcia heuristika mi ohodnoti dane policko (hodnotenie spociva v tom,
#ze si pocitam na kolko dalsich policok sa viem z danej pozicie dostat a su volne)
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
    return counter  #returnem pocet policok na ktore sa viem dostat a su volne

#funkcia na pridavanie dalsich stavov
#(v pripade ze heuristika nenajde riesenie na prvykrat a potrebujem prehladavat dalej do hlbky)
def add(total,value,stack):
    number=total.__len__()-1
    for i in range(number,0,-1):
        value[total[i][1]]=count+1 #ulozenie pozicie kde sa viem dostat do pola
        pom=value.copy()
        stack.append(pom) #pridanie pola s aktualnym stavom do listu
        value[total[i][1]]=0

#funkcia pohyb mi urcuje kde vsade sa viem pohnut
def pohyb(value, n,stack):
    index=value.index(max(value))   #zistenie maxima mi sluzi na najdenie indexu posledneho kroku kde sa nachadzam
    total=[]
    y,x=konvertuj(index) #prepis na dvojrozmerne pole pre kontrolu ci nepresahujem hranice mapy
    if(right_up(value,index,x,y)):
        new_index=index-n+2
        poz1,poz2=konvertuj(new_index)
        count= heuristika(value,new_index,poz2,poz1)    #ohodnotenie kazdej pozicie
        total.append([count,new_index])     #pridanie do listu
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
    total.sort()    #sort listu - sluzi ako queue, 0 prvok beriem do postupnosti (ma najlepsie ohodnotenie podla heuristiky)
    add(total,value,stack) #ostatne prvky z queue pridavam do listu
    if(total==[]):  #ak je total prazdna mnozina, riesenie neexistuje
        return -1
    return total[0][1]  #returnem najmensi prvok z queue

n=(int(input())) #vstup - velkost mapy
pocitadlo=0
final=[]
for p in range(0,n*n): #zistovanie poctu vyskytu prvkov
    stack=[]
    value = [0] * n*n   #inicializacia samich 0 v poli
    pocet=n*n
    counter=0
    count=1
    value[p]=count
    while(min(value)==0):   #ak min == 0, tak este niesom vo finalnom stave, final stav ma min 1
        counter+=1
        if counter==100000: #pocet pokusov po kolkych je prehladavanie vyhodnotene ako nedosiahnutelny cielovy stav
            print("Vysledny stav z tejto pozicie neexistuje")
            break
        new = pohyb(value, n,stack) #index prvku s najmensim ohodnotenim podla heuristiky
        if(new==-1):    #ak uloha nema riesenie
               # print("neuspech ",value)
                value=stack.pop()   #v pripade neuspechu berem najblizsi stav
                count=max(value)    #do countu si ulozim cislo posledneho kroku
        else:
            count+=1
            value[new]=count    #poznacenie si pozicie ktora bola vyhodnotena za najlepsiu
            if(min(value)!=0):  #ak minimum je 1 tak som dosiahol finalny stav
                print("Uspech ",value)
                pocitadlo+=1
                final.append(p)
    if(pocitadlo==10):
        print("pozicie z ktorych sa da dostat:",final)  #vypis prvych 10 pozicii z ktorych sa da dostat
        break