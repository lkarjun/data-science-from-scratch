# from Linear import Vector, dot
from typing import Callable, List
import matplotlib.pyplot as plt
from linearalgebra import scalar_multiply, add
from typing import TypeVar, List, Iterator

#Estimating the Gradient

def difference_quotient(f: Callable[[float], float],
                        x: float,
                        h: float) -> float:
                        return (f(x+h) - f(x) / h)

def square(x: float) -> float:
    return x * x

def derivative(x: float) -> float:
    return 2 * x

Vector = List[float]

def partial_difference_quotient(f: Callable[[Vector], float],
                                v: Vector,
                                i: int,
                                h: float) -> float:
                  
                  w = [v_j + (h if j == i else 0)
                        for j, v_j in enumerate(v)]
                  return (f(w)- f(v))/h

def estimate_gradient(f: Callable[[Vector], float],
                      v: Vector,
                      h: float = 0.0001):
  return [partial_difference_quotient(f, v, i, h)
          for i in range(len(v))]

import random

def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
  """Moves 'step-size' in the 'gradient' direction from 'v' """
  assert len(v) == len(gradient)
  step = scalar_multiply(step_size, gradient)
  return add(v, step)

def sum_of_squares_gradient(v: Vector) -> Vector:
  return [2 * v_i for v_i in v]

def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
  slope, intercept = theta
  predicted = slope * x + intercept
  #prediction of the model
  error = (predicted - y)
  #error is (predicted - actual)o
  squared_error = error ** 2
  #we'll minimize squared error
  grad = [2 * error * x, 2 * error]
  return grad

T = TypeVar("T") # this allow us to type "generic" Function

def minibatches(dataset: List[T],
                batch_size: int,
                shuffle: bool = True) -> Iterator[List[T]]:
                '''Generates "batch_size" - sized minibatches from the dataset'''
                #start indexed 0, batch_size, 2 * batch_size
                batch_starts = [start for start in range(0, len(dataset), batch_size)]
                if shuffle: random.shuffle(batch_starts)
                #shuffle the batches
                for start in batch_starts:
                  end = start + batch_size
                  yield dataset[start: end]