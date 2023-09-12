# Author: Tingyi
# CreatTime 2023/9/11
# FileName: Linear Programming(线性规划)
# Description: simple praticises
#Maximize
# 3 * (x1) + 2 * (x2) + 2.9 * (x3)
# Subject To
#c0: 8 * x1 + 2 * x2 + 10 * x3 <= 300
#c1:10 * x1 + 5 * x2 + 8 * x3 <= 400
#c2:2 * x1 + 13 * x2 + 10 * x3 <= 420
#c3: x1,x2,x3 >= 0
#Bounds End(参考清华大学版运筹学课后习题)
from gurobipy import *
#发生错误时如无可行解或无界解等，执行下面的except语句(if error,execute 'except' sentences)
try:
# 创建新模型(create a new model)
    m = Model('LinearProblem')
#新建变量(create variables)
    x1 = m.addVar(lb=0,ub=float('inf'),vtype=GRB.CONTINUOUS,name='x1')#x1为连续型，下界为0 上届为无穷大
    x2 = m.addVar(lb=0,ub=float('inf'),vtype=GRB.CONTINUOUS,name='x2')#x2 is continuous, the minimum is 0,the maximum is infinity
    x3 = m.addVar(lb=0,ub=float('inf'),vtype=GRB.CONTINUOUS,name='x3')
#目标函数(set objective)
    m.setObjective(3 * x1 + 2 * x2 + 2.9 * x3,GRB.MAXIMIZE)
#约束c0 c1 c2(add constraint)
    m.addConstr(8 * x1 + 2 * x2 + 10 * x3 <= 300,'c0')
    m.addConstr(10 * x1 + 5 * x2 + 8 * x3 <= 400,'c1')
    m.addConstr(2 * x1 + 13 * x2 + 10 * x3 <= 420,'c2')
#优化迭代
    m.optimize()
#打印每个变量的最优值(print variables)
    print('Optimal solution',end='  ')
    for i in m.getVars():
        print('%s = %g' % (i.varName,i.x),end=' ')
#错误归因(error attribution)
except GurobiError as g:
    print('Error code' + str(g.errno) + ':' + str(g))
except AttributeError:
    print('Encountered an attribute error')
#Answer: x1 = 338/15  x2 = 116/5  x3 = 22/3 obj = 2029/15
