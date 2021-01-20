from typing import Dict, List
import numpy as np
from numpy.core.numeric import full



class DeepNeuralNetwork:

    def __init__(self, X: np.array, Y: np.array, hidden_layers: List[int], activations: List[str]) -> None:
        self.X = X
        self.Y = Y
        self.hidden_layers: List[int] = hidden_layers
        self.activation: List[str] = activations
        self.param = None
        self.Layer = None
        self.cache = None
        self.grads = None

    def initialize_parameters(self) -> Dict[str, np.array]:
        Layers = self.layer_size()
        parameters: Dict[str, np.array] = {}

        for i in range(1, len(Layers)):
            parameters["W"+str(i)] = np.random.randn(Layers[i], Layers[i-1]) * 0.1
            parameters["b"+str(i)] = np.zeros(shape=(Layers[i], 1))

        self.param = parameters
        return parameters

    def layer_size(self) -> List[int]:
        Layer_0 = [self.X.shape[0]]
        Layer_last = [self.Y.shape[0]]
        Layer_hidden = self.hidden_layers
        full_layer = (Layer_0 + Layer_hidden) + Layer_last
        self.Layer = full_layer
        return full_layer

    def forward_pass(self) -> Dict[str, np.array]:
        cache: Dict[str, np.array] = {}
        cache['Z1'] = (np.dot(self.param['W1'], 
                        self.X)) + self.param['b1']
        cache['A1'] = np.tanh(cache['Z1'])

        for i in range(2, len(self.Layer)):
            cache['Z'+str(i)] = (np.dot(self.param['W'+str(i)],
                                    cache['A'+str(i-1)])) + self.param['b'+str(i)]
            cache['A'+str(i)] = np.tanh(cache['Z'+str(i)])

        self.cache = cache
        return cache

    
    def backward_pass(self):
        m = self.X.shape[1]
        grads: Dict[str, np.array] = {}
        i = len(self.layer_size()) - 1

        while i > 1:
            grads["dz"+str(i)] = self.cache['A'+str(i)] - self.Y
            grads["dw"+str(i)] = 1/m * np.dot(grads['dz'+str(i)], self.cache['A'+str(i-1)].T)
            grads["db"+str(i)] = 1/m * np.sum(grads['dz'+str(i)], axis=1, keepdims=True)
            i -= 1

        grads['dz1'] = self.cache['A1'] - self.Y
        grads['dw1'] = 1/m * np.dot(grads['dz1'], self.X.T)
        grads['db1'] = 1/m * np.sum(grads['dz1'], axis=1, keepdims=True)

        self.grads = grads

        return grads
    
    def update_parameters(self):
        ...
    
    def fit(self):
        ...
    
    def predict(self):
        ...
    
    def sigmoid(self, z: np.array) -> np.array:
        return 1/(1+np.exp(-z))

    def derivative_of_Activation(self, data: np.array, Activation: str) -> np.array:
        ...

sample_data = np.array([[1,2,3],[2, 6, 8]]).reshape(2,-1)
sample_y = np.array([[0], [1], [3]]).reshape(1, -1)
model = DeepNeuralNetwork(sample_data, sample_y, [10, 10], ['relu', 'sigmoid'])

print(model.layer_size())
from pprint import pprint
pprint(model.initialize_parameters())

pprint(model.forward_pass())
print(len(model.layer_size()) - 1)
print(model.layer_size())
print(sample_y)

pprint(model.backward_pass())