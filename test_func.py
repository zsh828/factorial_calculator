from func import factorial
import pytest


class TestFactorial:
    """测试阶乘函数的单元测试类"""
    
    def test_factorial_zero(self):
        """测试 0 的阶乘应为 1"""
        assert factorial(0) == 1
    
    def test_factorial_one(self):
        """测试 1 的阶乘应为 1"""
        assert factorial(1) == 1
    
    def test_factorial_small_positive(self):
        """测试小正整数的阶乘"""
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
    
    def test_factorial_larger_number(self):
        """测试较大数字的阶乘"""
        assert factorial(10) == 3628800
        assert factorial(12) == 479001600
    
    def test_factorial_negative_raises_error(self):
        """测试负数应抛出 ValueError"""
        with pytest.raises(ValueError, match="not defined for negative numbers"):
            factorial(-1)
        
        with pytest.raises(ValueError, match="not defined for negative numbers"):
            factorial(-5)
    
    def test_factorial_non_integer_raises_error(self):
        """测试非整数输入应抛出 TypeError"""
        with pytest.raises(TypeError, match="Expected integer"):
            factorial(3.5)
        
        with pytest.raises(TypeError, match="Expected integer"):
            factorial("5")
        
        with pytest.raises(TypeError, match="Expected integer"):
            factorial(None)
        
        with pytest.raises(TypeError, match="Expected integer"):
            factorial([1, 2])
    
    def test_factorial_type_check_strict(self):
        """严格测试布尔值（bool 是 int 的子类）的行为"""
        # Python 中 bool 是 int 的子类，True=1, False=0
        # 根据实现，这应该正常工作
        assert factorial(True) == 1  # True == 1
        assert factorial(False) == 1  # False == 0