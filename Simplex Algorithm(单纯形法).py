# Author: Tingyi
# CreatTime 2023/9/20
# FileName: Simplex Algorithm(单纯形法)
# Description: simple praticises of Python
#Maximize
# 3 * (x1) + 2 * (x2) + 2.9 * (x3)
# Subject To
#c0: 8 * x1 + 2 * x2 + 10 * x3 <= 300
#c1:10 * x1 + 5 * x2 + 8 * x3 <= 400
#c2:2 * x1 + 13 * x2 + 10 * x3 <= 420
#c3: x1,x2,x3 >= 0
#Bounds End(参考清华大学版运筹学课后习题)
#standard form(化为标准型)
#c0: 8 * x1 + 2 * x2 + 10 * x3 + x4 == 300
#c1:10 * x1 + 5 * x2 + 8 * x3 + x5 == 400
#c2:2 * x1 + 13 * x2 + 10 * x3 + x6 == 420
#c3: x1,x2,x3,x4,x5,x6 >= 0
import numpy as np
import pandas as pd
import copy

Basic = [3,4,5]
Nonbasic = [0,1,2]
c = np.array([3,2,2.9,0,0,0]).astype(float)
c_B = np.array([0,0,0]).astype(float)
c_N = np.array([3,2,2.9]).astype(float)
A = np.array([[8,2,10,1,0,0],[10,5,8,0,1,0],[2,13,10,0,0,1]]).astype(float)
A_N = np.array([[8,2,10],[10,5,8],[2,13,10]]).astype(float)
b = np.array([300,400,420]).astype(float)
B_inv = np.array([[1,0,0],[0,1,0],[0,0,1]]).astype(float)
x_opt = np.array([0,0,0,0,0,0]).astype(float)
z_opt = 0

solutionStatus = None

row_num = len(A)
col_num = len(A[0])

reducedCost = c_N - np.dot(np.dot(c_B,B_inv),A_N)

max_sigma = max(reducedCost)
eps = 0.001

iterNum = 1

while (max_sigma >= eps):
    enter_var_index = Nonbasic[np.argmax(reducedCost)]
    print('enter_var_index:',enter_var_index)
# 选择出基变量(Determine the leaving basic variable)
    min_ratio = float('inf')
    leave_var_index = 0
    for i in range(row_num):
        print('b:',b[i],'\t A:',A[i][enter_var_index],'\t ratio:',b[i] / A[i][enter_var_index])
        if A[i][enter_var_index] == 0:
            continue
        elif b[i] / A[i][enter_var_index] < min_ratio and b[i] / A[i][enter_var_index] > 0:
            min_ratio = b[i] / A[i][enter_var_index]
            leave_var_index = i
# 交换基变量和非基变量(exchange entering basic and leaving basic)
    leave_var = Basic[leave_var_index]
    Basic[leave_var_index] = enter_var_index
    Nonbasic.remove(enter_var_index)
    Nonbasic.append(leave_var)
    Nonbasic.sort()
#高斯消元(Gaussian elimination)
#更新主要行(update pivot row)
    pivot_number = A[leave_var_index][enter_var_index]
    print('pivot_number :',pivot_number)
    for col in range(col_num):
        A[leave_var_index][col] = A[leave_var_index][col] / pivot_number
    b[leave_var_index] = b[leave_var_index] / pivot_number
#更新其他行(update other rows)
    for row in range(row_num):
        if row != leave_var_index:
            factor = -A[row][enter_var_index] / 1.0
            for col in range(col_num):
                A[row][col] = A[row][col] + factor * A[leave_var_index][col]
            b[row] = b[row] + factor * b[leave_var_index]
# 更新 update c_N,c_B,A_N and B_inv
    for i in range(len(Nonbasic)):
        var_index = Nonbasic[i]
        c_N[i] = c[var_index]
    for i in range(len(Basic)):
        var_index = Basic[i]
        c_B[i] = c[var_index]
    for i in range(row_num):
        for j in range(len(Nonbasic)):
            var_index = Nonbasic[j]
            A_N[i][j] = A[i][var_index]
    for i in range(len(Basic)):
        col = Basic[i]
        for row in range(row_num):
            B_inv[row][i] = A[row][col]
# 更新检验数(update reduced cost)
    reducedCost = c_N - np.dot(np.dot(c_B,B_inv),A_N)
    max_sigma = max(reducedCost)
    iterNum += 1
# 检查问题状态(check the solution status)
for i in range(len(reducedCost)):
    if reducedCost[i] == 0:
        solution_status = 'Alternative optimal solution'
        break
    else:
        solution_status = 'Optimal'
# 取得答案(get the solution)
x_basic = np.dot(B_inv,b)
x_opt = np.array([0.0] * col_num).astype(float)
for i in range(len(Basic)):
    basic_var_index = Basic[i]
    x_opt[basic_var_index] = x_basic[i]
z_opt = np.dot(np.dot(c_B,B_inv),b)

print('Simplex iteration:',iterNum)
print('objective:',z_opt)
print('optimal solution:',x_opt)