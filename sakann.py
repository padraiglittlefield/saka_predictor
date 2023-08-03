# Import dependencies
import torch 
from PIL import Image
from torch import nn, save, load
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
from dataset import SoccerDataset


saka_dataset = SoccerDataset("data\dataset.csv")
trainloader = DataLoader(saka_dataset, batch_size= 30, shuffle=True)

class SakaPredictor(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(127, 64),
            nn.LeakyReLU(),
            nn.Linear(64, 64),
            nn.LeakyReLU(),
            nn.Linear(64,64),
            nn.LeakyReLU(),
            nn.Linear(64,64),
            nn.LeakyReLU(),
            nn.Linear(64,64),
            nn.LeakyReLU(),
            nn.Linear(64,64),
            nn.LeakyReLU(),
            nn.Linear(64,4)
        )
    
    def forward(self, x):
        return self.model(x)

# Instance of neural network
prd = SakaPredictor().to('cuda')
opt = Adam(prd.parameters(),lr=1e-3)
loss_fn = nn.MSELoss()


# Training flow
if __name__ == "__main__":
    print("Starting...")
    # lowest_loss = 100
    # for epoch in range(1000):
    #     for batch in trainloader:
    #         x,y = batch
    #         x, y = x.to('cuda'), y.to('cuda')
    #         yhat = prd(x)
    #         loss = loss_fn(yhat, y)

    #         if loss < lowest_loss:
    #             lowest_loss = loss
    #             with open('model_state.pt', 'wb') as f:
    #                 save(prd.state_dict(), f)

    #         opt.zero_grad()
    #         loss.backward()
    #         opt.step()

    #     print(f"Epoch: {epoch} loss is {loss.item()}")
        # print(lowest_loss)
        # with open('model_state.pt', 'wb') as f:
        #     save(prd.state_dict(), f)

        # print(lowest_loss)
    with open('model_state.pt', 'rb') as f: 
        prd.load_state_dict(load(f))  


    stat = "18,0,90,6,5,0,0,0,1,0,0,0,0,0,0,0,0,26,35,74.3,431,98,13,15,86.7,12,15,80,1,2,50,0,0.1,0.1,3,1,3,1,3,0,0,0,0,0,0,1,0,1,0,0,0,0,0,2,0,90,9,8,0,0,1,0,0,2,1,0,0,1,0,0,33,41,80.5,566,115,18,19,94.7,12,13,92.3,3,5,60,0,0.3,0.2,5,0,4,3,2,1,1,1,0,0,0,0,0,0,1,0,1,0,1,2,0,2,1,19,12,3,4,35,18,17,39,8,19,12,1,6,37,25,12,37"
    stat = stat.split(",")
    actual = "0,1,1,0"
    stats = []
    for i in stat:
        stats.append(float(i))
    
    
    stat_tensor = torch.tensor(stats, dtype=torch.float32)
    stat_tensor = stat_tensor.to('cuda')
    print((prd(stat_tensor)))
 




