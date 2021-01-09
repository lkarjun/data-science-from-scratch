from typing import Dict, List
import numpy as np
from numpy.core.numeric import full



class DeepNeuralNetwork:

    def __init__(self, X: np.array, Y: np.array, hidden_layers: List[int]) -> None:
        self.X = X
        self.Y = Y
        self.hidden_layers: List[int] = hidden_layers

    def initialize_parameters(self):
        Layers = self.layer_size()
        parameters: Dict[np.array] = {}

        for i in range(1, len(Layers)):
            parameters["W"+str(i)] = np.random.randn(Layers[i], Layers[i-1]) * 0.1
            parameters["b"+str(i)] = np.zeros(shape=(Layers[i], 1))

        return parameters

    def layer_size(self):
        Layer_0 = [self.X.shape[0]]
        Layer_last = [self.Y.shape[0]]
        Layer_hidden = self.hidden_layers
        full_layer = (Layer_0 + Layer_hidden) + Layer_last

        return full_layer

    def forward_pass(self):
        ...
    
    def backward_pass(self):
        ...
    
    def update_parameters(self):
        ...
    
    def fit(self):
        ...
    
    def predict(self):
        ...


sample_data = np.array([[1,2,3],[2,3,4]]).reshape(2,-1)
sample_x = np.array([[0, 1]]).reshape(1, -1)
model = DeepNeuralNetwork(sample_data, sample_x, [2,64, 64, 2])

print(model.layer_size())
from pprint import pprint
pprint(model.initialize_parameters())