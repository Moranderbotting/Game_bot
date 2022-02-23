from random import randrange
import asyncio
from game_other import *


#defining sprites You can change these
#faces and skin: overworld, nether
face=['','']
skin=['','']
stone=''
wood=''
leaf=''
sapling='🌳'
apple='🍎'
bedrock=''
#grandient of sky, need at least 12 different (6 for overworld, 6 for nether)
sky=[['','','','','',''],['', '', '', '', '', '']]
dirt=''
diamond=''
coal=''
iron=''
s_iron=''
i_block=''
vpick=''
bpick=''
ipick=''
dpick=''
obsidian=''
gravel=''
flint=''
f_n_s=''
nth=''
np=''
gold=''
quartz=''
g_block=''

#defining names for objects
bedrock_n="bedrock"
stone_n="stone"
dirt_n="dirt"
sky_n="sky"
wood_n="wood"
leaves_n="leaves"
diamond_n="diamond"
apple_n="apple"
sapling_n="sapling"
iron_n="iron"
coal_n="coal"
i_pick_n="iron pickaxe"
v_pick_n="wooden pickaxe"
b_pick_n="stone pickaxe"
d_pick_n="diamond pickaxe"
s_iron_n="iron ingot"
i_block_n="iron block"
obsidian_n="obsidian"
gravel_n="gravel"
flint_n="flint"
f_n_s_n="flint and steel"
nth_n="netherrack"
np_n="nether portal block"
gold_n="gold"
quartz_n="quartz"
g_block_n="gold block"

#range of view and size of map and max health
p_y=5
p_d=1
p_x=5
h=40
n=400
mx_health=10

#id & map_id -> name
dic={
    'p': bedrock_n,
    'b': stone_n,
    'd': dirt_n,
    'c': sky_n,
    'v': wood_n,
    'l': leaves_n,
    'x': diamond_n,
    's': sapling_n,
    'i': iron_n,
    'z': coal_n,
    'h': i_block_n,
    'o': obsidian_n,
    'g': gravel_n,
    'np': np_n,
    'n': nth_n,
    'gd': gold_n,
    'q': quartz_n,
    'gb':g_block_n,
    0: wood_n,
    1: stone_n,
    2: sapling_n,
    3: apple_n,
    4: dirt_n,
    5: coal_n,
    6: iron_n,
    7: s_iron_n,
    8: diamond_n,
    9: i_block_n,
    10: obsidian_n,
    11: gravel_n,
    12: flint_n,
    13: nth_n,
    14: gold_n,
    15: quartz_n,
    16: g_block_n
}
#id -> map_id
switcher2={
    0: 'v',
    1: 'b',
    2: 's',
    3: 'r',
    4: 'd',
    8: 'x',
    6: 'i',
    5: 'z',
    9: 'h',
    10: 'o',
    11: 'g',
    13: 'n',
    14: 'gd',
    15: 'q',
    16: 'gb'
}
#id -> map_id
dic3={
    'v': 0,
    'b': 1,
    's': 2,
    'r': 3,
    'd': 4,
    'x': 8,
    'i': 6,
    'z': 5,
    'h': 9,
    'o': 10,
    'g': 11,
    'n': 13,
    'gd': 14,
    'q': 15,
    'gb': 16
}
#id -> sprite
dic2={
    'b': stone,
    'l': leaf,
    'v': wood,
    'p': bedrock,
    'd': dirt,
    's': sapling,
    'x': diamond,
    'i': iron,
    'z': coal,
    'o': obsidian,
    'h': i_block,
    'g': gravel,
    'n': nth,
    'np': np,
    'gd': gold,
    'q': quartz,
    'gb': g_block
}
#craftable items
cr=[vpick, bpick, ipick, dpick, s_iron, i_block, f_n_s, g_block]

#crafting recipe
#[identifier, name, items needed in inventory on given place]
switcher_c={
    vpick: [0,v_pick_n, [5]],
    bpick: [1,b_pick_n, [2,5]],
    ipick: [2,i_pick_n, [2,2,0,0,0,0,0,3]],
    dpick: [3, d_pick_n, [2,0,0,0,0,0,0,2,3]],
    s_iron: [4,s_iron_n, [0,0,0,0,0,1,1]],
    i_block: [5,i_block_n,[0,0,0,0,0,0,0,4]],
    f_n_s: [6,f_n_s_n,[0,0,0,0,0,0,0,1,0,0,0,0,2]],
    g_block: [7,g_block_n,[0,0,0,0,0,0,0,0,0,0,0,0,0,4]]
}

