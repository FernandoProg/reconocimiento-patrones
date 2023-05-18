import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import linear_model
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import tree
from sklearn import neighbors

df = pd.read_csv('log2.csv').to_numpy()
# missing_values = df.isnull().sum()
caracteristicas = df[:,np.array([0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11])]
Y = df[:,np.array([4])]
X_train, X_test, y_train, y_test = train_test_split(caracteristicas, Y, test_size=0.15, random_state=27)

# Regresion Logistica
Clasif = LogisticRegression()
y_pred = Clasif.fit(X_train, y_train).predict(X_test)
print('Regresion Logistica')
print('\n Matriz de confusion: col - realidad, filas - predicc\n')
print(confusion_matrix(y_pred, y_test))
print('\n Accuracy Reg_Log: %.4f' % accuracy_score(y_pred, y_test ))

# LDA
Clasif = LinearDiscriminantAnalysis()
y_pred = Clasif.fit(X_train, y_train).predict(X_test)
print('LDA')
print('\n Matriz de confusion: col - realidad, filas - predicc\n')
print(confusion_matrix(y_pred, y_test))
print('\n Accuracy Reg_LDA: %.4f' % accuracy_score(y_pred, y_test ))

# Regresion Lineal
NumClases=4
Y[Y == 'allow'] = 0
Y[Y == 'drop'] = 1
Y[Y == 'deny'] = 2
Y[Y == 'reset-both'] =3
y = np.array([])
for i in Y:
    y=np.append(y,i[0]).astype(int)
y_codif=np.zeros([y.shape[0],NumClases])

for n in range(0,y.shape[0]):
    y_codif[n,y[n]]=1
X_train, X_test, y_train, y_test = train_test_split(caracteristicas, y_codif, test_size=0.15, random_state=27)
regr0 = linear_model.LinearRegression()
regr1 = linear_model.LinearRegression()
regr2 = linear_model.LinearRegression()
regr3 = linear_model.LinearRegression()
regr0.fit(X_train, y_train[:,0])
regr1.fit(X_train, y_train[:,1])
regr2.fit(X_train, y_train[:,2])
regr3.fit(X_train, y_train[:,3])
y_predict0= regr0.predict(X_test)
y_predict1= regr1.predict(X_test)
y_predict2= regr2.predict(X_test)
y_predict3= regr3.predict(X_test)
Y_regr=np.array([y_predict0, y_predict1, y_predict2, y_predict3])
Y_predictor=np.argmax(Y_regr, axis=0)
ytest_dec=np.zeros(y_test.shape[0])
for n in range(0,y_test.shape[0]):
    ytest_dec[n]=np.where(y_test[n,:]==1)[0][0]
#matriz de confusion
print('Regresion Lineal')
print('\n Matriz de confusion: col - realidad, filas - predicc\n')
print(confusion_matrix(Y_predictor, ytest_dec))
#precision - accuracy
print('\n Accuracy Reg_Lin: %.4f' % accuracy_score(Y_predictor, ytest_dec))

# Perceptron
Y = df[:,np.array([4])]
X_train, X_test, y_train, y_test = train_test_split(caracteristicas, Y, test_size=0.15, random_state=27)
Clasif = Perceptron()
y_pred = Clasif.fit(X_train, y_train).predict(X_test)
print('Perceptron')
print('\n Matriz de confusion: col - realidad, filas - predicc\n')
print(confusion_matrix(y_pred, y_test))
#precision - accuracy
print('\n Accuracy Perceptron: %.4f' % accuracy_score(y_pred, y_test ))

# Metlin
y_pred = Clasif.fit(X_train, y_train).predict(X_test)
print('Metlin')
print('\n Matriz de confusion: col - realidad, filas - predicc\n')
print(confusion_matrix(y_pred, y_test))
#precision - accuracy
print('\n Accuracy Metlin: %.4f' % accuracy_score(y_pred, y_test ))

# Naive Bayes
Clasif = GaussianNB()
y_pred = Clasif.fit(X_train, y_train).predict(X_test)
print('Naive Bayes')
print('\n Matriz de confusion: col - realidad, filas - predicc\n')
print(confusion_matrix(y_pred, y_test))
#precision - accuracy
print('\n Accuracy Naive Bayes: %.4f' % accuracy_score(y_pred, y_test ))

# # SVM no lineal
# # Clasif = svm.SVC(kernel="rbf", C=10)
# # Clasif = svm.SVC(kernel="rbf", gamma=0.2)
# Clasif = svm.SVC(kernel="rbf", C=0.1)
# y_pred = Clasif.fit(X_train, y_train).predict(X_test)
# print('SVM no lineal')
# print('\n Matriz de confusion: col - realidad, filas - predicc\n')
# print(confusion_matrix(y_pred, y_test))
# #precision - accuracy
# print('\n Accuracy SVM no lineal: %.4f' % accuracy_score(y_pred, y_test ))


# Trees
Clasif = tree.DecisionTreeClassifier()
y_pred = Clasif.fit(X_train, y_train).predict(X_test)
print('Trees')
print('\n Matriz de confusion: col - realidad, filas - predicc\n')
print(confusion_matrix(y_pred, y_test))
#precision - accuracy
print('\n Accuracy Trees: %.4f' % accuracy_score(y_pred, y_test ))

# KNN 
Clasif = neighbors.KNeighborsClassifier(15, weights="distance")
y_pred = Clasif.fit(X_train, y_train).predict(X_test)
print('\n Matriz de confusion: col - realidad, filas - predicc\n')
print(confusion_matrix(y_pred, y_test))
#precision - accuracy
print('\n Accuracy KNN: %.4f' % accuracy_score(y_pred, y_test ))