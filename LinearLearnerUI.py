import tkinter as tk
from tkinter import messagebox

# --- Main Application Window ---
root = tk.Tk()
root.title("Weight & Bias Error Calculator")
root.geometry("450x250") # Set window size

# --- Core Calculation Logic ---
def calculate_and_display():
    """
    Retrieves inputs, calculates the sum and error, and updates the UI.
    """
    try:
        # 1. Get values from input fields
        bias_str = entry_bias.get()
        weights_str = entry_weights.get()
        true_value_str = entry_true_value.get()

        # 2. Convert strings to numbers
        bias = float(bias_str)
        true_value = float(true_value_str)
        
        # Split the weights string by commas and convert each to a float
        # This handles cases with spaces like "1.5, 2.3,4"
        weights = [float(w.strip()) for w in weights_str.split(',')]

        # 3. Perform calculations
        estimated_sum = bias + sum(weights)
        error = abs(true_value - estimated_sum)

        # 4. Update the result labels in the UI
        result_sum_var.set(f"Estimated Sum: {estimated_sum:.4f}")
        result_error_var.set(f"Absolute Error: {error:.4f}")

    except ValueError:
        # Show an error popup if the input is not a valid number
        messagebox.showerror("Input Error", "Please enter valid numbers.\nWeights must be comma-separated.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# --- UI Widgets ---

# Frame for better organization
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True)

# Input field for Bias (b)
tk.Label(frame, text="Bias (b):").grid(row=0, column=0, sticky="w", pady=2)
entry_bias = tk.Entry(frame, width=40)
entry_bias.grid(row=0, column=1, pady=2)

# Input field for Weights (w1, w2, ...)
tk.Label(frame, text="Weights (comma-separated):").grid(row=1, column=0, sticky="w", pady=2)
entry_weights = tk.Entry(frame, width=40)
entry_weights.grid(row=1, column=1, pady=2)

# Input field for the True Value to compare against
tk.Label(frame, text="True Value:").grid(row=2, column=0, sticky="w", pady=2)
entry_true_value = tk.Entry(frame, width=40)
entry_true_value.grid(row=2, column=1, pady=2)

# Button to trigger the calculation
calculate_button = tk.Button(frame, text="Calculate", command=calculate_and_display)
calculate_button.grid(row=3, column=1, pady=15, sticky="e")

# --- Labels to Display Results ---
result_sum_var = tk.StringVar()
result_error_var = tk.StringVar()

tk.Label(frame, textvariable=result_sum_var, font=("Helvetica", 12, "bold")).grid(row=4, column=0, columnspan=2, pady=5)
tk.Label(frame, textvariable=result_error_var, font=("Helvetica", 12, "bold")).grid(row=5, column=0, columnspan=2, pady=5)

# --- Start the UI event loop ---
root.mainloop()