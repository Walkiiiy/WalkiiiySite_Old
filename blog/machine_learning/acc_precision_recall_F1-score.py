#acc
from sklearn.metrics import accuracy_score

y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]

accuracy_score(y_true, y_pred)


#F1-score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

y_true = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
y_pred = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

f1_score(y_true, y_pred, average=None)

f1_score(y_true, y_pred, average='macro')  # (0.54545455+0.44444444)/2

f1_score(y_true, y_pred, average='weighted')  # 0.54545455*0.3+0.44444444*0.7

f1_score(y_true, y_pred, average='micro')  # 等于Accuracy
print(accuracy_score(y_true, y_pred))

#precision
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score

y_true = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
y_pred = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

precision_score(y_true, y_pred, average=None)

precision_score(y_true, y_pred, average='macro')  # (0.375 + 1.)/2

precision_score(y_true, y_pred, average='weighted')  # 0.375*0.3+1*0.7

precision_score(y_true, y_pred, average='micro')  # 等于Accuracy
accuracy_score(y_true, y_pred)

#recall
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score

y_true = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
y_pred = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

recall_score(y_true, y_pred, average=None)  # 3个0都被召回了，7个1只有2个被召回

recall_score(y_true, y_pred, average='macro')  # (1. + 0.28571429)/2

recall_score(y_true, y_pred, average='weighted')  # 1*0.3+0.28571429*0.7

recall_score(y_true, y_pred, average='micro')  # 等于Accuracy
accuracy_score(y_true, y_pred)




