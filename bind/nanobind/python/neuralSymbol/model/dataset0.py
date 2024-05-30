from torch.utils.data import ConcatDataset, Dataset
import torch


from neuralSymbol.model.getInstance0 import GetInstance0
class Dataset0(Dataset):
    
    def __init__(self) -> None:
        super().__init__()
        self.x, self.y = GetInstance0.generate() 
        self.x =self.x.to(torch.float)  
        self.x =self.x.to(torch.float)  
        self.n_samples = self.x.shape[0]
        
    def __getitem__(self,index):
        return self.x[index], self.y[index]
    
    def __len__(self):
        return self.n_samples
        