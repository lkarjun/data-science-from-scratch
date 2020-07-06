from typing import List, Tuple
import math

#Adding vectors

vector = List[float]

def add(v: vector, w: vector) -> vector:
    assert len(v) == len(w), 'Vectors must have same length'
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1,2,2],[2,3,3]) == [3, 5, 5], 'there is a mistake kindly please check the function'



#Subtracting vectors
def sub(v: vector, w: vector) -> vector:
    assert len(v) == len(w), 'vectors must have same len'
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert sub([1,2,1],[2,1,2]) == [-1, 1, -1], 'check the function there is a mistake'

#sum of all corresponding vectors

'''sum of all corresponding elements'''
def vector_sum(vectors: List[vector]) -> vector:
    assert vectors, 'no vectors provided'
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), 'different sizes'
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

assert vector_sum([[1,2], [3,4], [5,6], [7,8]]) == [16,20]


#scalar_multiply

def scalar_multiply(c: float, v: vector) -> vector:
    return [c * v_i for v_i in v]

assert scalar_multiply(2.0,[1,2,3]) == [2,4,6], 'please check the function'

def vector_mean(vectors: List[vector]) -> vector:
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1,2], [3,4], [5,6]]) == [3,4]


#dot prodcut

def dot(v: vector, w: vector) -> float:
    assert len(v) == len(w), 'len of vectors didnt match'
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

assert dot([1,2,3], [4,5,6]) == 32, 'please check the function'

#sum of squares 
def sum_of_squares(v: vector) -> float:
    return dot(v,v)


def magnitude(v: vector) -> float:
    return math.sqrt(sum_of_squares(v))

def squared_distance(v: vector, w: vector) -> float:
    return sum_of_squares(sub(v,w))

def distance(v: vector, w: vector) -> float:
    return math.sqrt(squared_distance(v,w))

def distance(v: vector, w: vector) -> float:
    return magnitude(sub(v,w))

#matrices

Matrix = List[List[float]]

def shape(A) -> Tuple[int,int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1,2,3], [4,5,6]]) == (2,3), 'error on functions'


def get_column(A, j: int) -> Vector:
    return [A_i[j] for A_i in A]

get_column([[1,2,3],[12,4]], 0)


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

    