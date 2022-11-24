import numpy as np

x1, y1, x2, y2, x3, y3 = [float(i) for i in input().split()]
array_longi  = np.array([x2-x1, y2-y1])
array_trans = np.array([x2-line_start_x, y2-line_start_y])
 # Рассчитать расстояние от точки до прямой линии с вектором
 array_temp = (float (array_trans.dot (array_longi)) / array_longi.dot (array_longi)) # Обратите внимание на преобразование в операции с плавающей запятой
array_temp = array_longi.dot(array_temp)
distance   = np.sqrt((array_trans - array_temp).dot(array_trans - array_temp))