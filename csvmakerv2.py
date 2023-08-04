import csv
import team_stats as ts




def create_csv(playerstats, trainingstats, output, squad):
    teamstatmaker = ts.TeamStatMaker()
    team_dict = teamstatmaker.make_dict()

    main_stats = []
    dict_reader = csv.DictReader(open(trainingstats))
    for row in dict_reader:
        main_stats.append(row)
    all_stats = []
    dict_reader = csv.DictReader(open(playerstats))
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


    output = open(output)
    output_list = []

    for line in output.readlines():
        output_list.append(line)           

    stats_reader = open(trainingstats, "r")
    stats_writer = open("csvFiles\int_data.csv", "w")
    stats_reader.readline()
    for i in training_last_stats:
        #print(i)
        line = stats_reader.readline()
        line = line.strip()
        #print(line)
        stats_writer.write(line)
        for j in i:
            
            stats_writer.write(",")
            stats_writer.write(j)
        stats_writer.write("\n")
        

    stats_reader.close()
    stats_writer.close()

    stats_reader = open("csvFiles\int_data.csv", "r")
    stats_writer = open("data\csv_data.csv","a")

    count = 0
    for line in stats_reader.readlines():
        line = line.strip()
        line= line.split(",")
        venue = line.pop(0)

        if venue == "Home":
            op_venue = " Away"
        else:
            op_venue = " Home"

        opponent = line.pop(0) + op_venue
        line.pop(0)

        for value in team_dict[squad + venue]:
            line.append(value)
        for value in team_dict[opponent]:
            line.append(value)

        for i in line:
            stats_writer.write(i)
            stats_writer.write(",")

        
        stats_writer.write(output_list[count])
        count += 1

    stats_reader.close()
    stats_writer.close()

        
        

lolz = open("data\csv_data.csv", "w")

# Saka Stats
training = "csvFilesv2\saka_training_stats.csv"
all = "csvFilesv2\SakaStats.csv"
output = "csvFilesv2\saka_output.csv"
squad = "Arsenal "
create_csv(all, training, output, squad)

# Martinelli Stats

