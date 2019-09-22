# 美國原油存量漲跌方向預測

## 實驗目的

- 取得美國政府提供的能源資料，以每週的原油輸入等各種數值為特徵值，隔週的 原油存量為標注資料，以支持向量機等機器學習演算法，訓練一個預估模型。
- 若可以用能源歷史資料預估未來(隔週)的原油存量增減方向，即可藉此預估未來 的油價漲跌方向，進而以此作為期貨交易的參考資訊。

## 實驗方法

### 資料來源 (Datasource)
- U.S. Energy Information Administration

### 資料集 (Dataset)
- Weekly Supply Estimates
- July 31, 2009 ~ March 1, 2019
- Total is 500 data points.

### 特徵值 (Features)
- 取 Data2-B, Data2-D, ...., 等多個欄位，將 t-1 日至 t 日之差額的正負作為特徵值，差額正值為1，負值為0。

### 標注值 (Label)
- 取 Data6-E 資料，將 t 日至 t+1日之差額的正負作為標註 值，差額正值為1，負值為0。

### 訓練/測試資料集 (Training Set / Test Set)
- 取最新的 500筆資料作為本實驗的資料集
- 以資料集的前 80%的資料集作為訓練集
- 以資料集的後 20%的資料集作為測試集

### 演算法 (Algrithms)
- 以 Support-Vector Machine(SVM) 演算法進行訓練

### 評量方式 (Evaluation)
- 以正確率 (Accurancy)做為評量模型效果優劣的方式

### 資料欄位列表
- D2-B : Weekly U.S. Refiner Net Input of Crude Oil (Thousand Barrels per Day)
- D2-D : Weekly U. S. Operable Crude Oil Distillation Capacity (Thousand Barrels per Calendar Day)
- D6-D : Weekly U.S. Ending Stocks of Crude Oil (Thousand Barrels)
- D6-E : Weekly U.S. Ending Stocks excluding SPR of Crude Oil (Thousand Barrels)
- D6-I : Weekly U.S. Ending Stocks of Total Gasoline (Thousand Barrels)
- D6-J : Weekly U.S. Ending Stocks of Finished Motor Gasoline (Thousand Barrels)
- D6-S : Weekly U.S. Ending Stocks of Gasoline Blending Components
- D6-AB : Weekly U.S. Ending Stocks of Distillate Fuel Oil
- D7-B : Weekly U.S. Days of Supply of Crude Oil excluding SPR (Number of Days)

## 實驗結果

- Accuracy for training set: 0.67
- Accuracy for test set: 0.63

