#!/usr/bin/env python
# coding: utf-8

# # 美國原油庫存量增減方向預測
# ### 參數
# - 資料集(1982/8/20 ~ 今 )
# - 只採用最新500筆
# - 用9個數值預測隔週存貨(D6-E)漲跌
# - 前80%做training set (非亂數)
# - 以SVM做二元分類

import numpy as np
import pandas as pd
import math
from time import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


def train_predict(clf, X_train, y_train, X_test, y_test):
    print( "Training a {} using a training set size of {}. . .".format(clf.__class__.__name__, len(X_train)) )    
    clf.fit(X_train, y_train)
    
    y_pred_train = clf.predict(X_train)
    y_pred_test = clf.predict(X_test)
    score_train = accuracy_score(y_train, y_pred_train)
    score_test = accuracy_score(y_test, y_pred_test)
    
    print( "Accuracy for training set: {:.4f}.".format(score_train) )
    print( "Accuracy for test set: {:.4f}.".format(score_test) )
    

filename = "./weekly_supply_estimates_encoding.csv"
df = pd.read_csv(filename)
df = df[-500:]
y_all = df['Label_D6-E'].values
#D2-B,D2-D,D6-D,D6-E,D6-I,D6-J,D6-S,D6-AB,D7-B
x_all = df.drop(['Date','Label_D6-E','Label_D6-S','Label_D6-AB'], 1)
x_all = np.array(x_all)
y_all = np.array(y_all)
print(x_all.shape)

train_size = int(x_all.shape[0]*0.8)
X_train = x_all[0:train_size]
y_train = y_all[0:train_size]
X_test = x_all[train_size:]
y_test = y_all[train_size:]
X_train, XX_test, y_train, yy_test = train_test_split(X_train, y_train, test_size=0, random_state=42)
print(X_train.shape)
print(X_test.shape)

clf = SVC(C=128,gamma=0.0078125) 
train_predict(clf, X_train, y_train, X_test, y_test)