#defining holdable items
hold=[wood, stone, sapling, dirt, gravel, coal, iron, diamond, i_block, obsidian, nth, gold, quartz, g_block]
#defining eatable items
food=[apple]
#holdable items (not placeable)
hold_it=[f_n_s]


#identifier -> sprite
inv_a={
    0: wood,
    1: stone,
    2: sapling,
    3: apple,
    4: dirt,
    5: coal,
    6: iron,
    7: s_iron,
    8: diamond,
    9: i_block,
    10: obsidian,
    11: gravel,
    12: flint,
    13: nth,
    14: gold,
    15: quartz,
    16: g_block
}
#sprite -> identifier
r_inv={
    wood: 0,
    stone: 1,
    sapling: 2,
    apple: 3,
    dirt: 4,
    coal: 5,
    iron: 6,
    s_iron: 7,
    diamond: 8,
    i_block: 9,
    obsidian: 10,
    gravel: 11,
    flint: 12,
    nth: 13,
    gold: 14,
    quartz: 15,
    g_block: 16
}
#name -> identifier
r_inv_a={
    wood_n: 0,
    stone_n: 1,
    sapling_n: 2,
    apple_n: 3,
    dirt_n: 4,
    coal_n: 5,
    iron_n: 6,
    s_iron_n: 7,
    diamond_n: 8,
    i_block_n: 9,
    obsidian_n: 10,
    gravel_n: 11,
    flint_n: 12,
    nth_n: 13,
    gold_n: 14,
    quartz_n: 15,
    g_block_n: 16
}

#craftable items
items=[v_pick_n, b_pick_n, i_pick_n, d_pick_n, s_iron_n, i_block_n, f_n_s_n, g_block_n]

#ores specifications
ores=[['g',[h/4,h*4/5],[h/60,h/40],7],['z',[h/5,h*3.9/5],[h/70,h/50],5],['i',[h/6,h*3/4],[h/90,h/60],3],['x',[1,h/6],[h/300,h/180],2], ['o',[1,h/8],[h/800,h/400],10], ['gd',[2*h+4,3.4*h], [h/60,h/50], 2], ['q', [2*h+10, 3.8*h], [h/100,h/50], 5]]

#items used to crafting
un_p=[0,1,4,5,6,7,8,11,12,13]

#p-bedrock
#b-stone
#d-dirt
#c-sky
#v-wood
#g-leaves
#x-diamond
#s-sapling
#g-gravel
#np-nether_portal
#n-netherrack
#o-obsidian

