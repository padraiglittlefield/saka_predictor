import pandas as pd 
import csv
import team_stats as ts



teamstatmaker = ts.TeamStatMaker()
team_dict = teamstatmaker.make_dict()



main_stats = []
dict_reader = csv.DictReader(open("csvFiles\mart_training_stats.csv"))
for row in dict_reader:
    main_stats.append(row)
    print(row)
    break




all_stats = []
dict_reader = csv.DictReader(open("csvFiles\MartStats.csv"))
for row in dict_reader:
    all_stats.append(row)
    
    



training_last_stats = []
for i in reversed(main_stats):
    last= (i["Last Opponent"].split(" "))[0:-1]

    
    try:
        last = last[0] + " " + last[1]
    except:
        last = last[0]

    last_stats = []
    for j in reversed(all_stats):
        
        if j["Opponent"] == last:
           # print(f"Last:{last}")
            for key, value in j.items():
                if key not in ["Total","Venue","Opponent"]:
                    last_stats.append(value)
            all_stats.remove(j)
            break
    training_last_stats.append(last_stats)
    #print(last_stats)


            

stats_reader = open("csvFiles\mart_training_stats_copy.csv", "r")
stats_writer = open("csvFiles\mart_data.csv", "w")
stats_reader.readline()
for i in training_last_stats:
    print(i)
    line = stats_reader.readline()
    line = line.strip()
    print(line)
    stats_writer.write(line)
    for j in i:
        
        stats_writer.write(",")
        stats_writer.write(j)
    stats_writer.write("\n")
    

stats_reader.close()
stats_writer.close()

stats_reader = open("csvFiles\mart_data.csv", "r")
stats_writer = open("data\datasetv2.csv","w")

for line in stats_reader.readlines():
    line = line.strip()
    line= line.split(",")
    venue = line.pop(1)

    if venue == "Home":
        op_venue = " Away"
    else:
        op_venue = " Home"

    opponent = line.pop(2) + op_venue
    line.pop(2)

    for value in team_dict["Arsenal " + venue]:
        line.append(value)
    for value in team_dict[opponent]:
        line.append(value)

    for i in line:
        stats_writer.write(i)
        stats_writer.write(",")
    stats_writer.write("\n")

stats_reader.close()
stats_writer.close()

    
    

    