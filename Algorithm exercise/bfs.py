#����ͼΪ
#�˴����ֵ�洢
grap={"A":["B","C"],
	  "B":["A","C","D"],
	  "C":["A","B","D","E"],
	  "D":["B","C","E","F"],
	  "E":["C","D"],
	  "F":["D"]
}
#��ȡͼ�нڵ� graph.keys()
#��ȡ��E�������ӵ�  graph["E"]


#bfs��Ҫ����������һ����ͼ��һ���ǿ�ʼ��
def bfs(graph,s)��#s�ǿ�ʼ��
	#bfs��Ҫ���У���python��ֱ����list[]����
	queue=[]
	queue.append(s)
	#����һ�����ϴ���Ѿ��������Ľڵ�
	seen=set()
	#��s�Ž�ȥ
	seen.add(s)
	#�ڵ㲻Ϊ�վͰѶ�����ͷ�ڵ��ó���
	while (len(queue)>0):
		#�ó�����ͷ�ڵ�󣬰����������Ľڵ��ڷŽ�ȥ
		tmp=queue.pop(0)
		tmps=graph[tmp]
		for w in tmps:
			#���wû��������������������
			if w not in seen:
				queue.append(w)
				seen.add(w)
		print(tmp)
		
		
#bfs������·��
#���ʾ�����bfs������ʱ���һ��parent���¼��ǰ����һ�����ڵ���˭
#ʹ���ֵ���ӳ��
def bfs(graph,s)��#s�ǿ�ʼ��
	#bfs��Ҫ���У���python��ֱ����list[]����
	queue=[]
	queue.append(s)
	#����һ�����ϴ���Ѿ��������Ľڵ�
	seen=set()
	#��s�Ž�ȥ
	seen.add(s)
	#����һ��ӳ���ֵ�
	parents={s:None}
	#�ڵ㲻Ϊ�վͰѶ�����ͷ�ڵ��ó���
	while (len(queue)>0):
		#�ó�����ͷ�ڵ�󣬰����������Ľڵ��ڷŽ�ȥ
		tmp=queue.pop(0)
		tmps=graph[tmp]
		for w in tmps:		
			#���wû��������������������
			if w not in seen:
				queue.append(w)
				seen.add(w)
				#��ӵ�ӳ�����
				parents[w]=tmp
		print(tmp)
	return parents

#Ҫ�Ҵ�E����B�����·��
parents=bfs(grap,"E")
v="B"
while v!=None:
	print(v)
	v=parents[v]
	
	
#--------------------------Dijkstra�㷨------------------------------
#�����Ȩֵ�����·���㷨
#��bfs�Ľ������������б�����ȶ���
import heapq  # ���ͷ�ļ�ʵ�ֵ������ȶ��в���
import math

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
    # ����AB��֮��ľ��� grap["A"]["B"]
}


def init(graph, s):
    distance = {s: 0}
    indexs = graph.keys()
    for w in indexs:
        if w!=s:
            distance[w] = math.inf
    return distance


def bfs_Dijkstra(grap, s):
    # �����ʹ�����ȶ���
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    # ����һ��·��ӳ��
    parents = {s: None}
    # ��������,�����治ͬ�ǴӶ�����ȡ���ļ��ϲ����ù���
    seen = set()
    # ���ȶ��и��ݾ����������
    distance = init(graph, s)

    while (len(pqueue) > 0):
        tmp_pair = heapq.heappop(pqueue)
        tmp_index = tmp_pair[1]
        tmp_distance = tmp_pair[0]
        seen.add(tmp_index)
        # ȡ�����ӵ�
        tmps_index = graph[tmp_index].keys()
        for w in tmps_index:
            # ��������������ڴ˴����������о����Ƿ��Ѿ�ѡ������
            if w not in seen:
                if tmp_distance+ graph[tmp_index][w] < distance[w]:
                    distance[w] = tmp_distance+ graph[tmp_index][w]
                    # ����ӳ��
                    parents[w] = tmp_index
                    # �������
                    heapq.heappush(pqueue, (distance[w], w))

    return parents, distance

parents,distance=bfs(graph,"A")
