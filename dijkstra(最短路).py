# Author: Tingyi
# CreatTime 2023/9/23
# FileName: dijkstra
# Description: simple praticises of Python
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import copy
import re
import math

Nodes = ['v1','v2','v3','v4','v5','v6']

Arcs = {('v1','v2'):1,('v1','v3'):2,('v2','v3'):3,('v2','v4'):3,('v2','v6'):7,('v3','v4'):2,('v3','v5'):2,('v4','v6'):3,('v5','v6'):6}
#创建有向图（directed graph）
Graph = nx.DiGraph()
cnt = 0
pos_location = {}

for name in Nodes:
    cnt += 1
    X_coor = np.random.randint(1,10)
    Y_coor = np.random.randint(1,10)
    Graph.add_node(name,ID = cnt,node_type = 'normal',demand = 0,x_coor = X_coor,y_coor = Y_coor,min_dis = 0,previous_node = None)
    pos_location[name] = (X_coor,Y_coor)

for key in Arcs.keys():
    Graph.add_edge(key[0],key[1],length = Arcs[key],travelTime = 0)
#show graph（画出图）
pos = nx.spring_layout(Graph)
labels = {x[:2]: Graph.get_edge_data(*x)['length']  for x in Graph.edges}
nx.draw(Graph,pos,with_labels=True)
nx.draw_networkx_edge_labels(Graph, pos, labels)
plt.show()
#定义函数(definition dijkstra)
def dijkstra(Graph,org,des):
    bigM = float('inf')
    queue = []
    #标号（mark）
    for node in Graph.nodes:
        queue.append(node)
        if node == org:
            Graph.nodes[node]['min_dis'] = 0
        else:
            Graph.nodes[node]['min_dis'] = bigM
    # 更新每个点的最低距离(update min_dis of every nodes)
    while len(queue) > 0:
        current_node = None
        min_dis = bigM
        for node in queue:
            if Graph.nodes[node]['min_dis'] < min_dis:
                current_node = node
                min_dis = Graph.nodes[node]['min_dis']
        if current_node != None:
            queue.remove(current_node)
        for child in Graph.successors(current_node):
            arc_key = (current_node,child)
            dis_temp = Graph.nodes[current_node]['min_dis'] + Graph.edges[arc_key]['length']
            if dis_temp < Graph.nodes[child]['min_dis']:
                Graph.nodes[child]['min_dis'] = dis_temp
                Graph.nodes[child]['previous_node'] = current_node#记录当前点的上个点(record previous node)

    opt_dis = Graph.nodes[des]['min_dis']
    current_node = des
    opt_path = [current_node]
    #从终点依次遍历回起点(find node from end to start)
    while current_node != org:
        current_node = Graph.nodes[current_node]['previous_node']
        opt_path.insert(0,current_node)

    return Graph,opt_dis,opt_path

Graph,opt_dis,opt_path = dijkstra(Graph,'v1','v6')#传入图和起点、终点(input graph,start node and end node)
print('optimal distance:',opt_dis)
print('optimal path:',opt_path)
