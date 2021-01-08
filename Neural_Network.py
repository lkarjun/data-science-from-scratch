import numpy as np
from typing import Dict, List, Tuple

from numpy.core.fromnumeric import shape

class NeuralNetwork:

    def __init__(self, X: np.array,
                       Y: np.array, 
                       hidden_layer: List[int] = 32,
                       epochs: int = 1000,
                       learning_rate: int = 0.01,
                       standardize: bool = False) -> None:

        print("Welcome To Lk Nueral Network")
        self.X: np.array = X
        self.Y: np.array = Y
        self.hidden_layer: List[int] = hidden_layer
        self.epochs: int = epochs
        self.learning_rate: int = learning_rate
        self.standardize: bool = standardize
        self.layers: Tuple = self._layer_size(self.X, self.Y)

    def _layer_size(self, x: np.array, y: np.array) -> Tuple[float]:
        n_x = self.X.shape[0]
        n_h = self.hidden_layer[-1]
        n_y = self.Y.shape[0]

        '''return n_x, n_h, n_y order'''
        return n_x, n_h, n_y

    def initialize_parameters(self) -> Dict[np.array]:
        np.random.seed(2)
        W1:np.array = np.random.randn(self.layers[1], self.layers[0]) * 0.01
        b1:np.array = np.zeros(shape=(self.layers[1], 1))
        W2:np.array = np.random.randn(self.layers[2], self.layers[1]) * 0.01
        b2:np.array = np.zeros(shape=(self.layers[2], 1))

        parameter: Dict[np.array] = {'W1': W1,
                                     'b1': b1,
                                     'W2': W2,
                                     'b2': b2}
        return parameter

    def foward_propagate(self):
        ...

c = NeuralNetwork()