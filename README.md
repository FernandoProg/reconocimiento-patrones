# reconocimiento-patrones

## Dataset
Pincha [aqui](https://archive.ics.uci.edu/ml/datasets/Internet+Firewall+Data) para mas informacion del dataset

## Problema 1.

## 1. Describa el dataset, identificando las características y la variable de clasificación, que tipo de datos es cada una, y que valores toma la variable de clasificación. ¿El dataset presenta datos faltantes?  
|                      | Característica | Clasificador | Tipo de dato | Valores                              |
|----------------------|----------------|--------------|--------------|--------------------------------------|
| Source Port          |        x       |              |     int64    |                                      |
| Destination Port     |        x       |              |     int64    |                                      |
| NAT Source Port      |        x       |              |     int64    |                                      |
| NAT Destination Port |        x       |              |     int64    |                                      |
| Action               |                |       x      |    object    | ['allow' 'drop' 'deny' 'reset-both'] |
| Bytes                |        x       |              |     int64    |                                      |
| Bytes Sent           |        x       |              |     int64    |                                      |
| Bytes Received       |        x       |              |     int64    |                                      |
| Packets              |        x       |              |     int64    |                                      |
| Elapsed Time (sec)   |        x       |              |     int64    |                                      |
| pkts_sent            |        x       |              |     int64    |                                      |
| pkts_received        |        x       |              |     int64    |                                      |
No hay datos faltantes en el dataset.

## 2. Para el clasificador que propone como solución modifique los parámetros que tiene disponibles en la implementación de sklearn. Construya una tabla como la que aparece a continuación y escoja cuáles son los valores óptimos de los parámetros (pruebe al menos con 5 valores de los parámetros). Tome uno de los parámetros y grafique su relación con la métrica de desempeño. Interprete esta gráfica de acuerdo con el posible underfitting u overfitting del modelo.
| criterion | splitter | min_impurity_decrease | max_leaf_nodes | max_depth | accuracy promedio por clase |
|-----------|----------|-----------------------|----------------|-----------|-----------------------------|
| gini      | best     | 0.09                  | 66             | 2         | 0.9795523906408952          |
| entropy   | best     | 0.09                  | 66             | 2         | 0.9795523906408952          |
| log_loss  | best     | 0.09                  | 66             | 2         | 0.9795523906408952          |
| gini      | random   | 0.09                  | 66             | 2         | 0.9513733468972533          |
| entropy   | random   | 0.09                  | 66             | 2         | 0.9474059003051882          |
| log_loss  | random   | 0.09                  | 66             | 2         | 0.9712105798575789          |

## 3. Del clasificador que propone como solución del problema entregue una tabla que muestre los resultados de la matriz de confusión, así como los valores de las métricas de recall y precision de cada clase. Tome como referencia la que aparece a continuación. Interprete un valor de recall y precision. Obtenga las métricas de accuracy y accuracy promedio por clase, comente la diferencia entre estos valores
|            | allow | drop  | deny  | reset-both | Recall |
|------------|-------|-------|-------|------------|--------|
| allow      | 5612  | 0     | 0     | 0          | 1.000  |
| drop       | 0     | 2086  | 0     | 9          | 0.995  |
| deny       | 67    | 125   | 1931  | 0          | 0.909  |
| reset-both | 0     | 0     | 0     | 0          | 0.000  |
| Precision  | 0.988 | 0.943 | 1.000 | 0.000      |        |

## 4. Ocupe alguno de los métodos vistos en clase para reducir la dimensión de las características del problema y evalúe su impacto en las soluciones obtenidas (compare las métricas de desempeño). Pruebe al menos con la mitad de las características y con dos características. 
- Con reduccion de dimensionalidad balanceadas a 2 caractarísticas obtenemos una precisión del 0.7404
- Con reduccion de dimensionalidad balanceadas a 3 caractarísticas obtenemos una precisión del 0.9230
- Con reduccion de dimensionalidad balanceadas a 5 caractarísticas obtenemos una precisión del 0.9228

## 5. Ocupe algún método de balanceo de clases de ser necesario y evalúe su impacto en las soluciones obtenidas (compare las métricas de desempeño y la matriz de confusión).
- Con reduccion de dimensionalidad balanceadas a 2 caractarísticas obtenemos una precisión del 0.6976
- Con reduccion de dimensionalidad balanceadas a 3 caractarísticas obtenemos una precisión del 0.9162
- Con reduccion de dimensionalidad balanceadas a 5 caractarísticas obtenemos una precisión del 0.6704
