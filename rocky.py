import random as r
import pandas as pd
nb_players=1
nb_plays=1
occurence={"rock":0,"scissors":0,"paper":0,"draw":0}
affich=False
while nb_players % 2 ==1:
    nb_players = int(input("choose a pair numbs of players: "))
if nb_players<25:
    affich=True


while ((nb_plays!=1) &  (nb_plays!=nb_players-1)):
    nb_plays = int(input("choose the numbers of plays each round 1 or "+str(nb_players-1)+" : "))

nb_rounds = int(input("choose the number of rounds for each duel : "))


def affich_player(player):
    print(str(player[0])+" his id :"+str(player[1])+"  has played "+str(player[2])+" games with a history of :")
    print()
    for dic in player[3:]:
        for p,k in dic.items():
            print(p + " : "+k,end=" , ")
        print("\n")

def next_play_setup(list_scores):
    weakest_link= float('inf')
    weakest_link_index= float('inf')
    for j,k in list_scores.items():
        if (k < weakest_link) and (j not in losing_players):
            weakest_link=k
            weakest_link_index=[j]
        elif k == weakest_link and (j not in losing_players):
            weakest_link_index.append(j)
    return(r.choice(weakest_link_index))


def round_result(player1,player2):
    results = { "rock":{"paper":0,"scissors":1,"rock":0.5},"paper":{"scissors":0,"rock":1,"paper":0.5},"scissors":{"rock":0,"paper":1,"scissors":0.5}}
    if results[player1][player2]==1:
        occurence[player1]+=1
        return  1
    elif results[player1][player2]==0.5:
        occurence["draw"]+=1
        return  0.5
    else:
        occurence[player2]+=1
        return  2

def affich1(p1,p2,way_affich, line1):
    nb_line = len(line1)
    if way_affich==0:
        line1 = line1 +p1[0]+" Vs "+p2[0]+"    "
    elif way_affich==1:
        line1 = line1 +"p"+ str(p1[1]+1)+" Vs "+"p"+str(p2[1]+1)+"    "
    return nb_line,line1

def affich2(p1_score,p2_score,nb_line,way_affich,line2):
    if way_affich==0:
        line2=line2 +(nb_line-len(line2)+4)*" "+p1_score+10*" "+p2_score
    elif way_affich==1:
        line2=line2+(nb_line-len(line2)+1)*" "+p1_score+5*" "+p2_score
    return line2.find(p1_score,nb_line),line2

def affich3(winner,way_affich,index,line3):   
    if way_affich==0:
        line3= line3 + (index-len(line3)+2)*" "+winner # ! hedhi nrmlment titbaddl
    elif way_affich ==1:
        line3= line3 + (index-len(line3))*" "+winner  
    return line3
    



def condition(p1_score,p2_score,round_calcul):
    if (nb_rounds-round_calcul-(p1_score-p2_score)<0 and nb_rounds>=round_calcul):
        return False
    elif (nb_rounds-round_calcul-(p2_score-p1_score)<0 and nb_rounds>=round_calcul):
        return False
    elif (nb_rounds<=round_calcul and p2_score!=p1_score):
        return False
    else:
        return True



def play(player1,player2,game_number,way_affich,line1,line2,line3): 
    choices = ["rock","paper","scissors"]
    p1_score=0
    p2_score=0
    round_calcul = 0
    nb_line,line1 =affich1(player1,player2,way_affich,line1)
    while condition(p1_score,p2_score,round_calcul):
        round_calcul+=1
        choice1= r.choice(choices)
        choice2= r.choice(choices)
        result= round_result(choice1,choice2)
        if result==1:
            player1[game_number+2]["round"+str(round_calcul)]=choice1 +" VS "+ choice2 +" : W"
            player2[game_number+2]["round"+str(round_calcul)]=choice2 +" VS "+ choice1 +" : L"
            p1_score+=1
        elif result==2:
            player1[game_number+2]["round"+str(round_calcul)]=choice1 +" VS "+ choice2 +" : L"
            player2[game_number+2]["round"+str(round_calcul)]=choice2 +" VS "+ choice1 +" : W"
            p2_score+=1
        else:
            player1[game_number+2]["round"+str(round_calcul)]=choice1 +" VS "+ choice2 +" : D"
            player2[game_number+2]["round"+str(round_calcul)]=choice2 +" VS "+ choice1 +" : D"
    index,line2 = affich2(str(p1_score),str(p2_score),nb_line,way_affich,line2)
    if p1_score>p2_score:
        line3= affich3(player1[0],way_affich,index,line3)
        if round_calcul<=nb_rounds:
            p1_score=nb_rounds-round_calcul+1
        else:
            p1_score=0
        return [player2,[player1,p1_score],[line1,line2,line3]]
    elif p2_score>p1_score:
        line3 =affich3(player2[0],way_affich,index,line3)
        if round_calcul<=nb_rounds:
            p2_score=nb_rounds-round_calcul+1
        else:
            p2_score=0
        return [player1,[player2,p2_score],[line1,line2,line3]]
        



