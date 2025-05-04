def gcd(a, b):
    """
    使用大数减小数算法计算两个数的最大公约数
    
    参数:
        a: 第一个正整数
        b: 第二个正整数
    返回:
        a和b的最大公约数
    """
    # 确保a和b都是正整数
    if a <= 0 or b <= 0:
        raise ValueError("输入必须是正整数")
    
    # 当a和b相等时，最大公约数就是a（或b）
    while a != b:
        if a > b:
            a = a - b  # 大数减小数
        else:
            b = b - a  # 大数减小数
    
    return a  # 返回最大公约数

# 测试函数
def test_gcd():
    test_cases = [
        (12, 8, 4),    # gcd(12, 8) = 4
        (54, 24, 6),   # gcd(54, 24) = 6
        (48, 18, 6),   # gcd(48, 18) = 6
        (7, 5, 1),     # gcd(7, 5) = 1
        (100, 10, 10)  # gcd(100, 10) = 10
    ]
    
    for a, b, expected in test_cases:
        result = gcd(a, b)
        print(f"gcd({a}, {b}) = {result}, 期望值: {expected}, {'✓' if result == expected else '✗'}")

# 主程序
if __name__ == "__main__":
    print("最大公约数计算器（使用大数减小数算法）")
    print("-" * 40)
    
    # 运行测试用例
    print("运行测试用例:")
    test_gcd()
    print("-" * 40)
    
    # 用户输入
    try:
        num1 = int(input("请输入第一个正整数: "))
        num2 = int(input("请输入第二个正整数: "))
        result = gcd(num1, num2)
        print(f"\n{num1}和{num2}的最大公约数是: {result}")
    except ValueError as e:
        print(f"错误: {e}")