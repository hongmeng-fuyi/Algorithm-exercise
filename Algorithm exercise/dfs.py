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

#�ǵݹ��dfsд��
#dfs��Ҫ����������һ����ͼ��һ���ǿ�ʼ��
def dfs(graph,s)��#s�ǿ�ʼ��
	#dfs��һ���ߵ�ͷ����Ҫ����ջ������ȳ�
	#����������ú���ȳ���֤һ��·�ߵ���
	stack=[]
	stack.append(s)
	seen=set()
	seen.add(s)
	while (len(stack)>0):
		#list�Ϳ���ʵ��stack��pop����ȡ���һ��
		tmp=stack.pop()
		tmps=graph[tmp]
		for w in tmps:
			if w not in seen:
				stack.append(w)
				seen.add(w)
		print(tmp)
		
#dfs�ĵݹ�д��
#�ݹ�д��      
seen=set()
def dfs(grah,s):
    if s not in seen:
        print(s)
        seen.add(s)
        #���������ҳ���
        tmps=grap[s]
        for w in tmps:
            #Ӧ������ѡһ�������
            dfss(grap,w)
    else:
        return
