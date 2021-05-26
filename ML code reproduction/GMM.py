



class GMM:
	#��˹Ȩ�س�ʼ��
	def __init__(self.Data,k,weights=Noe,means=None,covars=None):
		"""
        ����GMM����˹���ģ�ͣ���Ĺ��캯��
        :param Data: ѵ������
        :param K: ��˹�ֲ��ĸ���
        :param weigths: ÿ����˹�ֲ��ĳ�ʼ���ʣ�Ȩ�أ�
        :param means: ��˹�ֲ��ľ�ֵ����
        :param covars: ��˹�ֲ���Э������󼯺�
        """
		
		self.Data = Data
        self.K = K
		#��ʼ��������ά�Ⱥ�����������ά���й�
		col = np.shape(self.Data)[1]
        if weights is not None:
            self.weights = weights
        else:
            self.weights  = np.random.rand(self.K)
            self.weights /= np.sum(self.weights)        # ��һ��
			
		if means is not None:
            self.means = means
        else:
            self.means = []
            for i in range(self.K):
                mean = np.random.rand(col)
                #mean = mean / np.sum(mean)        # ��һ��
                self.means.append(mean)
				
		if covars is not None:
            self.covars = covars
        else:
            self.covars  = []
            for i in range(self.K):
                cov = np.random.rand(col,col)
                #cov = cov / np.sum(cov)                    # ��һ��
                self.covars.append(cov)                     # cov��np.array,����self.covars��list
				
				
	def Gaussian(self,x,mean,cov):
        """
        �����Զ���ĸ�˹�ֲ������ܶȺ���
        :param x: ��������
        :param mean: ��ֵ����
        :param cov: Э�������
        :return: x�ĸ���
        """
        dim = np.shape(cov)[0]
        # cov������ʽΪ��ʱ�Ĵ�ʩ
		#np.linalg.det����a������ʽ
        covdet = np.linalg.det(cov + np.eye(dim) * 0.001)
		#np.linalg.inv()����������
        covinv = np.linalg.inv(cov + np.eye(dim) * 0.001)
		#�����x-u
        xdiff = (x - mean).reshape((1,dim))
        #���ݹ�ʽ������ܶ�
		#��Ҫ֪��Э�����ֵ��ά����
        prob = 1.0/(np.power(np.power(2*np.pi,dim)*np.abs(covdet),0.5))*\
               np.exp(-0.5*xdiff.dot(covinv).dot(xdiff.T))[0][0]
		#Ϊʲôȡ[0][0]��
		#ʲôʱ����np.dot()
        return prob
		
	def GMM_EM(self):
        """
        ��������EM�㷨�����Ż�GMM�����ĺ���
        :return: ���ظ������ݵ�����ÿ������ĸ���
        """
        loglikelyhood = 0
        oldloglikelyhood = 1
        len,dim = np.shape(self.Data)
        # gamma��ʾ��n���������ڵ�k����ϸ�˹�ĸ���
        gammas = [np.zeros(self.K) for i in range(len)]
        while np.abs(loglikelyhood-oldloglikelyhood) > 0.00000001:
            oldloglikelyhood = loglikelyhood
            # E-step
            for n in range(len):
                # respons��GMM��EM�㷨��Ȩ��Ϊw�ĺ������
                respons = [self.weights[k] * self.Gaussian(self.Data[n], self.means[k], self.covars[k])
                                                    for k in range(self.K)]
                respons = np.array(respons)
                sum_respons = np.sum(respons)
                gammas[n] = respons/sum_respons
            # M-step
            for k in range(self.K):
                #nk��ʾN���������ж������ڵ�k����˹
                nk = np.sum([gammas[n][k] for n in range(len)])
                # ����ÿ����˹�ֲ��ĸ���
                self.weights[k] = 1.0 * nk / len
                # ���¸�˹�ֲ��ľ�ֵ
                self.means[k] = (1.0/nk) * np.sum([gammas[n][k] * self.Data[n] for n in range(len)], axis=0)
                # ���¸�˹�ֲ���Э�������
				xdiffs = self.Data - self.means[k]
                self.covars[k] = (1.0/nk)*np.sum([gammas[n][k]*xdiffs[n].reshape((dim,1)).dot(xdiffs[n].reshape((1,dim))) for n in range(len)],axis=0)
            loglikelyhood = []
            for n in range(len):
                tmp = [np.sum(self.weights[k]*self.Gaussian(self.Data[n],self.means[k],self.covars[k])) for k in range(self.K)]
                tmp = np.log(np.array(tmp))
                loglikelyhood.append(list(tmp))
            loglikelyhood = np.sum(loglikelyhood)
        for i in range(len):
            gammas[i] = gammas[i]/np.sum(gammas[i])
        self.posibility = gammas
        self.prediction = [np.argmax(gammas[i]) for i in range(len)]
		
		
if __name__=="__main__":
# GMMģ��
    K = 3
    gmm = GMM(data,K)
    gmm.GMM_EM()
    y_pre = gmm.prediction

	
	