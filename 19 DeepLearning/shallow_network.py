import numpy as np

def layer_sizes(X, Y):
    n_x = X.shape[0]
    n_h = 20
    n_y = Y.shape[0]

    return (n_x, n_h, n_y)

def sigmoid(z):
    return 1/(1+np.exp(-z))

def initialize_parameters(n_x, n_h, n_y):
    np.random.seed(2)

    W1 = np.random.randn(n_h, n_x) * 0.1
    b1 = np.zeros(shape=(n_h, 1))
    W2 = np.random.randn(n_y, n_h) * 0.1
    b2 = np.zeros(shape=(n_y, 1))
      
    assert (W1.shape == (n_h, n_x))
    assert (b1.shape == (n_h, 1))
    assert (W2.shape == (n_y, n_h))
    assert (b2.shape == (n_y, 1))
    
    return {'W1':W1, 'W2':W2, 'b1':b1, 'b2':b2}


def compute_cost(a2, Y, parameters):
    m = Y.shape[1]
    # logprobs = np.multiply(np.log(A2),Y)+np.multiply((1-Y),np.log(1-A2))
    # cost = -1/m * np.sum(logprobs)
    cost = (-1/m) * np.sum(Y*np.log(a2) + (1-Y) * np.log(1-a2))
    return cost

def forward_propagation(X, parameters):
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']

    z1 = (np.dot(W1, X)) + b1
    a1 = np.tanh(z1)
    z2 = (np.dot(W2, a1)) + b2
    a2 = sigmoid(z2)

    assert(a2.shape == (1, X.shape[1])), "check there is somthing wrong"

    cache = {'Z1':z1, 'A1': a1, 'Z2': z2, 'A2': a2}

    return a2, cache


def backward_propagation(parameters, cache, X, Y):
    m = X.shape[1]
    W1 = parameters['W1']
    W2 = parameters['W2']

    A1 = cache['A1']
    A2 = cache['A2']

    dz2 = A2 - Y
    dW2 = 1/m * np.dot(dz2, A1.T)
    db2 = 1/m * np.sum(dz2, axis=1, keepdims=True)
    dz1 = np.multiply(np.dot(W2.T, dz2), (1- np.power(A1, 2)))
    dW1 = 1/m * np.dot(dz1, X.T)
    db1 = 1/m * np.sum(dz1, axis=1, keepdims=True)

    grads = {'dW1': dW1,
             'dW2': dW2,
             'db1': db1,
             'db2': db2}  

    return grads


def update_parameters(parameters, grads, learning_rate=0.001):
    W1 = parameters['W1']
    W2 = parameters['W2']
    b1 = parameters['b1']
    b2 = parameters['b2']

    dw1 = grads['dW1']
    dw2 = grads['dW2']
    db1 = grads['db1']
    db2 = grads['db2']

    W1 = W1 - learning_rate * dw1
    W2 = W2 - learning_rate * dw2
    b1 = b1 - learning_rate * db1
    b2 = b2 - learning_rate * db2

    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    
    return parameters


def nn_model(X, Y, n_h, num_iteration=10000, print_cost=False):
    np.random.seed(0)
    n_x, _ , n_y = layer_sizes(X, Y)
    parameters = initialize_parameters(n_x, n_h, n_y)

    for i in range(0, num_iteration):
        A2, cache = forward_propagation(X, parameters)
        cost = compute_cost(A2, Y, parameters)
        grads = backward_propagation(parameters, cache, X, Y)
        parameters = update_parameters(parameters=parameters, grads=grads)
        if i % 1000 == 0:
            print(f'Cost after iteration {i, cost}')
    
    return parameters