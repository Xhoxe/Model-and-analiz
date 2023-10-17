def pow_recursive(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        return 1 / pow_recursive(x, -n)
    half = pow_recursive(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half

print(pow_recursive(2.00000, 10))
