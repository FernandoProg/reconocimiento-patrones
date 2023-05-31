# reconocimiento-patrones

## Bibliografia
[Dataset](https://archive.ics.uci.edu/ml/datasets/Internet+Firewall+Data): Este conjunto de datos se recopiló a partir de los registros de tráfico de internet del cortafuegos de una universidad.  
[Artículo](https://www.researchgate.net/profile/Pedro-Navarro-Lorente/publication/328335601_Sistema_de_aprendizaje_basado_en_vision_por_computador_para_la_inspeccion_automatizada_de_particulas_magneticas_en_estructuras_marinas/links/5bc71e8d299bf17a1c56289b/Sistema-de-aprendizaje-basado-en-vision-por-computador-para-la-inspeccion-automatizada-de-particulas-magneticas-en-estructuras-marinas.pdf): Sistema de aprendizaje basado en visión por computador para la inspección automatizada de partículas magnéticas en estructuras marinas

## Problema 1.

### 1. Describa el dataset, identificando las características y la variable de clasificación, que tipo de datos es cada una, y que valores toma la variable de clasificación. ¿El dataset presenta datos faltantes?  
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

### 2. Para el clasificador que propone como solución modifique los parámetros que tiene disponibles en la implementación de sklearn. Construya una tabla como la que aparece a continuación y escoja cuáles son los valores óptimos de los parámetros (pruebe al menos con 5 valores de los parámetros). Tome uno de los parámetros y grafique su relación con la métrica de desempeño. Interprete esta gráfica de acuerdo con el posible underfitting u overfitting del modelo.
| criterion | splitter | min_impurity_decrease | max_leaf_nodes | max_depth | accuracy promedio por clase |
|-----------|----------|-----------------------|----------------|-----------|-----------------------------|
| gini      | best     | 0.09                  | 66             | 2         | 0.9795523906408952          |
| entropy   | best     | 0.09                  | 66             | 2         | 0.9795523906408952          |
| log_loss  | best     | 0.09                  | 66             | 2         | 0.9795523906408952          |
| gini      | random   | 0.09                  | 66             | 2         | 0.9513733468972533          |
| entropy   | random   | 0.09                  | 66             | 2         | 0.9474059003051882          |
| log_loss  | random   | 0.09                  | 66             | 2         | 0.9712105798575789          |

### 3. Del clasificador que propone como solución del problema entregue una tabla que muestre los resultados de la matriz de confusión, así como los valores de las métricas de recall y precision de cada clase. Tome como referencia la que aparece a continuación. Interprete un valor de recall y precision. Obtenga las métricas de accuracy y accuracy promedio por clase, comente la diferencia entre estos valores
|            | allow | drop  | deny  | reset-both | Recall |
|------------|-------|-------|-------|------------|--------|
| allow      | 5612  | 0     | 0     | 0          | 1.000  |
| drop       | 0     | 2086  | 0     | 9          | 0.995  |
| deny       | 67    | 125   | 1931  | 0          | 0.909  |
| reset-both | 0     | 0     | 0     | 0          | 0.000  |
| Precision  | 0.988 | 0.943 | 1.000 | 0.000      |        |

El valor de Recall en la fila allow es de 1 lo que nos indica que el modelo es capaz de clasificar de manera correcta el 100% de las veces los datos pertenecientes a esta clase, pero al mirar el valor de Precision de la columna allow podemos notar que no es 1, sino que tiene un valor de 0.988 lo que significa que aunque clasifique de manera correcta todos los datos de la clase allow, no todos los datos clasificados como allow estan correctos ya que en este ejemplo tenemos 67 datos de tipo deny como falsos positivos.

## 4. Ocupe alguno de los métodos vistos en clase para reducir la dimensión de las características del problema y evalúe su impacto en las soluciones obtenidas (compare las métricas de desempeño). Pruebe al menos con la mitad de las características y con dos características. 
- Con reduccion de dimensionalidad balanceadas a 2 caractarísticas obtenemos una precisión del 0.7404
- Con reduccion de dimensionalidad balanceadas a 3 caractarísticas obtenemos una precisión del 0.9230
- Con reduccion de dimensionalidad balanceadas a 5 caractarísticas obtenemos una precisión del 0.9228

### 5. Ocupe algún método de balanceo de clases de ser necesario y evalúe su impacto en las soluciones obtenidas (compare las métricas de desempeño y la matriz de confusión).
- Con reduccion de dimensionalidad balanceadas a 2 caractarísticas obtenemos una precisión del 0.6976
- Con reduccion de dimensionalidad balanceadas a 3 caractarísticas obtenemos una precisión del 0.9162
- Con reduccion de dimensionalidad balanceadas a 5 caractarísticas obtenemos una precisión del 0.6704

## Problema 2.

### 1. ¿Cuál es el problema práctico que se busca resolver? ¿Por qué es relevante? ¿Por qué se propone resolverlo mediante métodos de reconocimiento de patrones?
El artículo propuesto titulado "Sistema de aprendizaje basado en visión por computadora para la inspección automatizada de partículas magnéticas en estructuras marinas" aborda el problema de la inspección de partículas magnéticas en estructuras marinas. Este problema es relevante debido a que las estructuras marinas, como plataformas petroleras, barcos y tuberías submarinas, están expuestas a condiciones ambientales adversas y pueden sufrir daños o corrosión a lo largo del tiempo. La detección y evaluación temprana de defectos y fallas en estas estructuras es crucial para garantizar su integridad y seguridad.  

El método propuesto para abordar este problema es mediante técnicas de reconocimiento de patrones basadas en visión por computadora. Estos métodos se utilizan porque permiten analizar y procesar de manera eficiente grandes volúmenes de datos visuales para detectar patrones y anomalías. En el caso de la inspección automatizada de partículas magnéticas, se utilizan cámaras y algoritmos de visión por computadora para capturar imágenes de las estructuras marinas y analizarlas en busca de partículas magnéticas y posibles defectos.  

El uso de métodos de reconocimiento de patrones en este contexto ofrece varias ventajas. Permite una inspección más rápida y precisa en comparación con los métodos manuales tradicionales. Además, al automatizar el proceso de inspección, se reduce la dependencia de operadores humanos y se minimizan los errores humanos. Esto resulta en una mayor eficiencia y confiabilidad en la detección de defectos en las estructuras marinas.
### 2. ¿Qué métodos de clasificación se emplean en el trabajo? ¿Por qué éstos y no otros?
Los métodos utilizados fueron kNN, NBC y SVM. Escogidos por sus dispares procedimientos de clasificación que se describen a continuación
- kNN es un método de clasificación no-paramétrico en espacios multidimensionales
- NBC utiliza el teorema de Bayes para realizar un aprendizaje basado en probabilidad
- SVM es un clasificador supervisado que busca la separación óptima de las clases mediante la creación de hiperplanos
### 3. ¿Cuál es la metodología empleada en el trabajo? ¿Cómo se diseñan los experimentos? ¿Qué tipos de datos se emplean? ¿Qué métricas se usan para medir los resultados?, etc.
1. ENSAYO DE PARTÍCULAS MAGNÉTICAS EN ESTRUCTURAS MARINAS: La estructuras dañadas son extraídas y utilizadas en un ensayo de partículas magnéticas donde se busca encontrar fallas estructurales, para luego rociar con partículas de hierro reflectantes bajo luz UV para que se acoplen a las partes que presentan fallas haciendo mas fácil la toma de una imagen bajo luz UV.
2. EXTRACCIÓN DE MUESTRAS
    1. Captura de imágenes: Las imágenes fueron capturadas manualmente con estación de visión por computador y una cámara color IDS UI-6230SE-C colocada sobre un brazo de 6 grados de libertad sobre la pieza a inspeccionar a una distancia de un metro. La iluminación empleada consistió un sistema de radiación UV-A de 365 nm
    2. Procesado de imágenes: La imágenes son procesadas buscando el reducir ruidos, resaltar elementos de interés, suavizar objetos, realizar transformaciones morfológicas, realizar cambios de espacios de color, etc. y luego estas imágenes son utilizadas bajo distintos espacios de color para facilitar la extracción de información.
    3. Extracción de características: Se utilizan imágenes de estructura clasificadas como defectuosas para luego extraer distintas características como las dimensiones de la falla, intensidad de los pixeles bajo distintos espacios de color, etc.
3. ENTRENAMIENTO DE LOS MODELOS
4. VERIFICACIÓN DE RESULTADOS
### 4. ¿Cuáles fueron los resultados del trabajo y que se concluyó? Discuta gráficos, comparaciones, etc

### 5. ¿Qué hubiese hecho usted diferente? ¿Por qué?
