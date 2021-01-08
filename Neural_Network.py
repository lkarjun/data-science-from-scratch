import numpy as np
from typing import Dict, List, Tuple
from sklearn.preprocessing import StandardScaler

class NeuralNetwork:

    def __init__(self, X: np.array,
                       Y: np.array, 
                       hidden_layer: int = 4,
                       epochs: int = 1000,
                       learning_rate: int = 0.01,
                       standardize: bool = False) -> None:

        print("Welcome To Lk Nueral Network")
        self.X: np.array = X
        self.Y: np.array = Y
        self.hidden_layers: int = hidden_layer
        self.epochs: int = epochs
        self.learning_rate: int = learning_rate
        self.standardize: bool = standardize
        self.layers: Tuple = self._layer_size(self.X, self.Y)
        self.parameters: Dict[np.array] = None
        self.cache: Dict[np.array] = None
        self.grads: Dict[np.array] = None
        self.cost: int = None

    def _layer_size(self, x: np.array, y: np.array) -> Tuple[int]:
        n_x = self.X.shape[0]
        n_h = self.hidden_layers
        n_y = self.Y.shape[0]

        '''return n_x, n_h, n_y order'''
        return n_x, n_h, n_y

    def sigmoid(self, z) -> np.array:
        return 1/(1+np.exp(-z))

    def initialize_parameters(self):
        np.random.seed(2)
        W1:np.array = np.random.randn(self.layers[1], self.layers[0]) * 0.01
        b1:np.array = np.zeros(shape=(self.layers[1], 1))
        W2:np.array = np.random.randn(self.layers[2], self.layers[1]) * 0.01
        b2:np.array = np.zeros(shape=(self.layers[2], 1))

        parameter: Dict[np.array] = {'W1': W1,
                                     'b1': b1,
                                     'W2': W2,
                                     'b2': b2}
        self.parameters = parameter

    def foward_propagate(self):
        W1 = self.parameters['W1']
        b1 = self.parameters['b1']
        W2 = self.parameters['W2']
        b2 = self.parameters['b2']

        Z1 = (np.dot(W1, self.X)) + b1
        A1 = np.tanh(Z1)
        Z2 = (np.dot(W2, A1)) + b2
        A2 = self.sigmoid(Z2)
        
        assert(A2.shape == (1, self.X.shape[1])), "check there is somthing wrong"
        
        cache: Dict[np.array] = {'Z1': Z1,
                                 'Z2': Z2,
                                 'A1': A1,
                                 'A2': A2}
        self.cache = cache
        return A2
    
    def backward_propagate(self):
        m = X.shape[1]
        W1 = self.parameters['W1']
        W2 = self.parameters['W2']

        A1 = self.cache['A1']
        A2 = self.cache['A2']

        dz2 = A2 - self.Y
        dW2 = 1/m * np.dot(dz2, A1.T)
        db2 = 1/m * np.sum(dz2, axis=1, keepdims=True)
        dz1 = np.multiply(np.dot(W2.T, dz2), (1- np.power(A1, 2)))
        dW1 = 1/m * np.dot(dz1, self.X.T)
        db1 = 1/m * np.sum(dz1, axis=1, keepdims=True)

        grads = {'dW1': dW1,
             'dW2': dW2,
             'db1': db1,
             'db2': db2} 
        
        self.grads = grads
    
    def compute_cost(self):
        m = self.Y.shape[1]
        A2 = self.cache['A2']
        cost = (-1/m) * np.sum(self.Y*np.log(A2) + (1-self.Y) * np.log(1-A2))
        self.cost = cost

    def update_parameter(self):
        W1 = self.parameters['W1'] - self.learning_rate * self.grads['dW1']
        b1 = self.parameters['b1'] - self.learning_rate * self.grads['db1']
        W2 = self.parameters['W2'] - self.learning_rate * self.grads['dW2']
        b2 = self.parameters['b2'] - self.learning_rate * self.grads['db2']

        parameter: Dict[np.array] = {'W1': W1,
                                     'b1': b1,
                                     'W2': W2,
                                     'b2': b2}
        
        self.parameter = parameter
    
    def fit(self):
        np.random.seed(0)
        self.initialize_parameters()

        if self.standardize:
            self.X = StandardScaler().fit_transform(self.X)

        for i in range(0, self.epochs):
            self.foward_propagate()
            self.compute_cost()
            self.backward_propagate()
            self.update_parameter()
            if i % 1000 == 0:
                print(f'Cost after iteration {i, self.cost}')
        
        return self.parameters
            





import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

data = make_moons(n_samples=500)
X = data[0]
Y = data[1]
x_train, x_test, y_train, y_test = train_test_split(X, Y)

neural_network = NeuralNetwork(x_train.reshape(2, -1),
                               y_train.reshape(1, -1),
                               epochs = 500,
                               standardize = True)

neural_network.fit()
