
#混淆矩阵


#二分类混淆矩阵
import matplotlib.pyplot as plt
import scikitplot as skplt
from sklearn.metrics import accuracy_score

y_pred = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
y_true = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

accuracy_score(y_true, y_pred)
skplt.metrics.plot_confusion_matrix(y_true, y_pred, normalize=True)
plt.show()


#多分类混淆矩阵
import matplotlib.pyplot as plt
import scikitplot as skplt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = RandomForestClassifier(n_estimators=5, max_depth=5, random_state=1)
clf.fit(X, y)
clf.score(X, y)
pred = clf.predict(X)

skplt.metrics.plot_confusion_matrix(y, pred, normalize=True)
plt.show()
