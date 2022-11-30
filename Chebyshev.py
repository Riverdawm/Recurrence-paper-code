from numpy import *
import networkx as nx

def dist(i, j):  
    S_i_j = 0  #这里直接删除，写个等于零是为了不报错
    return 1 - S_i_j  #这里Sij替换成计算节点i和节点j的杰卡德相似度的函数


def Rho(G): #每个节点的影响力值（这里用节点的度表示），最终返回一个影响力值的列表，按照节点的id值排序，如n[0]的值就是id为1的节点的度，以此类推
    n = []
    for i in G.nodes():
        n.append(G.degree(i))
    return n

def Delta(G): #返回一个按照节点id顺序排列的列表，相对应位置存储的是各个节点的Delta值，即最小距离
    n = []
    a = Rho(G)
    m = max(a)
    for i in G.nodes():
        maxdist = -1
        if i == nx.number_of_nodes(G):
            mindist = dist(i, i - 1)
        else:
            mindist = dist(i, i + 1)
        if G.degree(i) == m:
            for j in G.nodes():
                if dist(i, j) > maxdist:
                    maxdist = dist(i, j)
        else:
            for j in G.nodes():
                if a[j - 1] > a[i - 1] and dist(i, j) < mindist:
                    mindist = dist(i, j)
        if maxdist == -1:
            n.append(mindist)
        else:
            n.append(maxdist)
    return n


def Qieb(a): #返回符合条件的节点，即筛选出距离大，影响力也大的节点
    n = []
    e = 2           #自己定义的艾普西隆值，越小选出来的点越少
    b = mean(a)     #求列表a的均值即数学期望E(X)
    c = std(a)      #数组a的标准差西格玛
    r = b + e * c
    for i in a:
        if i > r:
            n.append(a.index(i) + 1)
    return n


G = nx.read_gml(r'D:\AllMyTest\CommunityDetection-main\CommunityDetection-main\data_set\karate_club.gml')
r = []         #存储节点的伽马值，各个位置下标为id-1
n1 = Delta(G)  #节点最小距离列表，各个位置下标为id-1
n2 = Rho(G)    #节点度列表，各个位置下标为id-1
for i in range(nx.number_of_nodes(G)):
    r.append(n1[i] * n2[i])
GuanJianJieDian = Qieb(r)
print(GuanJianJieDian)

