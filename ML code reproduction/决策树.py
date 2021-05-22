
#����ֻ����ѧ��ʽ��һ��Ҫ�������ѧ��ʽת����ʵ�ʵ�������
#����Ҫ֪�������ص���������δ����д�ɴ����
#��Ҫ֪��������ɢ�� �������ת���ɸ��ʵ�

#������ѧϰ�������Ǵ�ѵ�����ݼ��й��ɳ�һ��������
#������ѧϰ���㷨ͨ����һ���ݹ��ѡ����������
#��������ѡ�񡢾����������ɺ;������ļ�֦���̡�


#-------------------------------------------------------
#----------------ID3------------------------------------
#ID3�㷨����Ϣ�������������Ե�ѡ��,ѡ����Ѻ���Ϣ�����������Խ��з���

#���ﲢ������������һ�����ṹ������һ�������߼��о��ṹ�����ж�ɶ���ж�ɶ
#{{{{}}}}���������ŵĴ��
#�ҳ����ִ������ķ�������
def majorityCnt(classList):  
    classCount = {}  
    for vote in classList:  
        if vote not in classCount.keys(): classCount[vote] = 0  
        classCount[vote] += 1  
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0] 


#��ȥ����������õ��µ��Ӽ�
def splitDataSet(data_set, axis, value):
    ret_dataset = []
    for feat_vec in data_set:
        if feat_vec[axis] == value:
            reduced_feat_vec = feat_vec[:axis]
            reduced_feat_vec.extend(feat_vec[axis + 1:])
            ret_dataset.append(reduced_feat_vec)
    return ret_dataset

#������
def calcShannonEnt(dataSet):
	#ͳ����������
	numEntries=len(dataset)
	#�洢ÿ��label���ֵĴ���
	label_counts={}
	#ͳ��label���ֵĴ���
	for featVec in dataSet:
		current_label=featVec[-1]:
		if current_label not in label_counts:
			label_counts[current_label]=0
		label_counts[current_label]+=1
	
	shannon_ent=0
	#���㾭����
	for key in label_counts:
	#���ݹ�ʽ����
		prob=float(label_counts[key])/numEntries
		shannon_ent-=prob*log(prob,2)
	
	return shannon_ent
	
#ѡ����õ��������з�֧
def chooseBestFeatureToSplit(dataSet):
	#��������
	num_features=len(dataSet[0])-1
	#������
	base_entropy=calcShannonEnt(dataSet)
    # ��Ϣ����
    best_info_gain = 0.0
	#������������ֵ
	best_feature=-1
	#���������������Ե�ǰ��������������
	#��ϸ�����ķ��ּ��㵱ǰ���������أ������Ե�ǰ����ȡ��ȥ������Ӽ����м���õ�����Ϊ������
	for i in range(num_features)
		#��ȡdataset��i������
		feat_list=[exampe[i] for exampe in dataSet]
		#����set���ϣ�Ԫ�ز����غ�
		unique_val=set(feat_list)
		#���ݹ�ʽ������Ϣ��������Ϣ����
		for value in unique_val:
			sub_dataset=splitDataSet(dataSet,i,value)
			#��һ�������ǲ���������
			#�����Ӽ����ֵĸ���
			prob=len(sub_dataset)/float(len(dataset))
			#���㾭��������---��ʽ
			#��ϸ�����ķ��ּ��㵱ǰ���������أ������Ե�ǰ����ȡ��ȥ������Ӽ����м���õ�����Ϊ������
			new_entropy+=prob*calcShannonEnt(sub_dataset)
		#��Ϣ����--��ʽ
		info_gain=base_entropy-new_entropy
		
		# ��ӡÿ����������Ϣ����
        print("��%d����������Ϣ����Ϊ%.3f" % (i, info_gain))
		
		if info_gain > best_info_gain:
            # ������Ϣ����
            best_info_gain = info_gain
            # ��¼��Ϣ������������������ֵ
            best_feature = i
		
	print("��������ֵ��" + str(best_feature))
    print()
    return best_feature

