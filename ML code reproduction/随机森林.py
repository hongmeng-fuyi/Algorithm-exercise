
#���ɭ�����ö��������������ѵ����Ԥ���һ�ַ�����

#����������ѡ����������Ŀ�����ѡ��ѵ������
#���ʾ��������������������˲���

#���ɭ��ʵ����һ�������bagging������������������bagging��
#��bootstrap��������m��ѵ��������ÿ��ѵ��������һ�ž��������ڵ�������ʱ
#����ѡ�񵥸���Ϣ���������������������ȡһ��������


#--------------------------------------------------------------------
#-------------------���ɭ��----------------------------------------

#�㷨
#��N����ʾѵ���������������ĸ�����M��ʾ������Ŀ��
#����������Ŀm������ȷ����������һ���ڵ�ľ��߽��������mӦԶС��M��
#��N��ѵ�������������������зŻس����ķ�ʽ��ȡ��N�Σ��γ�һ��ѵ��������bootstrapȡ����������δ�鵽����������������Ԥ�⣬��������
#����ÿһ���ڵ㣬���ѡ��m����������������ÿ���ڵ�ľ������ǻ�����Щ����ȷ���ġ�������m����������������ѵķ��ѷ�ʽ��
#ÿ�������������ɳ��������֦�����п����ڽ���һ��������״��������ᱻ���ã���



#����ϵ��
#���ݼ�D�Ĵ��ȿ����û���ֵ������
#Gini��D����ӳ�˴����ݼ�D�����ѡȡ����������������ǲ�һ�µĸ��ʣ�
#���Gini��D��ԽС�������ݼ�D�Ĵ���Խ�ߡ�


#�������ϵ��
#i�Ǳ�ʾѡ���������𣿣�����
def gini(data, i):

    num = len(data)
    label_counts = [0, 0, 0, 0]

    p_count = [0, 0, 0, 0]

    gini_count = [0, 0, 0, 0]

    for d in data:
        label_counts[d[i]] += 1

    for l in range(len(label_counts)):
        for d in data:
            if label_counts[l] != 0 and d[0] == 1 and d[i] == l:
                p_count[l] += 1


    for l in range(len(label_counts)):
        if label_counts[l] != 0:
            gini_count[l] = 2*(p_count[l]/label_counts[l])*(1 - p_count[l]/label_counts[l])

    gini_p = 0
    for l in range(len(gini_count)):
        gini_p += (label_counts[l]/num)*gini_count[l]



    return gini_p


#��ѡ���Լ���A�У�ѡ���Ǹ�ʹ�û��ֺ����ָ����С��������Ϊ���Ż�������

def get_best_feature(data, category):
    if len(category) == 2:
        return 1, category[1]

    feature_num = len(category) - 1
    data_num = len(data)

    feature_gini = []

    for i in range(1, feature_num+1):
        feature_gini.append(gini(data, i))

    min = 0

    for i in range(len(feature_gini)):
        if feature_gini[i] < feature_gini[min]:
            min = i

    print(feature_gini)
    print(category)
    print(min+1)
    print(category[min+1])

    return min+1, category[min + 1]
	
	

class Node(object):
	def __init__(self,item):
		self.name=item
		self.lchild=None
		self.rchild=None
		
def creat_tree(data, labels, feature_labels=[]):
# ���ֽ������
    # ȡ�����ǩ(survivor or death)
    class_list = [exampel[0] for exampel in data]

    if class_list == []:
        return Node(0)
    # ��������ȫ��ͬ��ֹͣ����
    if class_list.count(class_list[0]) == len(class_list):
        return Node(class_list[0])
    # ��������������ʱ���س��ִ����������ǩ
    if len(data[0]) == 1:
        return Node(majority_cnt(class_list))

    # ���������ı�ǩ
    best_feature_num, best_feature_label = get_best_feature(data, labels)

    feature_labels.append(best_feature_label)

    node = Node(best_feature_label)

    ldata = []
    rdata = []

    for d in data:
        if d[best_feature_num] == 1:
            del(d[best_feature_num])
            ldata.append(d)
        else:
            del(d[best_feature_num])
            rdata.append(d)

    labels2 = copy.deepcopy(labels)
    del(labels2[best_feature_num])

    tree = node
    tree.lchild = creat_tree(ldata, labels2, feature_labels)
    tree.rchild = creat_tree(rdata, labels2, feature_labels)

    return tree

#ͳ�Ʒ���
def majority_cnt(class_list):
    class_count = {}
    # ͳ��class_list��ÿ��Ԫ�س��ֵĴ���
    for vote in class_list:
        if vote not in class_count:
            class_count[vote] = 0
        class_count[vote] += 1
        # �����ֵ��ֵ��������
        sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]

#Ԥ�����
def pre(t_test, labels, tree):
    result = []
    r = []

    for i in range(len(t_test)):
            label = []
            label = copy.deepcopy(labels[i])
            print(label)
            breadth_travel(tree[i])
            r.append(prediction(tree[i], t_test[i], label))
    rr = []
    for i in range(len(r[0])):
        rr.append([])

    for i in range(len(rr)):
        for j in range(len(r)):
            rr[i].append(r[j][i])

    print(rr)

    for i in range(len(rr)):
        result.append(majority_cnt(rr[i]))
    return result
	

#------------main--------------

#����10����
	tree_num=10
	bootsrapping=[]
	b_category=[]

	#����10����
	for i in range(tree_num):
        b_category.append(copy.deepcopy(category))
		
        bootstrapping.append([])
		#���ݼ������ѡȡ����
		#Ϊʲô����о��ǰ�ȫ��������ѡ���ˣ�ֻ�������һ��˳�����
		#�������зŻص����������Ҳ����˵�����ܳ����˺ͳ�����Ŀ�����ݼ���Ŀһ��
		#�����������ݼ����ݲ�����ԭ�����ݼ�
		#��Ȼ���������Ŀ����Ӧ���ǿ����Լ�����
        for j in range(len(data_set)):
            bootstrapping[i].append(copy.deepcopy(data_set[int(np.floor(np.random.random() * len(data_set)))]))
			
	
	#��ÿ�����������ѡȡ����,ԭ����������5�����ѡȡ������Ϊ2��
	for i in range(tree_num):
		#����õ������±�
		n_num_category[i].append(random.sample(range(1, 5), 2))
	
	#��Ҫ������ֵת���������������������
	#���ϴ���û����ɶ��˼ ���о�Ӧ���������˼������
	b_category<------n_num_category

	
	#Ϊÿ����������
	for i in range(tree_num):
		my_tree.append(creat_tree(bootstrapping[i], b_category[i]))