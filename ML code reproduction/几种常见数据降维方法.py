
#д��ʽһ��Ҫ������±���ô���

#��ά��Ϊ�˽��ά�����ѣ��������ռ��һ����ά�ռ�任����һ����ά�ռ�




#--------------------------------------------------------------------
#---------MDS:MultiDimensional Scaling ��ά�߶ȱ任------------------


def calculate_distanc(x,y):
	d=np.sqrt(np.sum((x-y)**2)
	return d
	
# ����������֮���ŷʽ���룻x����ĵ�i����y����ĵ�0-j�м���ŷʽ������㣬�����¾����i��[i0��i1...ij]	
def calculate_distanc_matrix(x,y):
	d=metrics.pairwise_distance(x,y)
	return d

def  cla_B(D):
	(n1,n2)=D.shape
	DD=np.square(D)
	Di=np.sum(DD,axis=1)/n1
	Dj=np.sum(DD,axis=0)/n1
	Dij=np.sum(DD)/(n1**2)
	B=np.zeros((n1,n1))
	for i in range(n1):
		for j in range(n2):
			B[i,j]=(-1/2)*(Dij+DD[i,j]-Di[i]-Dj[j])
	
	return B
	
def MDS(data,n=2):
	D=calculate_distanc_matrix(data,data)
	B=cal_B(D)
	#����ֵ�ֽ�
	Be,Bv=np.linalg.eigh(B)
	Be_sort=np.argsort(-Be)
	#����ֵ�Ӵ�С����
	Be=Be[Be_sort]
	Bv=Bv[:,Be_sort]
	# ǰn������ֵ�ԽǾ���
	Bez=np.diag(Be[0:n])
	 # ǰn����һ����������
	Bvz=Bv=[:,0:n]
	Z=np.dot(np.sqrt(Bez),Bvz.T).T
	return Z
	
	
#-----------------------------------------------------------
#----------------------------ISOMAP-------------------------
#��MDS����ISOMAP��ͼ����������·���������MDS��ŷ�Ͽռ����
#���룺������D={x1,x2,...,xm},���ڲ���k,��ά�ռ�ά��
#���̣�
#	for i =1,2,3,...,m 
#		do ȷ��xi��k����
#		xi��k���ڵ�֮��ľ�������Ϊŷ�Ͼ��룬���������������Ϊ��ǿ��
#    end  for
# �������·���㷨������������������֮��ľ���dist(xi,xj)
# ��dist(xi,xj)��ΪMDS���㷨������
# return MDS�㷨�����
#����� ������D�ڵ�ά�ռ��ͶӰZ={z1,z2,..,}

#�㷨������ʱ�������������㣬�ڴ����Ӧ���У�������������ά��������ά��

def my_mds(dist,n_dims):
	
	n=dist.shape[0]
	
	dist=dist**2
	T1=np.ones((n,n))*np.sum(dist)/n**2
	T2=np.sum(dist,axis=1)/n
	T3=np.sum(dist,axis=0)/n
	
	B=-(T1-T2-T3+dist)/2
	
	eig_val��eig_vector=np.linalg.eig(B)
	#�Ӵ�С��
	index_=np.argsort(-eig_val)[:n_dims]
	picked_eig_val=eig_val[index_].real
	picked_eig_vector=eig_vector[:,index_]
	
	return picked_eig_val*picked_eig_val**(0.5)
	



#������������ͼ����̾�����㷨
def floyd(D,n_neighbors):
		
	n1,n2=D.shape
	k=n_neighbors
	#��ʼ��������Ϊ�����
	Max=np.max(D)*1000
	D1=np.one((n1,n1))*Max
	
	#argsort()�����ǽ������е�Ԫ�ش�С�������У�axis=1��������
	#��ȡ���Ӧ��index(����)��Ȼ�������y��Ҳ����˵D_rag������
	#����ͼ��������������ʵ�ʾ��ǰ�ÿ���㵽���еĵ�ľ����������
	D_rag=np.argsort(D,axis=1)
	#�������е㣬�ҵ��������������k��
	for i in range(n1):
		#ѡȡ�����k
		D1[i,D_rag[i,0:k+1]]=D[i,D_arg[i,0:k+1]]
	#ͼ���������·���㷨
	for m in range(n1):
		for i in range(n1):
			for j in range(n1):
				if D1[i,m]+D1[m,j]<D1[i,j]:
					D1[i,j]=D1[i,m]+D1[m,j]
					
	return D1
	

def cal_pairwise_dist(x):
    '''����pairwise ����, x��matrix
    (a-b)^2 = a^2 + b^2 - 2*a*b
    '''
	#np.square�����Ԫ�ص�ƽ�� 
    sum_x = np.sum(np.square(x), 1)
    dist = np.add(np.add(-2 * np.dot(x, x.T), sum_x).T, sum_x)
    #��������������֮������ƽ��
    return dist

def my_isomap(data,n=2,n_neighbors=30):
	D=cal_pariwise_dist(data)
	#��һ������Ҳ����û��
	D[D<0]=0
	D=D**0.5
	#D�����㷨��������˵��ͼ
	#��ͼ�м���k����
	D_floyd=floyd(D,n_neighbors)
	#��ʱ�Ϳ��Ե���my_mds
	data_n=my_mds(D_floyd,n_dims=n)
	return data_n

#------------------------------------------------------------
#-----------------------PCA----------------------------------

def pca(data, n):

    data = np.array(data)
    # ��ֵ
    mean_vector = np.mean(data, axis=0)
    # Э����
    cov_mat = np.cov(data - mean_vector, rowvar=0)
    # ����ֵ ��������
    fvalue, fvector = np.linalg.eig(cov_mat)
    # ����
    fvaluesort = np.argsort(-fvalue)
    # ȡǰ��������
    fValueTopN = fvaluesort[:n]
    # ����ǰ�������ֵ
    newdata = fvector[:, fValueTopN]
    new = np.dot(data, newdata)
    return new
	
	
#-------------------------------------------------------------
#-------------LDA��Linear Discriminant Analysis---------------
#��PCAһ������һ�����Խ�ά�㷨��
#��ͬ��PCAֻ��ѡ�����ݱ仯���ķ���
#����LDA���мල�ģ������ǩ����
#����LDA����Ҫ�����Ϊ˼�����أ�ʹ��ͶӰ������������ܿɷ֡�


def lda_num2(data1,  data2,  n=2):
    mu0 = data2.mean(0)
    mu1 = data1.mean(0)
    print(mu0)
    print(mu1)

    sum0 = np.zeros((mu0.shape[0], mu0.shape[0]))
    for i in range(len(data2)):
        sum0 += np.dot((data2[i] - mu0).T, (data2[i] - mu0))
    sum1 = np.zeros(mu1.shape[0])
    for i in range(len(data1)):
        sum1 += np.dot((data1[i] - mu1).T, (data1[i] - mu1))

    s_w = sum0 + sum1
    print(s_w)
    w = np.linalg.pinv(s_w) * (mu0 - mu1)

    new_w = w[:n].T

    new_data1 = np.dot(data1, new_w)
    new_data2 = np.dot(data2, new_w)

    return new_data1, new_data2
	
	
#-------------------------------------------------------------
#-------------t-SNE Stochastic Neighbor Embedding--------------
#ǰ���Ǳ�֤���벻�䣬tSNE��֤���Ǹ��ʷֲ�����
#t-SNE��SNE�ĸĽ��棬ʹ��t�ֲ������˹�ֲ��������֮������ƶ�
#SNE���Ƚ�ŷ����þ���ת��Ϊ�����������������֮������ƶ�
#�������Pij������Ϊ������


#����ÿһ����������Ϣ��
def cal_entropy(D,beta):
	#��Ϣ����μ��㣿������͹�ʽ��һ����
	#beta {float} -- ��1/(2sigma^2)
    
	P=np.exp(-D*beta)
    sumP=sum(P)
    sumP=np.maximum(sumP,1e-200)
	#H���㹫ʽ����һ������
    H=np.log(sumP) + beta * np.sum(D * P) / sumP
    return H


def cal_p(D,entropy,K=50):
	#ÿһ�еļ��㶼��Ҫ�ҵ�һ������beta
	#delta�����������ԭ��������������ز��ܳ���entropy
	#����һ����ʼֵ������������ֵ
	beta=1.0
	#����ÿһ����������Ϣ��
	H=cal_entropy(D,beta)
	error=H-entropy
	k=0
	betmin=-np.inf
	betmax=np.inf
	#ÿһ�еļ��㶼��Ҫ�ҵ�һ������beta��ʹ����һ�еķֲ���С�ڵ���log(neighbors)
	#��������Ѱ��beta
	while error>=1e-4 and k<=K:
		#˵��������ȡ����ֵ
		if error>0:
			betmin=copy.deepcopy(beta)
			if betmax=np.inf:
				beta=beta*2
			else:
				beta=(beta+betmax)/2
		
		else:
		#˵��ȡֵȡ����
            betamax=copy.deepcopy(beta)
            if betamin==-numpy.inf:
                beta=beta/2
            else:
                beta=(beta+betamin)/2
				
		#���¼���
		H=cal_entropy(D,beta)
		error=H-entropy
        k+=1
	#���ݹ�ʽ��
	P=numpy.exp(-D*beta)
    P=P/numpy.sum(P)
    return P

#�����ά�ռ�ֲ�
def cal_matrix_P(x,neigbors):
	#�����Ϣ�ز��ܳ����ֵ
	entropy=np.log(neigbors)
	n1,n2=x.shape
	D=np.square(metrics.pairwise_distance(x))
	#����͵�˸�����û��������㣬���Ƕ����ݽ���������ѡȡ����ǰ��k����Ϊ�����
	D_sort=np.argsort(D,axis=1)
	#p(i,j)��ʾ���ǵ�i�������ڵ�j��������Χ�ĸ���
	#����P�Ĵ�С��n1
	P=np.zeros((n1,n1))
	for i in xrange(n1):
		Di=D[i,D_sort[i,1:]]
		P[i,D_sort[i,1:]]=cal_p(Di,entropy=entropy)
	
	#���ݹ�ʽ���	p=(pij+pji)/2*n
	P=(P+np.transpose(P))/(2*n1)
	P=np.maximum(P,1e-100)
	return P
	
	
	
#�����ά�ռ�ֲ�Q
def cal_matrix_Q(Y):
	n1,n2=Y.shape
    D=numpy.square(metrics.pairwise_distances(Y))
	#���ݹ�ʽ��
	Q=(1/(1+D))/(np.sum(1/(1+D))-n1)
	#���漸���о���дҲ��
	Q=Q/(np.sum(Q)-np.sum(Q[range(n1),range(n1)]))
	Q[range(n1),range(n1)]=0
	Q=np.maximum(Q,1e-100)
	return Q


#������ʧ����KLɢ��
def cal_loss(P,Q):
	C=np.sum(p*np.log(p/Q))
	return C

	
#�����ݶ�	
#�ͼ��㹫ʽ��һ��
def cal_gradients(P,Q,Y):
    n1,n2=Y.shape
    DC=numpy.zeros((n1,n2))
    for i in xrange(n1):
	
        E=(1+np.sum((Y[i,:]-Y)**2,axis=1))**(-1)
        F=Y[i,:]-Y
        G=(P[i,:]-Q[i,:])
		
        E=E.reshape((-1,1))
        G=G.reshape((-1,1))
        G=np.tile(G,(1,n2))
        E=np.tile(E,(1,n2))
        DC[i,:]=np.sum(4*G*E*F,axis=0)
    return DC
		

		

def tsne(X,n=2,neighbors=30,max_iter=200):

    n1,n2=X.shape
    P=cal_matrix_P(X,neighbors)
    Y=numpy.random.randn(n1,n)*1e-4
	
    Q = cal_matrix_Q(Y)
	#�ݶ�
    DY = cal_gradients(P, Q, Y)
    A=200.0
    B=0.1
	#��ʼ����
    for i  in xrange(max_iter):
        data.append(Y)
		#��һ������
        if i==0:
            Y=Y-A*DY
            Y1=Y
            error1=cal_loss(P,Q)
		#�ڶ�������
        elif i==1:
            Y=Y-A*DY
            Y2=Y
            error2=cal_loss(P,Q)
        else:
			#��ʽ
            YY=Y-A*DY+B*(Y2-Y1)
            QQ = cal_matrix_Q(YY)
			#ɢ�Ⱥ�������
            error=cal_loss(P,QQ)
            if error>error2:
                A=A*0.7
                continue
            elif (error-error2)>(error2-error1):
                A=A*1.2
            Y=YY
            error1=error2
            error2=error
            Q = QQ
			#��ϸ�ݶ�
            DY = cal_gradients(P, Q, Y)
            Y1=Y2
            Y2=Y
        if cal_loss(P,Q)<1e-3:
            return Y
        if numpy.fmod(i+1,10)==0:
            print '%s iterations the error is %s, A is %s'%(str(i+1),str(round(cal_loss(P,Q),2)),str(round(A,3)))
    tsne_dat['data']=data
    tsne_dat.close()
    return Y
	



