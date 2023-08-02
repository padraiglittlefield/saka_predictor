from torch import nn, save, load
from torch.optim import Adam
from torch.utils.data import DataLoader
from dataset import SoccerDataset


saka_dataset = SoccerDataset("data\dataset.csv")
trainloader = DataLoader(saka_dataset, batch_size= 60, shuffle=True)

class SakaPredictor(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(127, 32),
            nn.ReLU(),
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64,64),
            nn.ReLU(),
            nn.Linear(64,4)
        )
    
    def forward(self, x):
        return self.model(x)

# Instance of neural network
prd = SakaPredictor().to('cpu')
opt = Adam(prd.parameters(),lr=1e-9)
loss_fn = nn.CrossEntropyLoss()


# Training flow
if __name__ == "__main__":
    print("Starting...")
    for epoch in range(100):
        for batch in trainloader:
            x,y = batch
            x, y = x.to('cpu'), y.to('cpu')
            yhat = prd(x)
            loss = loss_fn(yhat, y)
            opt.zero_grad()
            loss.backward()
            opt.step()

        print(f"Epoch: {epoch} loss is {loss.item()}")

    with open('model_state.pt', 'wb') as f:
        save(prd.state_dict(), f)
 




