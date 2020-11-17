
from typing import List, Tuple, Callable

Vector = List[float]

height_weight_age = [70, 170, 40]
grades = [90, 80, 75, 62]

def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), 'vectors must be the same lenght'
    return [
        v_i + w_i for v_i, w_i in zip(v, w)   
           ]

assert add([1,2,3], [4,5,6]) == [5,7,9], 'not expected data'

'''subtracting vectors'''
def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), 'vectors must be the same lenght'
    return [
        v_i - w_i for v_i, w_i in zip(v, w)   
           ]

assert subtract([5,7,9], [4,5,6]) == [1,2,3], 'not expected data'

'''sum of all corresponding elements'''
def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, 'no vectors provided'
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), 'different sizes'
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

assert vector_sum([[1,2], [3,4], [5,6], [7,8]]) == [16,20]

"""# Scalar Multiply"""

def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]

assert scalar_multiply(2.0,[1,2,3]) == [2,4,6], 'didnot match the expected data'

def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1,2], [3,4], [5,6]]) == [3,4]

"""# Dot Product"""

def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), 'len of vectors dont match'
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

assert dot([1,2,3], [4,5,6]) == 32

def sum_of_squares(v: Vector) -> float:
    return dot(v,v)

assert sum_of_squares([1,2,3]) == 14


import math

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))

assert magnitude([3,4]) == 5

def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v,w))

def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(squared_distance(v,w))


def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v,w))


Matrix = List[List[float]]

def shape(A) -> Tuple[int,int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1,2,3], [4,5,6]]) == (2,3), 'error on functions'

def get_row(A: Matrix, i: int) -> Vector:
    return A[i]


def get_column(A, j: int) -> Vector:
    return [A_i[j] for A_i in A]


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

