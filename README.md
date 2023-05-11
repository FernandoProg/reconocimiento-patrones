# reconocimiento-patrones

## Dataset
Pincha [aqui](https://archive.ics.uci.edu/ml/datasets/Internet+Firewall+Data) para mas informacion del dataset

##### Describa el dataset, identificando las características y la variable de clasificación, que tipo de datos es cada una, y que valores toma la variable de clasificación. ¿El dataset presenta datos faltantes?  
#
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