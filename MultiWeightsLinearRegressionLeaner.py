import random
from typing import List, Tuple, Sequence, Optional, TypedDict
from LinearTrainingDataGeneration import DatasetRow, generate_dataset

Vector = List[float]



def dot(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b))

def guess_weights(
    training_data: List[DatasetRow],
    learning_rate: float,
    epochs: int,
    seed: Optional[int] = None,
) -> Tuple[float, Vector]: 
    if not training_data:
        raise ValueError("training_data is empty.")
    if "x" not in training_data[0] or "y" not in training_data[0]:
        raise ValueError("Each training example must have 'x' and 'y' keys.")

    n_features = len(training_data[0]["x"])
    if n_features == 0:
        raise ValueError("Feature vector 'x' must have at least one feature.")

    rng = random.Random(seed)

    b = rng.uniform(-1.0, 1.0)
    w = [rng.uniform(-1.0, 1.0) for _ in range(n_features)]

    for _ in range(epochs):
        rng.shuffle(training_data)
        for point in training_data:
            x = point["x"]
            y_actual = point["y"]

            if not isinstance(x, list) or len(x) != n_features:
                raise ValueError("All 'x' must be lists of consistent length.")
            if not isinstance(y_actual, (int, float)):
                raise ValueError("'y' must be a number.")

            y_pred = dot(w, x) + b
            error = y_actual - y_pred

            for j in range(n_features):
                w[j] += learning_rate * error * x[j]
            b += learning_rate * error

    return b, w


def target_function(x_vec: Sequence[float], b: float, w: Sequence[float]) -> float:
    return b + dot(w, x_vec)


def print_results(
    b: float,
    w: Vector,
    set_b: float,
    set_w: Sequence[float],
    learning_rate: float,
    epochs: int,
    seed: Optional[int] = None,
) -> None:
    rng = random.Random(seed + 1) if seed is not None else random.Random()

    n_features = len(w)
    test_x: List[Vector] = [
        [rng.randint(-150, 150)] if n_features == 1
        else [rng.randint(-50, 50) for _ in range(n_features)]
        for _ in range(5)
    ]

    actual_y = [target_function(x, set_b, set_w) for x in test_x]
    pred_y = [target_function(x, b, w) for x in test_x]
    errors = [a - p for a, p in zip(actual_y, pred_y)]
    avg_abs = sum(abs(e) for e in errors) / len(errors)
    mse = sum(e * e for e in errors) / len(errors)

    print("\nTraining complete!")
    print(f"Params: learning_rate={learning_rate}, epochs={epochs}")
    print(f"Original:  b={set_b}, w={list(set_w)}")
    print(f"Learned :  b={b:.4f}, w={[round(v, 4) for v in w]}")
    print("-" * 40)
    print("Test X       :", test_x)
    print("Actual y     :", [round(v, 2) for v in actual_y])
    print("Predicted y  :", [round(v, 2) for v in pred_y])
    print("Error        :", [f"{e:.2f}" for e in errors])
    print(f"Average |err|: {avg_abs:.2f}")
    print(f"MSE          : {mse:.2f}")

# -------- Example run --------
if __name__ == "__main__":
    set_b = 5.0
    set_w = [2.0, 5.0, 17.0]   

    training_data = generate_dataset(set_w, 100, set_b)
    learning_rate = 0.0001
    epochs = 10000

    b, w = guess_weights(training_data, learning_rate, epochs, seed=42)
    print_results(b, w, set_b, set_w, learning_rate, epochs, seed=42)