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

#非递归的dfs写法
#dfs需要两个参数，一个是图，一个是开始点
def dfs(graph,s)：#s是开始点
	#dfs是一步走到头，需要的是栈，后进先出
	#这里就是利用后进先出保证一条路走到底
	stack=[]
	stack.append(s)
	seen=set()
	seen.add(s)
	while (len(stack)>0):
		#list就可以实现stack，pop就是取最后一个
		tmp=stack.pop()
		tmps=graph[tmp]
		for w in tmps:
			if w not in seen:
				stack.append(w)
				seen.add(w)
		print(tmp)
		
#dfs的递归写法
#递归写法      
seen=set()
def dfs(grah,s):
    if s not in seen:
        print(s)
        seen.add(s)
        #把相连点找出来
        tmps=grap[s]
        for w in tmps:
            #应该是先选一个点遍历
            dfss(grap,w)
    else:
        return
