import pandas as pd
import torch
from torch.utils.data import Dataset

#"data\dataset.csv"
class SoccerDataset(Dataset):

    def __init__(self, file_name):
        file_out  = pd.read_csv(file_name)
        x = file_out.iloc[0:77, 0:127].to_numpy()
        y = file_out.iloc[0:77, 127:131].to_numpy()

        self.X_train = torch.tensor(x, dtype=torch.float32)
        self.Y_train = torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return len(self.Y_train)

    def __getitem__(self, index):
        return self.X_train[index], self.Y_train[index]

        

# file_out  = pd.read_csv("data\dataset.csv")
# x = file_out.iloc[0:77, 0:127].to_numpy()
# y = file_out.iloc[0:77, 127:131].va

