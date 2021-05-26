#----------------------------------------------------------------


#################################################################
#--------------------------SVM-----------------------------------
#ѵ��ʱ��Զ�����ȳ�ʼ����Ȼ��һ��һ����ι�������и��µ�������

def select_j_rand(i ,m):
    # ѡȡalpha
    j = i
    while j == i:
        j = int(random.uniform(0, m))
    return j

def clip_alptha(aj, H, L):
    # �޼�alpha
    if aj > H:
        aj = H
    if L > aj:
        aj = L

    return aj

def smo(data_mat_In, class_label, C, toler, max_iter):
    # ת��Ϊnumpy��mat�洢
    data_matrix = np.mat(data_mat_In)
    label_mat = np.mat(class_label).transpose()
    # data_matrix = data_mat_In
    # label_mat = class_label
    # ��ʼ��b��ͳ��data_matrix��γ��
    b = 0
    m, n = np.shape(data_matrix)
    # ��ʼ��alpha����Ϊ0
    alphas = np.mat(np.zeros((m, 1)))
    # ��ʼ����������
    iter_num = 0
    # ������max_iter��
    while iter_num < max_iter:
        alpha_pairs_changed = 0
        for i in range(m):
		
            # �������Ei
			#data_matrix[i, :].T  //[i,:]ȡ��i�������ģ����ѵ�i�е�������ȡ����
            fxi = float(np.multiply(alphas, label_mat).T*(data_matrix*data_matrix[i, :].T)) + b
            Ei = fxi - float(label_mat[i])
            # �Ż�alpha���ɳ�����
            if (label_mat[i]*Ei < -toler and alphas[i] < C) or (label_mat[i]*Ei > toler and alphas[i] > 0):
                # ���ѡȡ��һ����alpha_j�ɶ��Ż���alpha_j
                j = select_j_rand(i, m)
                # 1.�������Ej
                fxj = float(np.multiply(alphas, label_mat).T*(data_matrix*data_matrix[j, :].T)) + b
                Ej = fxj - float(label_mat[j])
                # �������ǰ��alpha��deepcopy
                alpha_i_old = copy.deepcopy(alphas[i])
                alpha_j_old = copy.deepcopy(alphas[j])
                # 2.�������½�L��H
                if label_mat[i] != label_mat[j]:
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    print("L == H")
                    continue
                # 3.����eta
                eta = 2.0 * data_matrix[i, :]*data_matrix[j, :].T - data_matrix[i, :]*data_matrix[i, :].T - data_matrix[j, :]*data_matrix[j, :].T
                if eta >= 0:
                    print("eta >= 0")
                    continue
                # 4.����alpha_j
                alphas[j] -= label_mat[j]*(Ei - Ej)/eta
                # 5.�޼�alpha_j
                alphas[j] = clip_alptha(alphas[j], H, L)
                if abs(alphas[j] - alphas[i]) < 0.001:
                    print("alpha_j�仯̫С")
                    continue
                # 6.����alpha_i
                alphas[i] += label_mat[j]*label_mat[i]*(alpha_j_old - alphas[j])
                # 7.����b_1��b_2
                b_1 = b - Ei - label_mat[i]*(alphas[i] - alpha_i_old)*data_matrix[i, :]*data_matrix[i, :].T - label_mat[j]*(alphas[j] - alpha_j_old)*data_matrix[i, :]*data_matrix[j, :].T
                b_2 = b - Ej - label_mat[i]*(alphas[i] - alpha_i_old)*data_matrix[i, :]*data_matrix[j, :].T - label_mat[j]*(alphas[j] - alpha_j_old)*data_matrix[j, :] * data_matrix[j, :].T
                # 8.����b_1��b_2����b
                if 0 < alphas[i] and C > alphas[i]:
                    b = b_1
                elif 0 < alphas[j] and C > alphas[j]:
                    b = b_2
                else:
                    b = (b_1 + b_2)/2
                # ͳ���Ż�����
                alpha_pairs_changed += 1
                # ��ӡͳ����Ϣ
                print("��%d�ε��� ������%d , alpha�Ż�������%d" % (iter_num, i, alpha_pairs_changed))
        # ���µ�������
        if alpha_pairs_changed == 0:
            iter_num += 1
        else:
            iter_num = 0
        print("����������%d" % iter_num)

    return b, alphas


def caluelate_w(data_mat, label_mat, alphas):
    # ����w
    alphas = np.array(alphas)
    data_mat = np.array(data_mat)
    label_mat = np.array(label_mat)

    # numpy.tile(A, reps):ͨ���ظ�A�����Ĵ������������顣

    # numpy��reshape���������ֳ�������÷�
    # reshape(1, -1)ת����1�У�
    # reshape(2, -1)ת�������У�
    # reshape(-1, 1)ת����1�У�
    # reshape(-1, 2)ת��������

    w = np.dot((np.tile(label_mat.reshape(1, -1).T, (1, 5))*data_mat).T, alphas)
    return w.tolist()


def prediction(test, w, b):
    test = np.mat(test)
    result = []

    for i in test:
        if i*w+b > 0:
            result.append(1)
        else:
            result.append(-1)

    print(result)

    return result