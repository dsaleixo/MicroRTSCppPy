
import torch
from torch import nn

from neuralSymbol.model.getInstance0 import GetInstance0

class Model0(nn.Module):
    
    def __init__(self):
        
        self._n_inputs =8*8*2
        self._n_hidden0 = 20
        self._n_hidden1 = 20
        self._n_hidden2 = 20
        self._n_outputs = len(GetInstance0.action_label)
        
        super(Model0, self).__init__()
       
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(self._n_inputs, self._n_hidden0),
            nn.ReLU(), 
            nn.Linear(self._n_hidden0, self._n_hidden1),
            nn.ReLU(),
            nn.Linear(self._n_hidden1, self._n_hidden2),
            nn.ReLU(),
            nn.Linear(self._n_hidden2, self._n_outputs)
        )
    
    
    def forward(self, x):
        
        x = self.flatten(x)
        
        logits = self.linear_relu_stack(x)
        return logits
    
