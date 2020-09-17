from typing import NamedTuple, List
from collections import Counter
from linearalgebra import Vector, distance

def majority_vote(labels: List[str]) -> str:
    '''Assumes that labels are ordered from nearest to farthest'''
    vote_counts = Counter(labels)
    winner, winners_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                      for count in vote_counts.values()
                      if count == winners_count])
    if num_winners == 1:
        return winner #unique winner, so return it
    else:
        return majority_vote(labels[:-1]) #tyr again without the farthest

class LabeledPoint(NamedTuple):
    point: Vector
    label: str
def knn_classify(k: int, labeled_points: List[LabeledPoint], new_point: Vector) -> str:
    #order the labeled points from nearest to farthest.
    by_distance = sorted(labeled_points, key=lambda lp: distance(lp.point, new_point))
    #find the labels for the k closest
    k_nearest_labels = [lp.label for lp in by_distance[:k]]
    return majority_vote(k_nearest_labels)

