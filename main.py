import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv('log2.csv').to_numpy()
# missing_values = df.isnull().sum()
caracteristicas = df[:,np.array([0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11])]
Y = df[:,np.array([4])]
X_train, X_test, y_train, y_test = train_test_split(caracteristicas, Y, test_size=0.15, random_state=27)

# Refresion Logistica
Clasif = LogisticRegression()
y_pred = Clasif.fit(X_train, y_train).predict(X_test)
print('\n Matriz de confusion: col - realidad, filas - predicc\n')
print(confusion_matrix(y_pred, y_test))
print('\n Accuracy Reg_Lin: %.4f' % accuracy_score(y_pred, y_test ))

# LDA