#creating a playing board
def create(n):
    tab=[]
    h1=h
    h2=int(h*3/4)+1
    h3=int(h*3/4)
    for i in range(n):
        li=[]
        a=randrange(0,20)
        if a==0:
            h1-=2
        elif a<5:
            h1-=1
        elif a<16:
            h1=h1
        elif a<19:
            h1+=1
        else:
            h1+=2
        if h1<=int(h*0.8):
            h1=int(h*0.8)+1
        if h1>int(h*1.2)+1:
            h1=int(h*1.2)
        li.append('p')
        for i in range(h1-1):
            li.append('b')
        li.append('d')
        for i in range(2*h-h1):
            li.append('c')
        li+=['p']*p_y
        a=randrange(0,20)
        if a==0:
            h2-=3
        elif a<4:
            h2-=2
        elif a<8:
            h2-=1
        elif a<12:
            h2=h1
        elif a<16:
            h2+=1
        elif a<19:
            h2+=2
        else:
            h2+=3
        a=randrange(0,20)
        if a==0:
            h3-=4
        elif a<4:
            h3-=3
        elif a<8:
            h3-=2
        elif a<12:
            h3=h1
        elif a<16:
            h3+=2
        elif a<19:
            h3+=3
        else:
            h3+=4
        if h3+h2>2*h:
            h3-=1; h2-=1
        li+=['n']*h2
        li+=['c']*(2*h-h2-h3)
        li+=['n']*h3
        li+=['p']
        tab.append(li[:])
    b=randrange(int(n/10),int(n/10*3)+1)
    #creating trees
    for i in range(b):
        a=randrange(2,n-2)
        s=find2(tab[a],'d')
        if s!=-1:
            if s+2>=2*h-1:
                tab[a][h+1]='v'; tab[a-1][h+1]='l'; tab[a+1][h+1]='l'
                if h>1:
                    tab[a][h+2]='l'
            else:
                c=randrange(s+2,min(s+7,2*h-1))
                for j in range(s+1,c):
                    if tab[a][j]=='c':
                        tab[a][j]='v'
                tab[a+1][c-1]='l'; tab[a+1][c]='l'; tab[a+1][c+1]='l'; tab[a+2][c]='l'
                tab[a-1][c-1]='l'; tab[a-1][c]='l'; tab[a-1][c+1]='l'; tab[a-2][c]='l'
                tab[a][c]='l'; tab[a][c+1]='l'; tab[a][c+2]='l';
    #randomizing places for ores
    for i in ores:
        if int(i[2][0]*n)==int(i[2][1]*n):
            b=i[2][0]*n
        else:
            b=randrange(int(i[2][0]*n),int(i[2][1]*n))
        if b==0:
            b=1
        for j in range(b):
            if int(i[1][0])>=int(i[1][1]):
                a=int(i[1][0])
            else:
                a=randrange(int(i[1][0]),int(i[1][1]))
            c=randrange(1,n)
            d=randrange(i[3]//2,i[3]*2)
            if tab[c][a]=='b' or tab[c][a]=='n':
                tab=f_ores(tab,d+1,i[0],c,a,n)
    #caves
    a=randrange(int(n/40),int(n/10))
    for i in range(a):
        b=randrange(1,n-10)
        c=randrange(3,10)
        h_b=randrange(3,int(h*0.75))
        h_u=randrange(2,4)
        for j in range(b,b+c):
            for k in range(h_b,h_b+h_u):
                tab[j][k]='c'
        d=randrange(0,4)
        if d<2:
            h_b1=h_b+randrange(-1,2)
            h_u1=h_u-1
            b1=b+c
            c=min(n-1,b1+randrange(2,10))
            for j in range(b1,c):
                for k in range(h_b1,h_b1+h_u1):
                    tab[j][k]='c'
        if d==2 or d==3:
            h_b+=randrange(-1,2)
            h_u-=1
            c=max(2,b-randrange(2,10))
            for j in range(c,b):
                for k in range(h_b,h_b+h_u):
                    tab[j][k]='c'
    return tab


#mining or placing chosen blocks
def mine(tab,inv,x,y,i,cr):
    kon='s'
    #lootbox (id: [(chance to get item of id in the second list, in first list)]
    loot={
        'l': [[[4,2],[5,3],[11,-1]],-1],
        'b': [[[1,1]],0],
        'x': [[[1,8]],2],
        'v': [[[1,0]],-1],
        'd': [[[1,4]],-1],
        's': [[[1,2]],-1],
        'z': [[[1,5]],0],
        'i': [[[1,6]],1],
        'h': [[[1,9]],1],
        'o': [[[1,10]],3],
        'g': [[[4,11],[5,12]],-1],
        'n': [[[1,13]],0],
        'q': [[[1,15]],1],
        'gd': [[[1,14]],2]
    }
    #if we are in the board
    if x>0 and x<len(tab) and y>=0 and y<len(tab[0]):
        
        if i>=len(inv):
            if i-len(inv)==0:
                #portal
                #op...po
                #.p...p.
                #o.....o
                #Checking if you can light up the portal
                if tab[x][y]=='o':
                    if tab[x+1][y]=='o':
                        dim=prt_ch(tab,x,y,2,0,[x,y,x,y])
                        a=y
                        while tab[x][a]=='o':
                            a+=1
                        dim[3]=min(a,dim[3])
                    elif tab[x-1][y]=='o' or tab[x-1][y+1]=='o':
                        dim=prt_ch(tab,x,y,-2,0,[x,y,x,y])
                    elif tab[x][y-1]=='o' or tab[x-1][y-1]:
                        dim=prt_ch(tab,x,y,1,2,[x,y,x,y])
                        dim=prt_ch(tab,x,y,-1,1,dim)
                    else:
                        dim=[-1,-1,-1,-1]
                    dim=prt_ch(tab,dim[0],dim[3],1,1,dim)
                    for j in range(dim[1]+1,dim[3]):
                        if tab[dim[0]][j]!='o' or tab[dim[2]][j]!='o':
                            dim[3]=j-1; break
                        bl=True
                        for i in range(dim[0]+1,dim[2]-1):
                            if tab[i][j]!='c':
                                bl=False
                        if not bl:
                            dim[3]=j-1; break
                    for i in range(dim[0]+1,dim[2]):
                        for j in range(dim[1]+1, dim[3]+1):
                            tab[i][j]='np'
                    kon="You lighted a nether portal"
                else:
                    kon="You can only use a lighter on obsidian for now"
                return [kon,inv,tab]
            else:
                return ["You can only use a lighter on obsidian for now", inv, tab]
        elif tab[x][y]=='p' or tab[x][y]=='np':
            kon="You cannot mine further down"
        elif tab[x][y]=='c':
            #placing block of given identifier
            if inv[i]!=0:
                kon='Placed '+dic.get(i)
                tab[x][y]=switcher2.get(i)
                inv[i]-=1
            else:
                kon='You do not have enough '+dic.get(i)
        else:
            k=loot.get(tab[x][y])
            if k[1]==-1:
                c=randrange(0,k[0][len(k[0])-1][0])
                b=0
                for i in range(len(k[0])):
                    if c<k[0][i][0]:
                        if k[0][i][1]==-1:
                            kon="You did not acquire anything"
                        else:
                            kon="You acquired "+ dic.get(k[0][i][1])
                            inv[k[0][i][1]]+=1
                        tab[x][y]='c'
                        break
            else:
                #checking if you have the needed item to mine
                if cr[k[1]]:
                    c=randrange(0,k[0][len(k[0])-1][0])
                    b=0
                    for i in range(len(k[0])):
                        if c<k[0][i][0]:
                            if k[0][i][1]=='n':
                                kon="You did not acquire anything"
                            else:
                                kon="You acquired "+ dic.get(k[0][i][1])
                                inv[k[0][i][1]]+=1
                            tab[x][y]='c'
                            break
                else:
                    kon="You need "+items[k[1]]+" to mine "+ dic.get(tab[x][y])
    else:
        kon='Cannot mine or place blocks outside of the map'
    return [kon,inv,tab]

#checking inventory and giving sprites to inv
def inv_ch(inv):
    kon='**INVENTORY**\n'
    for i in range(len(inv)):
        kon+=inv_a.get(i)+': '+str(inv[i])+'    '
    return kon

#crafting
def craft(inv,k,crafted):
    bo=True
    depl=[]
    if r_inv_a.get(k[1]) is None and crafted[k[0]]:
        return "You already crafted "+k[1]
    for i in range(len(k[2])):
        if k[2][i]>inv[i]:
            depl.append(i)
    if len(depl)==0:
        for i in range(len(k[2])):
            inv[i]-=k[2][i]
        kon="You crafted a "+k[1]
        if not r_inv_a.get(k[1]) is None:
            inv[r_inv_a.get(k[1])]+=1
        else:
            crafted[k[0]]=True
    else:
        kon="You don\'t have enough "
        for i in depl:
            if i in un_p:
                kon+="pieces of "+dic.get(i)+" and "
            else:
                kon+=dic.get(i)+"s and "
        kon=kon[::-1][4:][::-1]
        kon+="to craft a "+k[1]
    return kon

#eating/adding health
def eat(inv,k,health):
    value={
        apple: 4,
    }
    if inv[r_inv.get(k)]>0:
        if health==mx_health:
            return[health, "You are too full to eat", inv]
        inv[r_inv.get(k)]-=1
        return [min(health+value.get(k),mx_health), "Eaten a "+dic.get(r_inv.get(k)), inv]
    return [health, "You don't have enough "+dic.get(r_inv.get(k))+"s to eat one", inv]

#updating the board (entities, checking if character died, water flow, falling blocks)
def update(health):
    if health<=0:
        return 0
    return 1

#reading the board from given position
def rea(tab,x,y):
    a=''
    for i in range(max(0,len(tab[0])-y-p_y),min(len(tab[0])-y+p_d,len(tab[0]))):
        for j in range(max(0,x-p_x),min(x+p_x+1,len(tab))):
            #drawing player in the middle
            if j==x and i==len(tab[0])-y-1:
                a+=skin[y//(2*h)]
            elif j==x and i==len(tab[0])-y-2:
                a+=face[y//(2*h)]
            elif tab[j][len(tab[0])-1-i]=='c':
                #gradient for sky
                a+=sky[y//(2*h)][len(tab[0])-i-y]
            else:
                a+=dic2.get(tab[j][len(tab[0])-1-i])
        a+='\n'
    return a

#going to nether
def go_to_nth(tab,x,y):
    if y<80:
        y+=84
        kon="went to nether"
    else:
        y-=84
        kon="went to overworld"
    while tab[x][y]=='p':
        y+=1
    if tab[x][y]!='np':
        tab[x][y]='np'; tab[x][y-1]='o'; tab[x+1][y]='o'; tab[x-1][y]='o'
    while tab[x][y]=='np' or tab[x][y]=='o':
        x-=1
    x+=1
    while tab[x][y]=='np' or tab[x][y]=='o':
        y+=1
    return [kon, tab, x, y]
