import random
from typing import List, Tuple, TypedDict
import numpy as np

class DatasetRow(TypedDict):
    """Represents a single row in the generated dataset."""
    x: List[float]
    y: float

def generate_dataset(
    weights: List[float],
    n_samples: int = 100,
    bias: float = 0.0,
    noise_fraction: float = 0.0,
    noise_level: float = 0.0,
    x_range: Tuple[float, float] = (-10, 10)
) -> List[DatasetRow]:
    """
    Generates a synthetic linear dataset with optional noise.

    Args:
        weights: Coefficients for each feature.
        n_samples: Number of samples to generate.
        bias: Bias term added to each output.
        noise_fraction: Fraction of samples with noise.
        noise_level: Standard deviation of noise.
        x_range: Range for feature values.

    Returns:
        List of DatasetRow dictionaries.
    """
    n_features = len(weights)
    dataset = []

    for _ in range(n_samples):
        x = [random.uniform(*x_range) for _ in range(n_features)]
        y = sum(w * xi for w, xi in zip(weights, x)) + bias

        # Apply noise to a fraction of rows
        if noise_fraction > 0 and random.random() < noise_fraction:
            y += np.random.normal(0, noise_level)

        dataset.append({"x": x, "y": y})

    return dataset