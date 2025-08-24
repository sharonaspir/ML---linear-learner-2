import random
import numpy as np
from typing import List, Tuple, TypedDict

class DatasetRow(TypedDict):
    x: List[float]
    y: float
    
def generate_dataset(
    weights: List[float], 
    n_samples: int = 100, 
    bias: float = 0.0, 
    noise_fraction: float = 0.0,   # fraction of rows with noise (0.0 - 1.0)
    noise_level: float = 0.0,      # std deviation of noise
    x_range: Tuple[float, float] = (-10, 10)
) -> List[DatasetRow]:
    n_features = len(weights)
    dataset = []

    for _ in range(n_samples):
        x = [random.uniform(*x_range) for _ in range(n_features)]
        y = sum(w * xi for w, xi in zip(weights, x)) + bias
        
        # Apply noise only to some rows
        if noise_fraction > 0 and random.random() < noise_fraction:
            y += np.random.normal(0, noise_level)
        
        dataset.append({"x": x, "y": y})

    return dataset