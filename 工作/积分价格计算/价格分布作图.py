import math
import numpy as np
import matplotlib.pyplot as plt

u = 2206   # 均值μ
sig = 395  # 标准差δ
x = np.linspace(u - 3*sig, u + 3*sig, 50)   # 定义域
y = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2*math.pi)*sig) # 定义曲线函数
plt.plot(x, y, "g", linewidth=2)    # 加载曲线
plt.xlabel('price(¥)')
# plt.grid(True)  # 网格线
plt.show()  # 显示