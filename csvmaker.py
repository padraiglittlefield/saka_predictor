import pandas as pd
import csv
import team_stats as ts
# file_out = pd.read_csv("csvFiles\\training_stats_22.csv")
# print(file_out)




def create_data(training_stats, saka_output, prem_away, prem_home):
    squad = "Arsenal"
    team_dict = {}
    teamstatmaker = ts.TeamStatMaker()
    team_dict = teamstatmaker.make_dict()
    # for i in [prem_away, prem_home]: 
    #     dict_reader = csv.DictReader(open(i))
    #     for row in dict_reader:
    #         team_name = ""
    #         stats = []
            
    #         for key,value in row.items():
    #             if key == "Team":
    #                 team_name = value
    #             else:
    #                 stats.append(value)
    #         team_dict[team_name] = stats



    output = open(saka_output)
    output_list = []

    for line in output.readlines():
        output_list.append(line)

    print(output_list)




    stats_reader = open(training_stats, "r")                
    dataset = open("csvFiles\datasetv1.csv", "a")
    count = 0
    for line in stats_reader.readlines():
        line = line.strip()
        game_stats = line.split(",")

        venue = game_stats[1]

        if venue == "Away":
            opponent_venue = "Home"
        else:
            opponent_venue = "Away"
        

        opponent = game_stats[2]
        

        last_opponent = game_stats[3]

        good_team = team_dict[squad + " " + venue]
        opponent_team = team_dict[opponent + " " + opponent_venue]


        for i in range(3):
            print(game_stats.pop(1))
        game_stats.pop(2)

        for i in [game_stats, good_team, opponent_team]:
            for item in i:
                
                dataset.write(item)
                dataset.write(",")
        
        for item in output_list[count]:
            dataset.write(item)

        count += 1
        
        
def main():
    training_stats_21 = "csvFiles\\saka_training_stats_22.csv"
    prem_away_21 = "csvFiles\\21_22_prem_away.csv"
    prem_home_21 = "csvFiles\\21_22_prem_home.csv"
    saka_output_21 = "csvFiles\\21_22_saka_output.csv"
    create_data(training_stats_21, saka_output_21, prem_away_21, prem_home_21)

    training_stats_22 = "csvFiles\\saka_training_stats_23.csv"
    prem_away_22 = "csvFiles\\22_23_prem_away.csv"
    prem_home_22 = "csvFiles\\22_23_prem_home.csv"
    saka_output_22 = "csvFiles\\22_23_saka_output.csv"
    create_data(training_stats_22, saka_output_22, prem_away_22, prem_home_22)

main()