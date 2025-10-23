import torch
import torch.nn as nn

class LSTMRUL(nn.Module):
    def __init__(self, in_dim=1, hid_dim=64, layers=2):
        super().__init__()
        self.lstm = nn.LSTM(in_dim, hid_dim, layers, batch_first=True)
        self.fc = nn.Sequential(
            nn.Linear(hid_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 1)  # RUL output (hours)
        )
    def forward(self, x):
        # x: (B, T, in_dim)
        out, _ = self.lstm(x)
        h = out[:, -1, :]            # last timestep embedding
        return self.fc(h).squeeze(-1)

# training loop sketch
# model = LSTMRUL(); loss=nn.MSELoss(); optimizer=torch.optim.Adam(model.parameters())
# for batch in dataloader: optimizer.zero_grad(); pred=model(batch['seq']); loss(pred,batch['rul']).backward(); optimizer.step()