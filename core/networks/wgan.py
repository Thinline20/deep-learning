import torch.nn as nn
import torch.nn.functional as F

class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, X):
        return X

class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, X):
        return X
        