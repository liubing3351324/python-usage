import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-0.5, 0.5, 0.01)
y=0.2*1 / (1 + np.exp(-x*5*5))

plt.grid()  # 生成网格
plt.plot(x,y)
plt.show()