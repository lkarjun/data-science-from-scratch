from typing import Dict, List
import numpy as np
from numpy.core.numeric import full



class DeepNeuralNetwork:

    def __init__(self, X: np.array, Y: np.array, hidden_layers: List[int]) -> None:
        self.X = X
        self.Y = Y
        self.hidden_layers: List[int] = hidden_layers
        self.param = None
        self.Layer = None
        self.cache = None

    def initialize_parameters(self):
        Layers = self.layer_size()
        parameters: Dict[np.array] = {}

        for i in range(1, len(Layers)):
            parameters["W"+str(i)] = np.random.randn(Layers[i], Layers[i-1]) * 0.1
            parameters["b"+str(i)] = np.zeros(shape=(Layers[i], 1))

        self.param = parameters
        return parameters

    def layer_size(self):
        Layer_0 = [self.X.shape[0]]
        Layer_last = [self.Y.shape[0]]
        Layer_hidden = self.hidden_layers
        full_layer = (Layer_0 + Layer_hidden) + Layer_last
        self.Layer = full_layer
        return full_layer

    def forward_pass(self):
        cache: Dict[np.array] = {}
        cache['Z1'] = (np.dot(self.param['W1'], 
                        self.X)) + self.param['b1']
        cache['A1'] = np.tanh(cache['Z1'])

        print('=' * 30)
        print(cache)
        print('=' * 30)
        for i in range(2, len(self.Layer)):
            cache['Z'+str(i)] = (np.dot(self.param['W'+str(i)],
                                    cache['A'+str(i-1)])) + self.param['b'+str(i)]
            cache['A'+str(i)] = np.tanh(cache['Z'+str(i)])

        self.cache = cache
        return cache

    
    def backward_pass(self):
        ...
    
    def update_parameters(self):
        ...
    
    def fit(self):
        ...
    
    def predict(self):
        ...
    
    def sigmoid(self, z):
        return 1/(1+np.exp(-z))


sample_data = np.array([[1,2,3],[2, 6, 8]]).reshape(2,-1)
sample_y = np.array([[0, 1]]).reshape(1, -1)
model = DeepNeuralNetwork(sample_data, sample_y, [4, 10,20, 10, 3])

print(model.layer_size())
from pprint import pprint
pprint(model.initialize_parameters())

pprint(model.forward_pass())