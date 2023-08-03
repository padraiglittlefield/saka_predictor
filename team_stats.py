import csv

class TeamStatMaker:
    def team_normalizer(self, dict1, standing1, standing2):
        reader1 = csv.DictReader(standing1)
        reader2 = csv.DictReader(standing2)

        for row in reader1:
            dict1[row["Team"]] = []
            for key,value in row.items():
                if key != "Team":
                    dict1[row["Team"]].append(value)

        #print(dict1["Arsenal Away"])

        for row in reader2:
            try:
                last = dict1[row["Team"]]
                i = 0
                for key,value in row.items():
                    if key != "Team":
                        
                        val_of = int(last[i])    
                        last[i] = str( val_of + int(value))
                        i += 1
            except:
                dict1[row["Team"]] = []
                for key,value in row.items():
                    if key != "Team":
                        dict1[row["Team"]].append(value)

        to_norm = []
        for key,value in dict1.items():
            to_norm.append(value)

        #print(to_norm)

        max_values = []
        for i in range(9):
            max = 0
            for j in to_norm:
                if int(j[i]) > max:
                    max = int(j[i])
            max_values.append(max)

        for i in to_norm:
            for j in range(9):
                num = round(int(i[j])/max_values[j], 3)
                i[j] = str(num)
                

        count = 0
        for key,value in dict1.items():
            dict1[key] = to_norm[count]
            count += 1
        
        return dict1


    def make_dict(self):
        dicts = {}
        std1= open("csvFiles\\21_22_prem_away.csv", "r")
        std2 = open("csvFiles\\22_23_prem_away.csv", "r")
        dicts = self.team_normalizer(dicts, std1, std2)

        dicts2 = {}
        std1= open("csvFiles\\21_22_prem_home.csv", "r")
        std2 = open("csvFiles\\22_23_prem_home.csv", "r")
        dicts2 = self.team_normalizer(dicts2, std1, std2)


        for key,value in dicts2.items():
            dicts[key] = value

        return dicts







