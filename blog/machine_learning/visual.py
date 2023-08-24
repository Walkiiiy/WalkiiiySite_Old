# 导入库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 读取训练集和测试集文件
train_data = pd.read_csv('/home/walkiiiy/walkiiiy_site/blog/machine_learning/train.csv')
test_data = pd.read_csv('/home/walkiiiy/walkiiiy_site/blog/machine_learning/test.csv')

# 相关性热力图
#sns.heatmap(train_data.corr().abs(), cmap='YlOrRd')#corr用于计算列之间的相关性
#plt.show()
# x7分组下标签均值
#sns.barplot(x='x7', y='target', data=train_data)
#plt.show()
#时间戳小时提取
train_data['common_ts']=pd.to_datetime(train_data['common_ts'],unit='ms')#将字符或数值类型转换为时间类型
train_data['common_ts_hour']=train_data['common_ts'].dt.hour#.dt方法提取时间信息
#print(train_data['common_ts_hour'])#返回int类型小时时间
sns.boxplot(x='x3',y='target',data=train_data)
plt.show()