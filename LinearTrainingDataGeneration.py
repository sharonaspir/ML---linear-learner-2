import random
from typing import Sequence 


def dot(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b))

def generate_training_data_independent(bias, weights, numberOfDataRows=500, lowerBound=-50, higherBound=50, seed=0):
    rng = random.Random(seed)
    N = len(weights)
    data = []
    for _ in range(numberOfDataRows):
        x = [rng.uniform(lowerBound, higherBound) for _ in range(N)]
        y = bias + dot(weights, x)
        data.append({'x': x, 'y': y})
    return data