import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import tree
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler 

df = pd.read_csv('log2.csv').to_numpy()
# missing_values = df.isnull().sum()
caracteristicas = df[:,np.array([0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11])]
Y = df[:,np.array([4])]
X_train, X_test, y_train, y_test = train_test_split(caracteristicas, Y, test_size=0.15, random_state=27)
pca = PCA(n_components=5)
pca.fit(X_train)
Xtrain_pca=pca.transform(X_train)
Xtest_pca=pca.transform(X_test)
scaler = StandardScaler()  
scaler.fit(Xtrain_pca)  
Xtrain_pca = scaler.transform(Xtrain_pca)  
Xtest_pca = scaler.transform(Xtest_pca)
# Trees
Clasif = tree.DecisionTreeClassifier(criterion='gini', splitter='best',min_impurity_decrease=0.09, max_leaf_nodes=66, max_depth=2)
y_pred = Clasif.fit(Xtrain_pca, y_train).predict(Xtest_pca)
print('Trees')
print('\n Matriz de confusion: col - realidad, filas - predicc\n')
print(confusion_matrix(y_pred, y_test))
#precision - accuracy
print('\n Accuracy Trees: %.4f' % accuracy_score(y_pred, y_test ))
# criterion
# 0.9978453713123091  gini
# 0.9978677517802643  entropy
# 0.9978708036622582  log_loss
# splitter y log_loss
# 0.9978687690742624 best
# 0.997438453713123 random
# max_leaf_nodes
# 0.9985757884028484 66
# min_impurity_decrease
# 0.9985757884028484
# max_depth
# 0.9795523906408952

# gini best 0.09 66 2
# 0.9795523906408952
# entropy best 0.09 66 2
# 0.9795523906408952
# log_loss best 0.09 66 2 *
# 0.9795523906408952
# gini random 0.09 66 2
# 0.9513733468972533
# entropy random 0.09 66 2
# 0.9474059003051882
# log_loss random 0.09 66 2
# 0.9712105798575789
