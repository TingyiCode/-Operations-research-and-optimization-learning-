# Author: Tingyi
# CreatTime 2023/9/12
# FileName: Integer Programming(整数规划)
# Description: simple praticises of Gurobi
#Maximize
#3 * x1 + 2 * x2
#Subject to
#c0:2 * x1 + 3 * x2 <= 14.5
#c1:4 * x1 + x2 <= 16.5
#c2:x1,x2 >= 0
#c3:x1,x2 is integer
#Bounds End(例子参考清华大学版运筹学课后习题)
import gurobipy as grb
#发生错误时如无可行解或无界解等，执行下面的except语句(if error,execute 'except' sentences)
try:
# 创建新模型(create a new model)
    m = grb.Model('LinearProblem')
#新建变量(create variables)
    x1 = m.addVar(lb=0,ub=float('inf'),vtype=grb.GRB.INTEGER,name='x1')#x1为整数型，下界为0 上届为无穷大
    x2 = m.addVar(lb=0,ub=float('inf'),vtype=grb.GRB.INTEGER,name='x2')#x2 is integer, the minimum is 0,the maximum is infinity
#目标函数(set objective)
    m.setObjective(3 * x1 + 2 * x2,sense=grb.GRB.MAXIMIZE)
#约束c0 c1 (add constraint)
    m.addConstr(2 * x1 + 3 * x2 <= 14.5,'c0')
    m.addConstr(4 * x1 + x2 <= 16.5,'c1')
#优化迭代(optimize)
    m.optimize()
#打印每个变量的最优值(print optimal variables)
    print('Optimal Solution',end='  ')
    for i in m.getVars():
        print('%s = %g' % (i.VarName,i.x),end=' ')
#错误归因(error attribution)
except grb.GurobiError as g:
    print('Error code' + str(g.errno) + ':' + str(g))
except AttributeError:
    print('Encountered an attribute error')

#Answer:x1 = 3 x2 = 2 obj = 13
