#假设图为
#此处用字典存储
grap={"A":["B","C"],
	  "B":["A","C","D"],
	  "C":["A","B","D","E"],
	  "D":["B","C","E","F"],
	  "E":["C","D"],
	  "F":["D"]
}
#获取图中节点 graph.keys()
#获取“E”的连接点  graph["E"]


#bfs需要两个参数，一个是图，一个是开始点
def bfs(graph,s)：#s是开始点
	#bfs需要队列，在python中直接用list[]即可
	queue=[]
	queue.append(s)
	#创建一个集合存放已经遍历过的节点
	seen=set()
	#把s放进去
	seen.add(s)
	#节点不为空就把队列最头节点拿出来
	while (len(queue)>0):
		#拿出来最头节点后，把与它相连的节点在放进去
		tmp=queue.pop(0)
		tmps=graph[tmp]
		for w in tmps:
			#如果w没被遍历过就往队列里面
			if w not in seen:
				queue.append(w)
				seen.add(w)
		print(tmp)
		
		
#bfs延伸求路径
#本质就是在bfs遍历的时候加一个parent表记录当前点上一个父节点是谁
#使用字典做映射
def bfs(graph,s)：#s是开始点
	#bfs需要队列，在python中直接用list[]即可
	queue=[]
	queue.append(s)
	#创建一个集合存放已经遍历过的节点
	seen=set()
	#把s放进去
	seen.add(s)
	#创建一个映射字典
	parents={s:None}
	#节点不为空就把队列最头节点拿出来
	while (len(queue)>0):
		#拿出来最头节点后，把与它相连的节点在放进去
		tmp=queue.pop(0)
		tmps=graph[tmp]
		for w in tmps:		
			#如果w没被遍历过就往队列里面
			if w not in seen:
				queue.append(w)
				seen.add(w)
				#添加到映射表中
				parents[w]=tmp
		print(tmp)
	return parents

#要找从E走向B的最短路径
parents=bfs(grap,"E")
v="B"
while v!=None:
	print(v)
	v=parents[v]
	
	
#--------------------------Dijkstra算法------------------------------
#求带有权值的最短路径算法
#由bfs改进过来，将队列变成优先队列
import heapq  # 这个头文件实现的是优先队列操作
import math

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
    # 访问AB的之间的距离 grap["A"]["B"]
}


def init(graph, s):
    distance = {s: 0}
    indexs = graph.keys()
    for w in indexs:
        if w!=s:
            distance[w] = math.inf
    return distance


def bfs_Dijkstra(grap, s):
    # 这里该使用优先队列
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    # 创建一个路径映射
    parents = {s: None}
    # 创建集合,与上面不同是从队列中取出的集合才算用过了
    seen = set()
    # 优先队列根据距离进行排序
    distance = init(graph, s)

    while (len(pqueue) > 0):
        tmp_pair = heapq.heappop(pqueue)
        tmp_index = tmp_pair[1]
        tmp_distance = tmp_pair[0]
        seen.add(tmp_index)
        # 取其连接点
        tmps_index = graph[tmp_index].keys()
        for w in tmps_index:
            # 和上面的区别在于此处是在这里判决点是否已经选出来了
            if w not in seen:
                if tmp_distance+ graph[tmp_index][w] < distance[w]:
                    distance[w] = tmp_distance+ graph[tmp_index][w]
                    # 更新映射
                    parents[w] = tmp_index
                    # 插入队列
                    heapq.heappush(pqueue, (distance[w], w))

    return parents, distance

parents,distance=bfs(graph,"A")
