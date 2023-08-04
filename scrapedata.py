import pandas as pd 
import numpy as np
import math
import copy
import team_stats as ts


url_21 = 'https://fbref.com/en/players/bc7dc64d/matchlogs/2020-2021/c9/Bukayo-Saka-Match-Logs'
url_22 = 'https://fbref.com/en/players/bc7dc64d/matchlogs/2021-2022/c9/Bukayo-Saka-Match-Logs'
url_23 = 'https://fbref.com/en/players/bc7dc64d/matchlogs/2022-2023/c9/Bukayo-Saka-Match-Logs'

teamstatmaker = ts.TeamStatMaker()
team_dict = teamstatmaker.make_dict()

playerstats = []
trainingstats = []

for i in [url_21, url_22, url_23]:
    df = pd.read_html(i)

    plstats = df[0]
    plstats = plstats.iloc[0:38, 2:35].to_numpy()

    # Deletes Position and Start

    plstats = np.delete(plstats, (5,6), axis = 1)

    #Checks to see if stat is valid (not NaN and had gametime)
    for j in plstats.tolist():
        if j[5] != 'On matchday squad, but did not play' and not math.isnan(float(j[5])): 
            temp1 = copy.deepcopy(j)
            playerstats.append(temp1)
            if i != url_21:
                temp2 = copy.deepcopy(j)
                trainingstats.append(temp2)




for j in [playerstats, trainingstats]:
    for i in j:
        # Remove Matchweek
        temp = i[0]
        temp = temp.split(" ")
        i[0] = int(temp[1])

        # Calculate Result
        temp = i[2]
        temp = temp.split(" ")
        temp = temp[1]
        temp = temp.split("–")
        i[2] =(int(temp[0]) - int(temp[1]))

        # Turn all elements into strings
        for k in range(len(i)):
            i[k] = str(i[k])
        
        # Rearranges List and concates location onto team name
        venue = i.pop(1)
        temp1 = i.pop(0)
        temp2 = i.pop(0)
        
        i.insert(2, temp2)
        i.insert(2, temp1)

        if venue == "Home":
            op_venue = "Away"
        else:
            op_venue = "Home"


        i[0] = i[0] + " " + venue
        i[1] = i[1] + " " + op_venue


# Collecting the correct outputs from the game.
outputs = []
for i in range(1, len(trainingstats)):
    out = []
    for j in [5,6,9,10,14,20,23,25,27]:
        out.append(playerstats[-i][j])
    outputs.append(out)


# Adds the stats from the last game for each game
# for i in trainingstats:
#     print(i)
#     print("")

for i in range(len(trainingstats) - 1, 0, -1):
    
    trainingstats[i][2:] = trainingstats[i-1][2:]
    #print(trainingstats[i-1][2])
    trainingstats[i].insert(2, trainingstats[i-1][1])
    
trainingstats.pop(0)




# Adds stats from the last time they played the team 


for i in range(0, len(trainingstats)):
    opponent = trainingstats[-i][1]
    for j in reversed(playerstats):
        if opponent == j[1]:
            for k in j[2:]:
                trainingstats[-i].append(k)
            playerstats.remove(j)
            break
        

# Add stats from each team
for i in trainingstats:
    team = i[:3][0]
    opponent = i[:3][1]
    last = i[:3][2]
    for j in range(3):
        for item in team_dict[i[:3][j]]:
            i.append(item)

count = 0
for output in reversed(outputs):
    for i in output:
        trainingstats[count].append(i)
    count+= 1

print(trainingstats[0])
print(trainingstats[27])
print(trainingstats[63])
print(trainingstats[-1])









    