#��ȡ���������	
def get_tree_depth(my_tree):
    max_depth = 0       # ��ʼ�����������
    firsr_str = next(iter(my_tree))     # python3��myTree.keys()���ص���dict_keys,������list,���Բ���ʹ��myTree.keys()[0]�ķ�����ȡ������ԣ�����ʹ��list(myTree.keys())[0]
    second_dict = my_tree[firsr_str]    # ��ȡ��һ���ֵ�
    for key in second_dict.keys():
        if type(second_dict[key]).__name__ == 'dict':     # ���Ըý���Ƿ�Ϊ�ֵ䣬��������ֵ䣬����˽��ΪҶ�ӽ��
            this_depth = 1 + get_tree_depth(second_dict[key])
        else:
            this_depth = 1
        if this_depth > max_depth:
            max_depth = this_depth      # ���²���
    return max_depth

#������Ǳ�����ģ�͵�Ҷ�ӽڵ�
#next() ���ص���������һ����Ŀ
#next() ����Ҫ�����ɵ������� iter() ����һ��ʹ�á�
	
def classify(input_tree, feat_labels, test_vec):
    # ��ȡ�������ڵ�
    first_str = next(iter(input_tree))
    # ��һ���ֵ�
    second_dict = input_tree[first_str]
    feat_index = feat_labels.index(first_str)

    for key in second_dict.keys():
        if test_vec[feat_index] == key:
            if type(second_dict[key]).__name__ == 'dict':
                class_label = classify(second_dict[key], feat_labels, test_vec)
            else:
                class_label = second_dict[key]
    return class_label
	
	
def create_tree(dataSet,Labels,featLabels):
	# ���ݼ�
    dataSet = [[0, 0, 0, 0, 'no'],
               [0, 0, 0, 1, 'no'],
               [0, 1, 0, 1, 'yes'],
               [0, 1, 1, 0, 'yes'],
               [0, 0, 0, 0, 'no'],
               [1, 0, 0, 0, 'no'],
              # [1, 0, 0, 0, 'yes'],
               [1, 0, 0, 1, 'no'],
               [1, 1, 1, 1, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [2, 0, 1, 2, 'yes'],
               [2, 0, 1, 1, 'yes'],
               [2, 1, 0, 1, 'yes'],
               [2, 1, 0, 2, 'yes'],
               [2, 0, 0, 0, 'no']]
    # ��������
    labels = ['����', '�й���', '���Լ��ķ���', '�Ŵ����']
	
	
	
	#ȡ�����ǩ���Ƿ�Ŵ���yes or no��
	class_list=[exampel[-1] for exampel in dataSet]	
	
	# ֻʣ��һ�����ʱ�Ͳ��÷�����
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # ��������������ʱ���س��ִ����������ǩ
	#��dataSet[0]ֻ��һ�����ȵ�ʱ�򣬱�ʾ�Ѿ������һ��������
	#�����ǲ���ֱ����dataset���Ⱦ��� ���ö�λ��[0]??
    if len(dataSet[0]) == 1:
        return majority_cnt(class_list)
	
	
	#ѡ����������
	best_feature = chooseBestFeatureToSplit(dataSet)
	# ���������ı�ǩ
    best_feature_label = labels[best_feature] 
	featLabels.append(best_feature_label)
	
	#��������������ǩ������
	my_tree={best_feature_label:{}}#����{���䣺{���䣨1�������1��{...}�����䣨2�������2��{.....}}}
	#����ɾ���Ѿ�ʹ�ñ�ǩ
	del(labels[best_feature])
	
	# �õ�ѵ������������������������ֵ(ĳһ�е�ֵ)
    feat_value = [exampel[best_feature] for exampel in dataSet]
    # ȥ���ظ�����ֵ
    unique_vls = set(feat_value)
    for value in unique_vls:
        my_tree[best_feature_label][value] = 
				creat_tree(splitDataSet(dataSet, best_feature, value), labels, featLabels)
	
	return my_tree
	
if __name___=="__main__":
	
	#
	featLabels=[]
	
	#������
	myTree=create_tree(dataSet,labels,featLabels)

	
