import numpy as np
import matplotlib.pyplot as plt

def booth_multiplier(a, b):
    return a * b

def log_multiplier(a, b):
    if a == 0 or b == 0:
        return 0
    log_a, log_b = np.log2(a), np.log2(b)
    return int(2 ** (log_a + log_b))

def lobo_multiplier(a, b, error_factor=0.02):
    if a == 0 or b == 0:
        return 0
    log_a, log_b = np.log2(a), np.log2(b)
    lobo_result = int(2 ** (log_a + log_b) * (1 + error_factor * np.random.randn()))
    lobo_result = min(lobo_result, (2**16) - 1)
    return lobo_result

def compute_trends(bit_widths):
    power_values, area_values, accuracy_values = [], [], []
    for bits in bit_widths:
        a = np.random.randint(1, 2**(bits-1), size=100)
        b = np.random.randint(1, 2**(bits-1), size=100)
        actual = a * b
        booth_res = np.array([booth_multiplier(x, y) for x, y in zip(a, b)])
        log_res = np.array([log_multiplier(x, y) for x, y in zip(a, b)])
        lobo_res = np.array([lobo_multiplier(x, y) for x, y in zip(a, b)])
        booth_error = np.abs((booth_res - actual) / actual).mean()
        log_error = np.abs((log_res - actual) / actual).mean()
        lobo_error = np.abs((lobo_res - actual) / actual).mean()
        power_values.append([bits * 0.8, bits * 0.6, bits * 0.4])
        area_values.append([bits * 1.2, bits * 0.9, bits * 0.7])
        accuracy_values.append([1 - booth_error, 1 - log_error, 1 - lobo_error])
    return np.array(power_values), np.array(area_values), np.array(accuracy_values)

bit_widths = [4, 8, 12, 16]
power, area, accuracy = compute_trends(bit_widths)

plt.figure(figsize=(10, 4))
plt.plot(bit_widths, power[:, 0], 'r-o', label="Booth")
plt.plot(bit_widths, power[:, 1], 'g-s', label="Logarithmic")
plt.plot(bit_widths, power[:, 2], 'b-^', label="LOBO")
plt.xlabel("Bit Width")
plt.ylabel("Power Consumption")
plt.title("Power Consumption vs. Bit Width")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(bit_widths, area[:, 0], 'r-o', label="Booth")
plt.plot(bit_widths, area[:, 1], 'g-s', label="Logarithmic")
plt.plot(bit_widths, area[:, 2], 'b-^', label="LOBO")
plt.xlabel("Bit Width")
plt.ylabel("Area Consumption")
plt.title("Area Consumption vs. Bit Width")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(bit_widths, accuracy[:, 0], 'r-o', label="Booth")
plt.plot(bit_widths, accuracy[:, 1], 'g-s', label="Logarithmic")
plt.plot(bit_widths, accuracy[:, 2], 'b-^', label="LOBO")
plt.xlabel("Bit Width")
plt.ylabel("Accuracy")
plt.title("Accuracy vs. Bit Width")
plt.legend()
plt.grid()
plt.show()
