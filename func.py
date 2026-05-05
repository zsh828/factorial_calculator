def factorial(n: int) -> int:
    """
    计算一个非负整数的阶乘。
    
    Args:
        n (int): 非负整数
        
    Returns:
        int: n 的阶乘
        
    Raises:
        ValueError: 如果 n 是负数
        TypeError: 如果 n 不是整数
    """
    # 类型检查
    if not isinstance(n, int):
        raise TypeError(f"Expected integer, got {type(n).__name__}")
    
    # 边界条件检查
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # 基础情况
    if n == 0 or n == 1:
        return 1
    
    # 递归计算阶乘
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result