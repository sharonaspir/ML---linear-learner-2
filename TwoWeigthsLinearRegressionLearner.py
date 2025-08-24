import random

def guess_weights(training_data, learning_rate, epochs):
    w0 = random.uniform(-1, 1)  
    w1 = random.uniform(-1, 1)  

    for i in range(epochs):
        for point in training_data:
            x = point['x']
            y_actual = point['y']
 
            y_predicted = w1 * x + w0

            error = y_actual - y_predicted
 
            w1_update = error * x * learning_rate
            w0_update = error * learning_rate

            w1 += w1_update
            w0 += w0_update

        if (i + 1) % 200 == 0:
            print(f"Epoch {i+1}/{epochs} -> Learned function: y = {w1:.2f}x + {w0:.2f}")
    
    return w0, w1

def target_function(x, w0, w1):
    return w0 + w1 * x 

def print_results(w0, w1, set_w0, set_w1, learning_rate, epochs):
    
    test_x = [random.randint(-150, 150) for _ in range(5)]

    print("\n" * 4) 
    print(f"Initial random guess: y = {w1:.2f}x + {w0:.2f}")
    print("-" * 40)
    print("Training complete! with parameters: learning_rate =", learning_rate, "epochs =", epochs)
    print(f"Original Function: y = {set_w1}x + {set_w0}")
    print(f"Learned Function:  y = {w1:.2f}x + {w0:.2f}")
    print("-" * 40)

    print("Testing the model with a new, unseen value (x=100):")
    actual_y = [target_function(x, set_w0, set_w1) for x in test_x]
    predicted_y = [w1 * x + w0 for x in test_x]
    error = [actual - predicted for actual, predicted in zip(actual_y, predicted_y)]
    avg_error = sum(abs(e) for e in error) / len(error)

    print(f"Actual result: {actual_y}")
    print(f"Model's prediction: {predicted_y}")
    print(f"Error: {[f'{e:.2f}' for e in error]}")
    print(f"Average error: {avg_error:.2f}")
    

set_w0 = 5
set_w1 = 2000

training_data = []
for x in range(-50, 51):  # Generate 101 data points from x=-50 to x=50
    y = target_function(x, set_w0, set_w1) 
    training_data.append({'x': x, 'y': y})

learning_rate = 0.001
epochs = 10
res = guess_weights(training_data, learning_rate, epochs)
w0, w1 = res

print_results(w0, w1, set_w0, set_w1, learning_rate, epochs)
