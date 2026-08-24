import numpy as np

def log_multiplier(a, b):
    if a == 0 or b == 0:
        return 0
    log_a = np.log2(a)
    log_b = np.log2(b)
    log_result = log_a + log_b
    return int(2 ** log_result)

def log_multiplier_truncated(a, b, truncate_bits=3):
    if a == 0 or b == 0:
        return 0
    log_a = np.log2(a)
    log_b = np.log2(b)
    log_result = log_a + log_b
    return int(2 ** (log_result - truncate_bits))

A = 50
B = 25
actual_product = A * B
log_result = log_multiplier(A, B)
log_trunc_result = log_multiplier_truncated(A, B)
error_log = abs(actual_product - log_result)
error_trunc = abs(actual_product - log_trunc_result)
error_log_percent = (error_log / actual_product) * 100
error_trunc_percent = (error_trunc / actual_product) * 100

print(f"A = {A}, B = {B}")
print(f"Actual Product = {actual_product}")
print(f"Logarithmic Multiplier Result (No Truncation) = {log_result}, Error = {error_log} ({error_log_percent:.2f}%)")
print(f"Logarithmic Multiplier Result (With Truncation) = {log_trunc_result}, Error = {error_trunc} ({error_trunc_percent:.2f}%)")
