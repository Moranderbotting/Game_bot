#  __  __           _        _             __  __                           _            _  _  __  ___    __   ___  
# |  \/  |         | |      | |           |  \/  |                         | |         _| || |/_ |/ _ \  / /  / _ \ 
# | \  / | __ _  __| | ___  | |__  _   _  | \  / | ___  _ __ __ _ _ __   __| | ___ _ _|_  __  _| | (_) |/ /_ | | | |
# | |\/| |/ _` |/ _` |/ _ \ | '_ \| | | | | |\/| |/ _ \| '__/ _` | '_ \ / _` |/ _ \ '__|| || |_| |> _ <| '_ \| | | |
# | |  | | (_| | (_| |  __/ | |_) | |_| | | |  | | (_) | | | (_| | | | | (_| |  __/ | |_  __  _| | (_) | (_) | |_| |
# |_|  |_|\__,_|\__,_|\___| |_.__/ \__, | |_|  |_|\___/|_|  \__,_|_| |_|\__,_|\___|_|   |_||_| |_|\___/ \___/ \___/ 
#                                   __/ |                                                                           
#                                  |___/

import discord
import nacl
import time
from datetime import datetime
import asyncio
from game_other import find2
from game_manage import *
import os

client=discord.Client()
channel=client.get_channel(711919025659314187)
member=client.get_user(709385722666418236)

msg=[]
tab=[]
plr=[]

#token to your bot
bot_token=''

#controls to game, you can change them
left='⬅️'; right='➡️'; up=':arrow_double_up:'; minelu='↖️'; mineru='↗️'; mineld='↙️'; minerd='↘️'; mineu='⬆️'; mined='⬇️'

