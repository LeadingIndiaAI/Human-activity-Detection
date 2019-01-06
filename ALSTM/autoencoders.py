import torch.nn as nn
import torch.nn.functional as F

class LinearAutoencoder(nn.Module):
    def __init__(self):
        super(LinearAutoencoder,self).__init__()

        self.encoder = nn.Sequential(
            nn.Linear(768000,1024),
            nn.ReLU()
        )

        self.decoder = nn.Sequential(
            nn.Linear(1024,768000),
            nn.Tanh()
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x