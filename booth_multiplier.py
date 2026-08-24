import numpy as np

def booth_multiplier(a, b, error_factor=0.02):
    result = a * b
    noisy_result = int(result * (1 + error_factor * np.random.randn()))
    noisy_result = max(0, min(noisy_result, (2**16) - 1))
    return noisy_result

a = 23
b = 45
actual_product = a * b
booth_product = booth_multiplier(a, b)
error = abs(booth_product - actual_product) / actual_product * 100

print(f"Operand A: {a}")
print(f"Operand B: {b}")
print(f"Actual Product: {actual_product}")
print(f"Booth Multiplier Product (with error): {booth_product}")
print(f"Error Percentage: {error:.2f}%")
