from linearalgebra import Vector, dot
import math
from typing import List

def binary_encode(x: int) -> Vector:
    binary: List[float] = []
    for i in range(10):
        binary.append(x % 2)
        x = x // 2
    return binary

def sigmoid(t: float) -> float:
    return 1/(1+math.exp(-t))

def neuron_output(weights: Vector, inputs: Vector) -> float:
    '''weights includes the bias term, inputs includes a 1'''
    return sigmoid(dot(weights, inputs))

def feed_forward(neural_network: List[List[Vector]],
                 input_vector: Vector) -> List[Vector]:
    '''
    Feeds the inputs vector through the neural network.
    Returns the outputs of all layers (not just the last one).'''
    
    outputs: List[Vector] = []
    
    for layer in neural_network:
        input_with_bias = input_vector + [1]  # Add a constant.
        output = [neuron_output(neuron, input_with_bias)
                  for neuron in layer]
        outputs.append(output)  # add to results.
        #  then the input to the next layers is the output of this one
        
        input_vector = output
        
    return outputs


def sqerror_gradients(network: List[List[Vector]],
                      input_vector: Vector,
                      target_vector: Vector) -> List[List[Vector]]:
    """
    Given a neural network, an input vector, and a target vector,
    make a prediction and compute the gradient of the squared error
    loss with respect to the neuron weights.
    """
    # forward pass
    hidden_outputs, outputs = feed_forward(network, input_vector)

    # gradients with respect to output neuron pre-activation outputs
    output_deltas = [output * (1 - output) * (output - target)
                     for output, target in zip(outputs, target_vector)]

    # gradients with respect to output neuron weights
    output_grads = [[output_deltas[i] * hidden_output
                     for hidden_output in hidden_outputs + [1]]
                    for i, output_neuron in enumerate(network[-1])]

    # gradients with respect to hidden neuron pre-activation outputs
    hidden_deltas = [hidden_output * (1 - hidden_output) *
                         dot(output_deltas, [n[i] for n in network[-1]])
                     for i, hidden_output in enumerate(hidden_outputs)]

    # gradients with respect to hidden neuron weights
    hidden_grads = [[hidden_deltas[i] * input for input in input_vector + [1]]
                    for i, hidden_neuron in enumerate(network[0])]

    return [hidden_grads, output_grads]