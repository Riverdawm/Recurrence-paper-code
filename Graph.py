# _*_ coding : utf-8
# @Time : 2022/11/19 14:59
# @Author : 施树含
# @File ：Graph
# @Project : 新建文件夹

import networkx as nx
import matplotlib.pyplot as plt


# 绘制初始数据图
class Graph:
    # 这一步可以省略
    graph = nx.Graph()

    def __init__(self):
        self.graph = nx.Graph()

    # 根据txt文件创建图
    def createGraph(self, filename):
        file = open(filename, 'r')
        for line in file.readlines():
            nodes = line.split()
            edge = (int(nodes[0]), int(nodes[1]))
            self.graph.add_edge(*edge)

        return self.graph