nb_players_list = []
list_scores={}
for id in range(nb_players):
    nb_players_list.append(["player"+str(id+1),id,0])

def condition_main(count):
    if len(nb_players_list)==3:
        return False
    elif (count*2>=len(nb_players_list) ):
        return False
    elif True:
        return True


losing_players=[]
losing_players_data=[]
plays=1
while  len(nb_players_list)>1:    #chaque play                # rodhom player1 w 2 , num of game played ymkn ytna77a , list of score 3awdhha bil gnum of game played
             # numb of games
    line1="Players : ";line2="Score   : ";line3="Winner  : "
    count=0         # numb of players who played in each game
    played=[]      # list of feha l id t3 played_players the ones done for this round  
              # to iterate the list 
    #print("--------------------")
    #print("game : "+str(plays))
    if len(nb_players_list)>14:
        way_affich=1
    else:
        way_affich=0
        
    while condition_main(count): #(count*2 <len(nb_players_list) and len(nb_players_list)!=3) and (len(nb_players_list)!=3 and count!=1):## :
        #print(played)
        player_index  =  r.choice([i for i in range(0,len(nb_players_list)) if i not in played])   # 1st player
        player=nb_players_list[player_index]
        played.append(player_index)   # played player list for that game

        num_player_against  =  r.choice([i for i in range(0,len(nb_players_list)) if i not in played])        #2nd one
        played.append(num_player_against)  # played player list for that game    

        player[2]+=1  # +1 l 3dad l atra7 l l3bhom
        nb_players_list[num_player_against][2]+=1  # kif kif
            
        player.append({"game"+str(plays):"Vs "+nb_players_list[num_player_against][0]})   # add in the dic game info 
        nb_players_list[num_player_against].append({"game"+str(plays):"Vs "+player[0] })  # like wise 
        
        
        list_result= play(player,nb_players_list[num_player_against],plays,way_affich,line1,line2,line3)     #gameplay
        line1,line2,line3 = list_result[2]         
        try:
            list_scores[list_result[1][0][1]]+=list_result[1][1]   
        except:
            list_scores[list_result[1][0][1]]=list_result[1][1] # initiate the player score 
        
        count+=1    # adding to the count DOES ACTUALLY deppend on the condtion

        losing_players.append(list_result[0][1])        # list of losing players
        losing_players_data.append(list_result[0])

    plays=plays+1


    
    nb_players_list = [x for x in nb_players_list if x[1] not in losing_players]

    if affich:
        for line in list_result[2]:
            print(line)
        print()
        print(len(list_result[2][0])*"-")
        print()
    if len(nb_players_list)==1:
        break
    elif (len(nb_players_list)%2==1) and(len(nb_players_list)>1) :   # if impaire get rid of the weak link
        unlucky_player_index = next_play_setup(list_scores)
        
        losing_players.append(unlucky_player_index)
        for player in nb_players_list:
            if player[1]==unlucky_player_index:
                losing_players_data.append(player)
                if affich:
                    print("the player eliminated this round is : "+player[0])
                    print("-"*20)
                    print()
        nb_players_list = [x for x in nb_players_list if x[1] != unlucky_player_index]


print("THE WINNER IS : \n")
chosed = nb_players_list[0]
affich_player(chosed)


k=sum([k for k in occurence.values()])
print(occurence)
df=pd.DataFrame(list(occurence.items()),columns=['i','Occurence'])
df.set_index(['i'], inplace=True)
df['Freq']=df['Occurence']/k
df['P({i})']='{0:.3f}'.format(1/3)
print(df)
history= input("press 'yes' to see the history of all the player :  ")
if history=="yes":
    for player in losing_players_data:
        affich_player(player)

x=-1
while ((x>nb_players) or (x<1)):
    dic={"rock":0,"scissors":0,"paper":0,"draw":0}
    x = int(input("put the number of the player u wanna see his own probability  :  "))-1

k=0
dataa=[]
cont=0
for player in losing_players_data:
    
    if player[1]==x:
        chosed = player 
        for data in player[3:]:
            dataa=list(data.values())

            for d in dataa[1:]: 
                if d[-1]=='D':
                    dic["draw"]+=1 
                elif d[0] == "s":
                    dic["scissors"]+=1
                elif  d[0] == "r":
                    dic["rock"]+=1
                elif  d[0] == "p":
                    dic["paper"]+=1            
        break


affich_player(chosed)

k=sum([k for k in dic.values()])
df=pd.DataFrame(list(dic.items()),columns=['i','Occurence'])
df.set_index(['i'], inplace=True)
df['Freq']=df['Occurence']/k
df['P({i})']='{0:.3f}'.format(1/3)
print(df)
