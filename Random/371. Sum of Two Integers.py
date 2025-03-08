def getSum(a: int, b: int) -> int:
    mask = 0xFFFFFFFF  # 32-bit mask
    while b & mask:
        carry = a & b
        a = (a ^ b) & mask
        b = (carry << 1) & mask

    return a if a <= 0x7FFFFFFF else ~(a ^ mask)  # Handling negatives
