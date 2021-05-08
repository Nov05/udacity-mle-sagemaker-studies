import torch
import torch.nn as nn
import torch.nn.functional as F

## TODO: Complete this classifier
class SimpleNet(nn.Module):
    
    ## TODO: Define the init function
    def __init__(self, input_dim, hidden_dim, output_dim):
        '''Defines layers of a neural network.
           :param input_dim: Number of input features
           :param hidden_dim: Size of hidden layer(s)
           :param output_dim: Number of outputs
         '''
        super(SimpleNet, self).__init__()
        
        # define all layers, here
        
        # linear layer (input_dim -> hidden_dim)
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        # liner layer (hidden_dim -> hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        # liner layer (hidden_dim -> output_dim)
        self.fc3 = nn.Linear(hidden_dim, output_dim)
        # dropout layer
        self.dropout = nn.Dropout(0.4)
        # sigmoid layer
        self.sig = nn.Sigmoid()
        
    
    ## TODO: Define the feedforward behavior of the network
    def forward(self, x):
        '''Feedforward behavior of the net.
           :param x: A batch of input features
           :return: A single, sigmoid activated value
         '''
        # your code, here
        
        # add hidden layer, with relu activation function
        x = F.relu(self.fc1(x))
        # add dropout layer
        x = self.dropout(x)
        # add hidden layer
        x = F.relu(self.fc2(x))
        # add dropout layer
        x = self.dropout(x)
        # add hidden layer
        x = F.relu(self.fc3(x))
        # add activation layer
        x = self.sig(x)
        
        return x