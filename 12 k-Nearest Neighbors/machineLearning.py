import random
from typing import TypeVar, List, Tuple

X = TypeVar("X")  # generic type to represent a data point.


def split_data(data: List[X], percentage: float) -> Tuple[List[X], List[X]]:
    '''split data into fractions [prob, 1-prob]'''
    random.seed(0)
    data = data[:]
    random.shuffle(data)
    cut = int(len(data) * percentage)
    return data[:cut], data[cut:]


Y = TypeVar('Y')  # generic type to represent output variables


def train_test_split(xs: List[X],
                     ys: List[Y],
                     test_pct: float) -> Tuple[List[X], List[X],
                                               List[Y], List[Y]]:
    idxs = [i for i in range(len(xs))]
    train_idxs, test_idxs = split_data(idxs, 1 - test_pct)
    return ([xs[i] for i in train_idxs],
            [xs[i] for i in test_idxs],
            [ys[i] for i in train_idxs],
            [ys[i] for i in test_idxs])


def accuracy(tp: int, fp: int, fn: int, tn: int) -> float:
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct/total


def precision(tp: int, fp: int) -> float:
    return tp / (tp+fp)


assert precision(70, 4930, 13930, 981070) == 0.014


def recall(tp: int, fn: int) -> float:
    return tp / (tp+fn)


assert recall(70, 4930, 13930, 981070) == 0.005


def f1_score(tp: int, fp: int, fn: int, tn: int) -> float:
    precisionValue = precision(tp, fp, fn, tn)
    recallValue = recall(tp, fp, fn, tn)
    return 2*precisionValue*recallValue/(precisionValue+recallValue)
#  assert f1_score(70, 4930, 1390, 981070) == 0.021671826625386997


def f_beta(tp: int, fp: int, tn: int, fn: int, beta: float) -> float:
    precisionValue = precision(tp, fp, fn, tn)
    recallValue = recall(tp, fp, fn, tn)
    return beta*precisionValue*recallValue/(precisionValue+recallValue)
