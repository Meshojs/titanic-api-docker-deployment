import torch.nn as nn

class Model(nn.Module):
    def __init__(self, infeatures, hidden=64, outfeature=1):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(infeatures, hidden),
            nn.BatchNorm1d(hidden), 
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden, hidden // 2),
            nn.BatchNorm1d(hidden // 2),  
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden // 2, outfeature),
        )

    def forward(self, x):
        return self.network(x)