switcher={
    left: [-1,'left'],
    right: [1,'right'],
    up: [0,'up'],
    minelu: [-1,1],
    mineru: [1,1],
    mineld: [-1,0],
    minerd: [1,0],
    mined: [0,-1],
    mineu: [0,2],
}


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    channel=client.get_channel(758392380126265396)
    #Loading saves from text file
    global msg,tab,plr
    num=['0','1','2','3','4','5','6','7','8','9']
    kon=open('game_bot_saves.txt','r')
    a=0; b=[]; c=''
    rl=kon.readline()
    if rl!='' or rl!='[]': 
        for i in rl:
            if i in num: c+=i
            else:
                if c!='': b.append(int(c)); c=''
        msg.append([])
        for i in range(0,len(b),3):
            if i//12>len(msg)-1: msg.append([])
            try:
                g=client.get_guild(b[i+2])
                g=g.get_channel(b[i+1])
                g=await g.fetch_message(b[i])
            except:
                g=None
            msg[i//12].append(g)
        rl=kon.readline()
        a=[]; b=[]; c=[]; j=''; k=''; p=''; number=0
        for i in rl:
            if i in num and j in num: number*=10; number+=int(i)
            elif i in num: p+=j; number=int(i)
            elif i=='[':
                continue
            elif i==']':
                if j in num: c+=[p]*number; b.append(c); c=[]
                elif j==']' and k!=']': tab.append(b); b=[]
            elif j in num: c+=[p]*number; p=''
            elif j!='[' and j!=']':
                p=j
            k=j; j=i
        rl=kon.readline()
        a=[]; b=0; c=''; k=[]; j=''
        for i in rl:
            if i==']' and b==3 and j in num: k.append(int(j)); c=''; a.append(k); k=[]
            elif i==']' and b==3:
                if c==' False': k.append(False)
                else: k.append(True)
                c=''; a.append(k); k=[]
            if i==']' and b==2: a.append(int(c)); c=''; plr.append(a); a=[]
            if i==',' and j==']': continue
            if i=='[': b+=1
            elif i==']': b-=1
            elif i==',' and b==2: a.append(int(c)); c=''
            elif i==',' and b==3 and j in num: k.append(int(c)); c=''
            elif i==',' and b==3:
                if c==' False': k.append(False)
                else: k.append(True)
                c=''
            else: c+=i
            j=i
    kon.close()
    print("Finished loading")
    #saving games every hour
    now = datetime.now()
    while True:
        if now.minute==0:
            k='['
            for i in range(len(msg)):
                k+='['
                try:
                    if plr[i][2]==[0]*len(inv_a) and plr[i][3]==[False]*len(cr):
                        for gam in msg[i]:
                            await gam.delete()
                        msg.pop(i)
                        tab.pop(i)
                        plr.pop(i)
                        i-=1
                        continue
                except:
                    for gam in msg[i]:
                        await gam.delete()
                    msg.pop(i)
                    tab.pop(i)
                    plr.pop(i)
                    i-=1
                    continue
                try:
                    for gam in msg[i]:
                        k+=str(gam.id)+','+str(gam.channel.id)+','+str(gam.guild.id)+','
                    k+=']'
                except:
                    print("Access denied")
            k+=']'+'\n['
            for gam in tab:
                k+='['
                for line in gam:
                    it=0
                    k+='['
                    for s in range(1,len(line)):
                        if line[s]==line[s-1]: it+=1
                        else: k+=line[s-1]+str(it+1); it=0
                    if len(line)!=0:
                        k+=line[len(line)-1]+str(it+1)+']'
                k+=']'
            k+=']\n'+str(plr)
            os.remove('game_bot_saves_bu.txt')
            r=open('game_bot_saves.txt','r')
            kon=open('game_bot_saves_bu.txt','w+')
            kon.write(r.read())
            r.close()
            kon.close()
            os.remove('game_bot_saves.txt')
            kon=open('game_bot_saves.txt','w+')
            kon.write(k)
            kon.close()
            print("Saved games at "+str(now.hour)+str(now.minute))
        await asyncio.sleep(60)
        now = datetime.now()

@client.event
async def on_message(message):
    cont=message.content.lower()
    #8===========D, a meme function
    elif cont.startswith('bot pp'):
        name=message.content[5:]
        b=0
        for i in name:
            if i!=' ':
                break
            else:
                b+=1
        name=name[b+2:]
        b=0
        for i in name:
            if i!=' ':
                break
            else:
                b+=1
        name=name[b:]
        if len(name)==0:
            name=str(message.author)[:len(str(message.author))-5]
        a=randrange(0,100)
        if '<' in name and '>' in name:
            name2=name[find2(name,'<'):find2(name,'>')]
            if '!' in name2:
                name2=name2[3:]
                print(name2)
                name2=client.get_user(int(name2))
            elif '&' in name2:
                name2=name2[3:]
                print(name2)
                name2 = message.guild.get_role(int(name2))
            else:
                name2=name2[2:]
                name2=client.get_user(int(name2))
            name2=name2.name
            j=0
            name=name[:find2(name,'<')]+name2+name[find2(name,'>')+1:]        
        kon="   8"; kon+="="*randrange(0,25); kon+="D "
        if '758397597999300639' in cont:
            kon="   8"; kon+="="*randrange(20,25); kon+="D"
        if(a==0):
            kon="so smoll pp "+name+" killed himself"
        elif(a==1):
            kon="so big it destroyed "+name+"'s house"
        embedVar = discord.Embed(title="peepee size machine", description="saying how big ur pp is since 1995", color=randrange(0,16777215))
        embedVar.add_field(name=name+'\'s penis', value=kon, inline=True)
        await message.channel.send(embed=embedVar)
#_____________________________________________________________________________________________________
#Bot management with a message
    #starting new game
    elif cont=='bot game':
        #adding new map
        global tab,plr,msg
        #adding starting eq and creating a map
        plr.append([n//2,int(h*1.5+1),[0]*len(inv_a),[False]*len(cr),0,message.author.id,mx_health]); tab.append(create(n))
        v=len(msg)
        if msg==[]: v=0
        while tab[v][plr[v][0]][plr[v][1]-1]=='c':
            plr[v][1]-=1
        msg.append([await message.channel.send("You are currently holding "+wood), await message.channel.send("Started new game\n"+rea(tab[v],plr[v][0],plr[v][1])),await message.channel.send(':heart:'*(mx_health//2)+':broken_heart:'*(mx_health%2)), await message.channel.send('.\n'+inv_ch(plr[v][2]))])
        #Adding reactions to messages
        re=hold+hold_it
        for i in re:
            await msg[v][0].add_reaction(i)
        re=[left,right,minelu,mineld,minerd,mineru,mined,mineu,up]
        for i in re:
            await msg[v][1].add_reaction(i)
        re=food
        for i in re:
            await msg[v][2].add_reaction(i)
        await msg[v][2].edit(content=':heart:'*(mx_health//2)+':broken_heart:'*(mx_health%2))
        re=cr
        for i in re:
            await msg[v][3].add_reaction(i)
        print("started game nr "+str(v))
    #giving a crafting recipe
    elif cont.startswith('crafting recipe'):
        v=find2(items,message.content[16::])
        k=cr[v]
        k=switcher_c.get(k)
        if v==-1:
            await message.channel.send("This item is not craftable")
        else:
            kon="You need "
            j=0
            for i in k[2]:
                if i!=0:
                    kon+=str(i)+' '
                    if j in un_p:
                        if i>1:
                            kon+="pieces of "+dic.get(j)
                        else:
                            kon+="piece of "+dic.get(j)
                    elif i>1:
                        kon+=dic.get(j)+'s'
                    else:
                        kon+=dic.get(j)
                    kon+=" and "
                j+=1
            kon=kon[:len(kon)-4]
            kon+="to craft "+k[1]
            await message.channel.send(kon)
    #sending a help message
    elif cont=="bot help":
        help_g="Help regarding the game:\n  1. To start a game type ```bot game``` in any channel\n   2. After you type this bot will send 3 messages:\n          1) Shows you what you are holding\n          2) Shows your character and the world around it\n          3)Shows your health\n          4) Shows you your inventory\n   3. You can add reactions to command your character:\n          1)Reacting to first message changes what your character will be placing\n          2) Reacting to second message makes your character move, place or destroy blocks\n          3)Reacting to the third message will allow you to eat food and regenerate hp\n          4)Reacting to fourth message will craft whatever you are reacting with"
        help_g+="\n\nTo get the crafting recipe of given item type ```crafting recipe + name of item you want to craft```"
        help_g+="\nTo get a savefile with your game type ```bot save``` while replying to the message of the game.\nType ```bot load``` and attach a savefile to start a game from that save"
        await message.channel.send(help_g)
    #saving all game files to a txt file, so you don't lose it on program close
    if message.author.id==444990330178371584 and cont=='bot save' and message.reference==None:
        k=''
        for i in range(len(msg)):
            k+='['
            if len(plr[i])<len(plr[0]):
                for gam in msg[i]:
                    try: await gam.delete()
                    except: print("access denied")
                msg.pop(i)
                tab.pop(i)
                plr.pop(i)
                i-=1
                continue
            elif plr[i][2]==[0]*len(inv_a) and plr[i][3]==[False]*len(cr):
                for gam in msg[i]:
                    try: await gam.delete()
                    except: print("access denied")
                msg.pop(i)
                tab.pop(i)
                plr.pop(i)
                i-=1
                continue
            for gam in msg[i]:
                k+=str(gam.id)+','+str(gam.channel.id)+','+str(gam.guild.id)+','
            k+=']'
        k+=']'+'\n['
        for gam in tab:
            k+='['
            for line in gam:
                it=0
                k+='['
                for s in range(1,len(line)):
                    if line[s]==line[s-1]: it+=1
                    else: k+=line[s-1]+str(it+1); it=0
                if len(line)!=0:
                    k+=line[len(line)-1]+str(it+1)+']'
            k+=']'
        k+=']\n'+str(plr)
        os.remove('game_bot_saves_bu.txt')
        r=open('game_bot_saves.txt','r')
        kon=open('game_bot_saves_bu.txt','w+')
        kon.write(r.read())
        r.close()
        kon.close()
        os.remove('game_bot_saves.txt')
        kon=open('game_bot_saves.txt','w+')
        kon.write(k)
        kon.close()
        print("Saved games")
    #Sending a savefile to user asking
    elif cont=='bot save':
        if message.reference is not None:
            g=client.get_guild(message.reference.guild_id)
            g=g.get_channel(message.reference.channel_id)
            g=await g.fetch_message(message.reference.message_id)
            v=find3(msg,g)
            if v!=[-1,-1]:
                k=''
                for line in tab[v[0]]:
                    it=0
                    k+='['
                    for s in range(1,len(line)):
                        if line[s]==line[s-1]: it+=1
                        else: k+=line[s-1]+str(it+1); it=0
                    if len(line)!=0:
                        k+=line[len(line)-1]+str(it+1)+']'
                k+=']\n'+str(plr[v[0]])
                kon=open('game_bot_save_temp.txt','w+')
                kon.write(k)
                kon.close()
                kon=open('game_bot_save_temp.txt','r')
                await message.channel.send("Succesfully saved",file=discord.File('game_bot_save_temp.txt','game_save.txt'))
                kon.close()
                os.remove("game_bot_save_temp.txt")
            else: await message.channel.send("Please reply to the game message with this command")
        else: await message.channel.send("Please reply to the game message with this command")
    #loading a game from a savefile
    elif cont=='bot load' and message.attachments!=[]:
        num=['0','1','2','3','4','5','6','7','8','9']
        for at in message.attachments:
            if at.filename.endswith('.txt'):
                v=len(msg)
                x=await at.read()
                x=x.decode('utf-8')
                a=0; b=[]; c=[]; j=''; p=''; number=0
                for i in x:
                    if i in num and j in num: number*=10; number+=int(i)
                    elif i in num: p+=j; number=int(i)
                    elif i=='[':
                        continue
                    elif i==']':
                        if j in num: c+=[p]*number; b.append(c); c=[]
                        elif j==']': c+=[p]*number; p=''; b.append(c); tab.append(b); b=[]; break
                    elif j in num: c+=[p]*number; p=''
                    elif j!='[' and j!=']':
                        p=j
                    j=i
                    a+=1
                d=[]; b=1; c=''; k=[]; j=''
                for i in x[x.find(']]')+3:]:
                    if i==']' and b==3 and j in num: k.append(int(j)); c=''; d.append(k); k=[]
                    elif i==']' and b==3:
                        if c==' False': k.append(False)
                        else: k.append(True)
                        c=''; d.append(k); k=[]
                    if i==']' and b==2: d.append(int(c)); c=''; plr.append(d); d=[]
                    if i==',' and j==']': continue
                    if i=='[': b+=1
                    elif i==']': b-=1
                    elif i==',' and b==2: d.append(int(c)); c=''
                    elif i==',' and b==3 and j in num: k.append(int(c)); c=''
                    elif i==',' and b==3:
                        if c==' False': k.append(False)
                        else: k.append(True)
                        c=''
                    else: c+=i
                    j=i
                if tab[v]!=[] and plr[v]!=[]:
                    plr[v][5]=message.author.id
                    msg.append([await message.channel.send("You are currently holding "+inv_a.get(plr[v][4])), await message.channel.send("Started game from savefile\n"+rea(tab[v],plr[v][0],plr[v][1])),await message.channel.send(':heart:'*(plr[v][6]//2)+':broken_heart:'*(plr[v][6]%2)), await message.channel.send('.\n'+inv_ch(plr[v][2]))])
                    re=hold+hold_it
                    for i in re:
                        await msg[v][0].add_reaction(i)
                    re=[left,right,minelu,mineld,minerd,mineru,mined,mineu,up]
                    for i in re:
                        await msg[v][1].add_reaction(i)
                    re=food
                    for i in re:
                        await msg[v][2].add_reaction(i)
                    re=cr
                    for i in re:
                        await msg[v][3].add_reaction(i)
                    print("Started game nr "+str(v)+" from load")
                    break
    #Stopping a referenced game from being played
    elif cont=='bot stop':
        if message.reference is not None:
            g=client.get_guild(message.reference.guild_id)
            g=g.get_channel(message.reference.channel_id)
            g=await g.fetch_message(message.reference.message_id)
            v=find3(msg,g)
            if v!=[-1,-1]:
                if plr[v[0]][5]==message.author.id:
                    await msg[v[0]][0].edit(content="Game stopped, You cannot play it anymore")
                    msg.pop(v[0])
                    tab.pop(v[0])
                    plr.pop(v[0])
                    await message.add_reaction("<:upvote:927885768326791179>")
                else:
                    await message.channel.send("Don't try to delete other's games")
            else: await message.channel.send("Please reply to the game message with this command")
        else: await message.channel.send("Please reply to the game message with this command")
                
                

        
@client.event
async def on_raw_reaction_add(reaction):
    guild=client.get_guild(int(reaction.guild_id))
    channel=guild.get_channel(int(reaction.channel_id))
    mes=await channel.fetch_message(reaction.message_id)
    
    #declining reaction from self
    if reaction.user_id==mes.author.id:
        return
    #taking variables
    global tab,plr,switcher,switcher_c,cr,inv_a,hold
    
    #checking place in arrays
    v = find3(msg,mes)
    if v!=[-1,-1]:
        if reaction.user_id==plr[v[0]][5]:
            re=[minelu,mineru,mineld,minerd,mined,mineu,up]
            if v[0]!=-1:
                #deleting reaction
                await mes.remove_reaction(reaction.emoji,client.get_user(reaction.user_id))
                if v[1]==0:
                    #changing what you are holding depending on reaction
                    if str(reaction.emoji) in hold:
                        plr[v[0]][4]=r_inv.get(str(reaction.emoji))
                        ho="You are currently holding "+inv_a.get(plr[v[0]][4])
                        await msg[v[0]][0].edit(content=ho)
                    if str(reaction.emoji) in hold_it:
                        if plr[v[0]][3][find2(cr,str(reaction.emoji))]:
                            plr[v[0]][4]=len(inv_a)+find2(hold_it,str(reaction.emoji))
                            await msg[v[0]][0].edit(content="You are currently holding "+str(reaction.emoji))
                        else:
                            await msg[v[0]][0].edit(content="Didn't craft "+str(reaction.emoji)+" yet")
                if v[1]==1:
                    if str(reaction.emoji) == left or str(reaction.emoji) == right or str(reaction.emoji) == up:
                        #moving left or right
                        k=switcher.get(str(reaction.emoji))
                        #checking if character is on border
                        if plr[v[0]][0]==0 and str(reaction.emoji) == left:
                            kon='Cannot go further left'
                        elif plr[v[0]][0]==n and str(reaction.emoji) == right:
                            kon='Cannot go further right'
                        #moving up
                        elif str(reaction.emoji) == up:
                            if plr[v[0]][1]==2*h-1 and str(reaction.emoji) == up:
                                kon='cannot go further up'
                            elif tab[v[0]][plr[v[0]][0]][plr[v[0]][1]]!='c':
                                kon="You cannot place a block beacause there are leaves below you"
                            elif tab[v[0]][plr[v[0]][0]][plr[v[0]][1]+2]=='np':
                                k=mine(tab[v[0]],plr[v[0]][2],plr[v[0]][0],plr[v[0]][1],plr[v[0]][4],plr[v[0]][3])
                                if k[0].startswith("You do not have enough"):
                                    kon=k[0]
                                else:
                                    plr[v[0]][1]+=2
                                    l=go_to_nth(tab[v[0]],plr[v[0]][0], plr[v[0]][1])
                                    kon=k[0]; tab[v[0]]=l[1]; plr[v[0]][0]=l[2]; plr[v[0]][1]=l[3]
                                    await msg[v[0]][3].edit(content='.\n'+inv_ch(plr[v[0]][2]))
                            elif tab[v[0]][plr[v[0]][0]][plr[v[0]][1]+2]!='c' and tab[v[0]][plr[v[0]][0]][plr[v[0]][1]+2]!='l':
                                kon="There's something in your way"
                            else:
                                k=mine(tab[v[0]],plr[v[0]][2],plr[v[0]][0],plr[v[0]][1],plr[v[0]][4],plr[v[0]][3])
                                if k[0].startswith("You do not have enough"):
                                    kon=k[0]
                                else:
                                    plr[v[0]][1]+=1
                                    kon="Moved one space up and "+k[0]
                                    tab[v[0]]=k[2]
                                    plr[v[0]][2]=k[1]
                                    await msg[v[0]][3].edit(content='.\n'+inv_ch(plr[v[0]][2]))
                        elif tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]+1]=='np':
                            #checking for a nether portal
                            plr[v[0]][0]+=k[0]; plr[v[0]][1]+=1; l=go_to_nth(tab[v[0]],plr[v[0]][0],plr[v[0]][1])
                            kon="Moved "+k[1]+" and went to nether"
                            tab[v[0]]=l[1]; plr[v[0]][0]=l[2]; plr[v[0]][1]=l[3]
                        elif tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]+1]!='c' and tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]+1]!='l':
                            #checking if there's a block in front of your head
                            kon="There\'s something in your way"
                        elif tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]]=='np':
                            plr[v[0]][0]+=k[0]; l=go_to_nth(tab[v[0]],plr[v[0]][0],plr[v[0]][1])
                            kon="Moved "+k[1]+" and went to nether"
                            tab[v[0]]=l[1]; plr[v[0]][0]=l[2]; plr[v[0]][1]=l[3]
                        elif tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]]=='np':
                            plr[v[0]][0]+=k[0]; plr[v[0]][1]+=1; l=go_to_nth(tab[v[0]],plr[v[0]][0],plr[v[0]][1])
                            kon="Moved "+k[1]+" and went to nether"
                            tab[v[0]]=l[1]; plr[v[0]][0]=l[2]; plr[v[0]][1]=l[3]
                        elif ((tab[v[0]][plr[v[0]][0]][plr[v[0]][1]+2]!='c' and tab[v[0]][plr[v[0]][0]][plr[v[0]][1]+2]!='l') or (tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]+2]!='c' and tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]+2]!='l')) and tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]]!='c' and tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]]!='l':
                            #checking if you can climb the block ahead of you
                            kon="There\'s something in your way"
                        elif tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]]!='c' and tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]]!='l' and (tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]+2]=='c' or tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]+2]=='l'):
                            #climbing
                            plr[v[0]][0]+=k[0]
                            plr[v[0]][1]+=1
                            kon="Moved 1 tile "+k[1]
                        elif tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]]!='c' and tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]]!='l':
                            if tab[v[0]][plr[v[0]][0]+k[0]][plr[v[0]][1]+2]=='np':
                                plr[v[0]][0]+=k[0]; plr[v[0]][1]+=2; l=go_to_nth(tab[v[0]],plr[v[0]][0],plr[v[0]][1])
                                kon="Moved "+k[1]+" and went to nether"
                                tab[v[0]]=l[1]; plr[v[0]][0]=l[2]; plr[v[0]][1]=l[3]
                            elif tab[v[0]][plr[v[0]][0]][plr[v[0]][1]+2]=='np':
                                plr[v[0]][1]+=2; l=go_to_nth(tab[v[0]],plr[v[0]][0],plr[v[0]][1])
                                kon="Moved "+k[1]+" and went to nether"
                                tab[v[0]]=l[1]; plr[v[0]][0]=l[2]; plr[v[0]][1]=l[3]
                            else:
                                kon="There\'s something in your way"
                        else:
                            #moving forward
                            plr[v[0]][0]+=k[0]
                            kon="Moved 1 tile "+k[1]
                        #checking if character is falling
                        f=0
                        while tab[v[0]][plr[v[0]][0]][plr[v[0]][1]-1]=='c':
                            plr[v[0]][1]-=1
                            f+=1
                        if f>3:
                            plr[v[0]][6]-=(f-3)
                            await msg[v[0]][2].edit(content="You lost "+str(f-3)+' hp\n'+':heart:'*(plr[v[0]][6]//2)+':broken_heart:'*(plr[v[0]][6]%2)+':white_heart:'*((mx_health-plr[v[0]][6])//2))
                        if tab[v[0]][plr[v[0]][0]][plr[v[0]][1]-1]=='np':
                            plr[v[0]][1]-=1; l=go_to_nth(tab[v[0]],plr[v[0]][0],plr[v[0]][1])
                            kon="Moved "+k[1]+" and went to nether"
                            tab[v[0]]=l[1]; plr[v[0]][0]=l[2]; plr[v[0]][1]=l[3]
                        await msg[v[0]][1].edit(content=kon+'\nheight: '+str(plr[v[0]][1]%(2*h))+'\n'+rea(tab[v[0]],plr[v[0]][0],plr[v[0]][1]))
                        if plr[v[0]][6]<=0:
                            plr[v[0]]=[n//2, int(h*1.5),[0]*len(inv_a),[False]*len(cr), 0, plr[v[0]][5], mx_health]
                            while tab[v[0]][plr[v][0]][plr[v][1]-1]=='c':
                                plr[v[0]][1]-=1
                            await msg[v[0]][2].edit(content="You died\n"+':heart:'*(plr[v[0]][6]//2)+':broken_heart:'*(plr[v[0]][6]%2)+':white_heart:'*((mx_health-plr[v[0]][6])//2))
                    elif str(reaction.emoji) in re:
                        #using items (flint and steel etc.)
                        #mining or placing a block
                        r=switcher.get(str(reaction.emoji))
                        p=plr[v[0]][0]
                        o=plr[v[0]][1]
                        k=mine(tab[v[0]],plr[v[0]][2],p+r[0],o+r[1],plr[v[0]][4],plr[v[0]][3])
                        if k[0]=='Placed sapling':
                            #placing a sapling
                            #checking if sapling is placed above dirt
                            #if yes, grow a tree after a random amount of time
                            if tab[v[0]][p+r[0]][o+r[1]-1]=='d':
                                await msg[v[0]][1].edit(content=k[0]+'\nheight: '+str(plr[v[0]][1]%(2*h))+'\n'+rea(tab[v[0]],plr[v[0]][0],plr[v[0]][1]))
                                #growing a tree
                                await asyncio.sleep(randrange(30,120))
                                if tab[v[0]][p+r[0]][o+r[1]]=='s':
                                    c=randrange(o+r[1]+2,o+r[1]+7)
                                    bo=True
                                    #checking if tree is under something if yes, stop growing further
                                    k[2][p+r[0]][o+r[1]]='v'
                                    for j in range(c,o+r[1],-1):
                                        if tab[v[0]][p+r[0]][j]=='c':
                                            k[2][p+r[0]][j]='v'
                                        else:
                                            c=j-1
                                            bo=False
                                    if bo:
                                        k[2][p+r[0]+1][c-1]='l'; k[2][p+r[0]+1][c]='l'; k[2][p+r[0]+1][c+1]='l'; k[2][p+r[0]+2][c]='l'
                                        k[2][p+r[0]-1][c-1]='l'; k[2][p+r[0]-1][c]='l'; k[2][p+r[0]-1][c+1]='l'; k[2][p+r[0]-2][c]='l'
                                        k[2][p+r[0]][c]='l'; k[2][p+r[0]][c+1]='l'; k[2][p+r[0]][c+2]='l';
                                    else:
                                        k[2][p+r[0]+1][c-1]='l'; k[2][p+r[0]+1][c]='l'; k[2][p+r[0]+2][c]='l'
                                        k[2][p+r[0]-1][c-1]='l'; k[2][p+r[0]-1][c]='l'; k[2][p+r[0]-2][c]='l'
                                        k[2][p+r[0]][c]='l';
                                    k[0]="tree has grown"
                                else:
                                    return
                            else:
                                #sending a message
                                k[0]="You can only place sapling on dirt"
                                k[1][plr[v[0]][4]]+=1
                                k[2][p+r[0]][o+r[1]]='c'
                        tab[v[0]]=k[2]
                        plr[v[0]][2]=k[1]
                        while tab[v[0]][plr[v[0]][0]][plr[v[0]][1]-1]=='c':
                            plr[v[0]][1]-=1
                        #editing message (Placed or mined a block)
                        await msg[v[0]][1].edit(content=k[0]+'\nheight: '+str(plr[v[0]][1]%(2*h))+'\n'+rea(tab[v[0]],plr[v[0]][0],plr[v[0]][1]))
                        await msg[v[0]][3].edit(content='.\n'+inv_ch(plr[v[0]][2]))
                        if plr[v[0]][6]<=0:
                            plr[v[0]]=[n//2,int(h*1.5),[0]*len(inv_a),[False]*len(cr),0,plr[v[0]][5],mx_health]
                            while tab[v][plr[v][0]][plr[v][1]-1]=='c':
                                plr[v[0]][1]-=1
                            await msg[v[0]][2].edit(content="You died\n"+':heart:'*(plr[v[0]][6]//2)+':broken_heart:'*(plr[v[0]][6]%2)+':white_heart:'*((mx_health-plr[v[0]][6])//2))
                        if tab[v[0]][plr[v[0]][0]][plr[v[0]][1]]=='np':
                            l=go_to_nth(tab[v[0]],plr[v[0]][0],plr[v[0]][1])
                            kon="Went to nether"
                            tab[v[0]]=l[1]; plr[v[0]][0]=l[2]; plr[v[0]][1]=l[3]
                if v[1]==3:
                    if str(reaction.emoji) in cr:
                        #crafting
                        k=switcher_c.get(str(reaction.emoji))
                        kon=craft(plr[v[0]][2],k,plr[v[0]][3])
                        await msg[v[0]][3].edit(content=kon+'\n'+inv_ch(plr[v[0]][2]))
                if v[1]==2:
                    if str(reaction.emoji) in food:
                        #eating
                        k=eat(plr[v[0]][2],str(reaction.emoji),plr[v[0]][6])
                        plr[v[0]][6]=k[0]
                        plr[v[0]][2]=k[2]
                        await msg[v[0]][2].edit(content=k[1]+'\n'+':heart:'*(plr[v[0]][6]//2)+':broken_heart:'*(plr[v[0]][6]%2)+':white_heart:'*((mx_health-plr[v[0]][6])//2))
                        await msg[v[0]][3].edit(content='.\n'+inv_ch(plr[v[0]][2]))
                        if plr[v[0]][6]<=0:
                            plr[v[0]]=[n//2,int(h*1.5),[0]*len(inv_a),[False]*len(cr),0,plr[v[0]][5],mx_health]
                            while tab[v][plr[v][0]][plr[v][1]-1]=='c':
                                plr[v[0]][1]-=1
                            await msg[v[0]][2].edit(content="You died\n"+':heart:'*(plr[v[0]][6]//2)+':broken_heart:'*(plr[v[0]][6]%2)+':white_heart:'*((mx_health-plr[v[0]][6])//2))
                


client.run(bot_token)
