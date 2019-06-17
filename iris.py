# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:21:55 2019
任务：花的识别
@author: Ericariel
"""

from sklearn.model_selection import train_test_split
from scipy.spatial.distance import euclidean
import numpy as np
import pandas as pd
import ai_utils


DATA_FILE = './data_ai/Iris.csv'

SPECIES = ['Iris-setosa',
           'Iris-versicolor',
           'Iris-virginica']

FEAT_COLS = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']

def get_pred_label(test_sample_feat, train_data):
    '''
    寻找最近距离样本
    '''
    dis_list=[]
    for idx, row in train_data.iterrows():
        # 训练样本特征
        train_sample_feat = row[FEAT_COLS].values
        # 计算距离
        dis = euclidean(test_sample_feat, train_sample_feat)
        dis_list.append(dis)
    pos = np.argmin(dis_list)
    pred_label = train_data.iloc[pos]['Species']
    return pred_label

def main():
    """
    主函数
    """
    # 读取数据集
    iris_data = pd.read_csv(DATA_FILE, index_col='Id')
    
    # EDA
    ai_utils.do_eda_plot_for_iris(iris_data)
    
    # 划分数据集
    train_data, test_data = train_test_split(iris_data, test_size=1/3, random_state=10)

    acc_count = 0

    # 分类器
    for idx, row in test_data.iterrows():
        # 测试样本特征
        test_sample_feat = row[FEAT_COLS].values

        # 预测值
        pred_lable = get_pred_label(test_sample_feat, train_data)

        #真实值
        true_label = row['Species']

        print('样本{}的真实标签是{}，预测标签是{}'.format(idx, true_label, pred_lable))

        if true_label == pred_lable:
            acc_count+=1

    accuracy = acc_count / test_data.shape[0]
    print('预测准确率为{:.2f}%'.format(accuracy * 100))
    
if __name__=='__main__':
    main()