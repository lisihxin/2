# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cmath

def solve_quadratic_equation(a, b, c):
    # 計算判別式
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # 計算兩個解
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)

    return root1, root2

# 輸入係數
a = float(input("請輸入a的值："))
b = float(input("請輸入b的值："))
c = float(input("請輸入c的值："))

# 解方程式
roots = solve_quadratic_equation(a, b, c)

# 輸出解
print(f"方程式的解為：{roots}")
