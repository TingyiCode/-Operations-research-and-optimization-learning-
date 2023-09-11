# Author: Tingyi
# CreatTime 2023/9/11
# FileName: Interger Programming(整数规划)
# Description: simple praticises
#Minimize
# 2 * (x1) + 5 * (x2) + 3 * (x3) + 4 * (x4)
# Subject To
#c0: -4 * x1 + x2 + x3 + x4 >= 0
#c1:-2 * x1 + 4 * x2 + 2 * x3 + 4 * x4 >= 4
#c2:x1 + x2 - x3 + x4 >= 1
#c3: x1,x2,x3 == {0,1}
#Bounds End(参考清华大学版运筹学课后习题)
from gurobipy import *
#发生错误时如无可行解或无界解等，执行下面的except语句(if error,execute 'except' sentences)
try:
# 创建新模型(create a new model)
    m = Model('LinearProblem')
#新建变量(create variables)
    x1 = m.addVar(vtype=GRB.BINARY,name='x1')#x1取值为0或1
    x2 = m.addVar(vtype=GRB.BINARY,name='x2')#x2 is bianry
    x3 = m.addVar(vtype=GRB.BINARY,name='x3')
    x4 = m.addVar(vtype=GRB.BINARY,name='x4')
#目标函数(set objective)
    m.setObjective(2 * x1 + 5 * x2 + 3 * x3 + 4 * x4,GRB.MINIMIZE)
#约束c0 c1 c2(add constraint)
    m.addConstr(-4 * x1 + x2 + x3 + x4 >= 0,'c0')
    m.addConstr(2 * x1 + 4 * x2 + 2 * x3 + 4 * x4 >= 4,'c1')
    m.addConstr(x1 + x2 - x3 + x4 >= 1,'c2')
#优化迭代
    m.optimize()
#打印每个变量的最优值(print variables)
    print('Optimal solution',end='  ')
    for i in m.getVars():
        print('%s = %g' % (i.varName,i.x),end=' ')
#错误归因(error attribution)
except GurobiError as g:
    print('Error code' + str(g.grrno) + ':' + str(g))
except AttributeError:
    print('Encountered an attribute error')
#Answer:x1 = x2 = x3 = 0 x4 = 1 obj = 4