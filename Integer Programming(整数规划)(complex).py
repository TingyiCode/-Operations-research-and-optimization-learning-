# Author: Tingyi
# CreatTime 2023/9/13
# FileName: Integer Programming(整数规划)1
# Description: simple praticises of Python
#Minimize
#5(x1_1) + 4(x1_2) + 3(x1_3) + 2(x1_4) + (x1_5) + ...... + 5(x10_1) + 4(x10_2) + 3(x10_3) + 2(x10_4) + (x10_5)
#Subject to
#c0:10(xi_1) + 7(xi_2) + 5(xi_3) + 4(xi_4) + (xi_5) = Di
#c1:(xi_1) + (xi_2) + (xi_3) + (xi_4) + (xi_5) <= Di
#c2:(xi_1) + 2(xi_2) + 3(xi_3) + (xi_4) + (xi_5) <= INCi
#c3:(xi_1),(xi_2),(xi_3),(xi_4),(xi_5) >= 0 and integer i = {1,2,3...,10}
#Bounds End(例子参考运筹优化常用模型算法)
from gurobipy import *
import pandas as pd
import numpy as np
D = [60,60,60,72,72,82,60,80,80,90]
INC = [10,20,30,60,80,50,60,70,90,80]
obj_coef = [5,4,3,2,1]
coef = [[10,7,5,4,1],[1,1,1,1,1],[1,2,3,6,10]]
model = Model('IP')
x = [[[] for i in range(5)]for j in range(len(D))]
for i in range(len(D)):
    for j in range(5):
        x[i][j] = model.addVar(lb=0.0,ub=100000,vtype=GRB.INTEGER,name='x_'+str(i)+'_'+str(j))
# 目标函数(objective function)
obj = LinExpr(0)
for i in range(len(D)):
    for j in range(5):
        obj.addTerms(obj_coef[j],x[i][j])
model.setObjective(obj,GRB.MINIMIZE)
# 约束1(constraint c0)
for i in range(len(D)):
    expr = LinExpr(0)
    for j in range(5):
        expr.addTerms(coef[0][j],x[i][j])
    model.addConstr(expr == D[i],name='D_'+str(i))
# 约束2(constraint c1)
for i in range(len(D)):
    expr = LinExpr(0)
    for j in range(5):
        expr.addTerms(coef[1][j],x[i][j])
    model.addConstr(expr <= D[i],name='D_2'+str(i))
# 约束3(constraint c2)
for i in range(len(D)):
    expr = LinExpr(0)
    for j in range(5):
        expr.addTerms(coef[2][j],x[i][j])
    model.addConstr(expr <= INC[i],name='INC_'+str(i))
# 求解
model.optimize()
# 打印大于0的数
for var in model.getVars():
    if var.x > 0:
        print(var.varName,'\t',var.x)