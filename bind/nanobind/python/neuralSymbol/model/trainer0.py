import torch
from torch import nn
from torch.utils.data import DataLoader,Dataset
from neuralSymbol.model.Model0 import Model0
from neuralSymbol.model.dataset0 import Dataset0



class Trainer0():
    
    def __init__(self) -> None:
        self.model = Model0()
        self.loss_fn = nn.CrossEntropyLoss()
        self.optimizer0 = torch.optim.SGD(self.model.parameters(), lr=1)
        self.optimizer1 = torch.optim.SGD(self.model.parameters(), lr=0.5)
        self.optimizer2 = torch.optim.SGD(self.model.parameters(), lr=0.01)
        self.optimizer3 = torch.optim.SGD(self.model.parameters(), lr=0.001)
        self._n_epocs= 100000000
        
    def train(self,dataloader: DataLoader):
        self.model.train()
        size = len(dataloader.dataset)
        for epoc in range (self._n_epocs):
            if self._n_epocs< 100000: self.optimizer = self.optimizer0 
            elif  self._n_epocs< 200000: self.optimizer = self.optimizer1 
            elif  self._n_epocs< 300000: self.optimizer = self.optimizer2 
            else :self.optimizer = self.optimizer3 
            for batch, (X, y) in enumerate(dataloader):
                #X, y = X.to(device), y.to(device)

                # Compute prediction error
                pred = self.model(X)
                loss = self.loss_fn(pred, y)
                y_pred= torch.argmax(pred,dim=1)
                
                # Backpropagation
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                if epoc%100 ==0:
                    print(epoc,loss,sum(y_pred==y)/size)
                    if abs(sum(y_pred==y)/size-1) <0.001:
                        return
                   
        
    @staticmethod
    def test():
        dataset = Dataset0()
        dataloader = DataLoader(dataset,len(dataset),shuffle=True)
        
        trainer = Trainer0()
        #trainer.train(dataloader)
        x,y = dataset[6]
        
      
        trainer.train(dataloader)
        path = "./neuralSymbol/model/models/model1.pt"
        
        torch.save(trainer.model.state_dict(), path)
       
                
                
     