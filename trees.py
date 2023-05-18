import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

df = pd.read_csv('log2.csv').to_numpy()
# missing_values = df.isnull().sum()
caracteristicas = df[:,np.array([0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11])]
Y = df[:,np.array([4])]
prom_trees = np.array([])
for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(caracteristicas, Y, test_size=0.15, random_state=27)
    # Trees
    Clasif = tree.DecisionTreeClassifier(criterion='log_loss', splitter='best',min_impurity_decrease=i/100, max_leaf_nodes=66)
    y_pred = Clasif.fit(X_train, y_train).predict(X_test)
    # print('Trees')
    # print('\n Matriz de confusion: col - realidad, filas - predicc\n')
    # print(confusion_matrix(y_pred, y_test))
    # #precision - accuracy
    # print('\n Accuracy Trees: %.4f' % accuracy_score(y_pred, y_test ))
    prom_trees = np.append(prom_trees, accuracy_score(y_pred, y_test ))
print(np.max(prom_trees))
plt.plot(prom_trees)
plt.show()
# criterion
# 0.9978453713123091  gini
# 0.9978677517802643  entropy
# 0.9978708036622582  log_loss
# splitter y log_loss
# 0.9978687690742624 best
# 0.997438453713123 random
# max_leaf_nodes
# 0.9985757884028484 66

