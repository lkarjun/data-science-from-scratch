from typing import Tuple, List
from linearalgebra import vector_mean,Vector
from stati import standard_deviation

def scale(data: List[Vector]) -> Tuple[Vector, Vector]:
    '''returns the mean and standard deviation for each position'''
    dim = len(data[0])
    means = vector_mean(data)
    stdevs = [standard_deviation([vector[i] for vector in data]) for i in range(dim)]
    return means, stdevs

def rescale(data: List[Vector]) -> List[Vector]:
    '''rescales the input data so that each positions has mean 0 and standard deviation 1.(leaves a position as is if its std is 0)'''
    dim = len(data[0])
    means, stdevs = scale(data)
    rescaled = [v[:] for v in data]#making a copy of each vector
    for v in rescaled:
        # print('v is ', v)
        for i in range(dim):
            # print('printing i', i)
            if stdevs[i] > 0:
                # print('stdv is greater than 0 so.')
                v[i] = (v[i] - means[i]) / stdevs[i]
                # print(f'printing {v[i]}')
    return rescaled
        