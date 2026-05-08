# Practica3_MSR
Practica 3 de modelado y simulacion de robots: gazebo + rviz + ros2 + moveit

## Parte A
### Imagen del robot en Rviz  
![Imagen Rviz](https://github.com/jmartinm2021/Practica3_MSR/blob/main/media/modelo_rviz.png)  
  
### Imagen de los frames en Rviz  
![Imagen frames](https://github.com/jmartinm2021/Practica3_MSR/blob/main/media/modelo_rviz_frames.png)  
  
### Video de la demostracion de la Parte A  
[![Video de la Parte A](https://img.youtube.com/vi/0tbewH5eLeE/0.jpg)](https://youtu.be/0tbewH5eLeE)

### Imagen arbol de links  
Separe los frames normativos (para control y navegacion) de los visuales (para apariencia), colgando estos ultimos de los primeros mediante joints fijos, para cumplir REP-103 sin alterar los meshes originales.  
  
![Imagen links](https://github.com/jmartinm2021/Practica3_MSR/blob/main/media/frames_2026-05-04_17.28.16.pdf)  

## Parte B
### Video de la demostracion de la Parte B  
[![Video de la Parte B](https://img.youtube.com/vi/xcdt0nWppis/0.jpg)](https://youtu.be/xcdt0nWppis)

### Graficas
#### Grafica G Parcial vs Tiempo  
![Grafica vs G](https://github.com/jmartinm2021/Practica3_MSR/blob/main/media/grafica_gasto_parcial.png)  
En esta grafica se muestran la G-Parcial del pick and place:
- Se aprecian dos monotañas claras que se mantienen durante un periodo prolongado de tiempo.
- La primera montaña se generea debido a que durante ese tiempo el robot tiene agarrada y suspendido en el aire el cubo de color verde
- La segunda montaña se genera debido a que el robot sostiene el cubo azul hasta que lo suelta encima del rojo
  
### Grafica Posicion de las Ruedas vs Tiempo
![Grafica vs Pos](https://github.com/jmartinm2021/Practica3_MSR/blob/main/media/grafica_posicion_ruedas.png)  
En esta grafica se muestran la posicion de las ruedas:
- Pese a que se intentan representar todas las ruedas, se terminan aggrupando en 2 (IZQ y DRCH) debido a que el controlador mueve las ruedas 3 a 3
- Cuando la pos de un lateral aumenta y la otra disminuye indica un giro del robot (ya que para eso el robot mueve unas ruedas hacia delante y otras hacia atras), tal y como ocurre al principio, mientras que cuando se ve que la pos de ambos lados aumenta o disminuye indica que el robot estaaba avanzando o retrocediendo como sucede ya al final de la grafica.
  
### Grafica Aceleracion vs Tiempo
![Grafica vs Acc](https://github.com/jmartinm2021/Practica3_MSR/blob/main/media/grafica_aceleracion_imu.png)  
En esta grafica se muestran la aceleracion en los 3 ejes:
- En el eje X e Y: a lo largo de la grafica se aprecian picos en ambos ejes que suelen coincidir en el mismo momento, estos casos son cuando el robot estaba girando.
- En el eje Z: el valor se mantiene casis siempre constante en unos 9.8 correspondiendo a la aceleracion de la gravedad
